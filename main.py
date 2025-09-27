from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import chromadb
from google import genai
from google.genai import types
from google.api_core import retry
import os
import re
import json

# ========================
# Configuración de Gemini
# ========================
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GOOGLE_API_KEY)

# ========================
# Base de datos SQLite
# ========================
DB_NAME = "lesson_memory.db"
conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS lesson_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    role TEXT,
    content TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def save_message(session_id, role, content):
    cursor.execute(
        "INSERT INTO lesson_history (session_id, role, content) VALUES (?, ?, ?)", 
        (session_id, role, content)
    )
    conn.commit()

def get_recent_history(session_id, n_turns=3):
    cursor.execute("""
        SELECT role, content FROM lesson_history 
        WHERE session_id=? 
        ORDER BY id DESC LIMIT ?
    """, (session_id, n_turns*2))
    rows = cursor.fetchall()
    return list(reversed(rows))

# ========================
# ChromaDB con currículo escolar
# ========================
class GeminiEmbeddingFunction(chromadb.EmbeddingFunction):
    document_mode = True
    @retry.Retry(predicate=lambda e: isinstance(e, genai.errors.APIError) and e.code in {429,503})
    def __call__(self, input):
        task = "retrieval_document" if self.document_mode else "retrieval_query"
        response = client.models.embed_content(
            model="models/text-embedding-004",
            contents=input,
            config=types.EmbedContentConfig(task_type=task),
        )
        return [e.values for e in response.embeddings]

embed_fn = GeminiEmbeddingFunction()
chroma_client = chromadb.Client()
knowledge_db = chroma_client.get_or_create_collection(
    name="curriculo_secundaria", embedding_function=embed_fn
)

# Documentos curriculares (ejemplo resumido)
documents = [
    "Competencia: Resuelve problemas de cantidad. Capacidades: Traduce cantidades a expresiones numéricas...",
    "Competencia: Resuelve problemas de regularidad, equivalencia y cambios...",
    "Competencia: Resuelve problemas de forma, movimiento y localización...",
    "Competencia: Resuelve problemas de gestión de datos e incertidumbre...",
    "Procesos didácticos de Matemática: Comprensión del problema, Búsqueda y ejecución de estrategias, Socializa sus representaciones, Reflexión y formalización, Planteamiento de otros problemas."
]
knowledge_db.add(documents=documents, ids=[str(i) for i in range(len(documents))])

# ========================
# Procesar mensaje docente
# ========================
def parse_teacher_message(message: str):
    tema = re.search(r"Tema:\s*(.*)", message)
    competencia = re.search(r"Competencia:\s*(.*)", message)
    grado = re.search(r"Grado:\s*(.*)", message)
    contexto = re.search(r"Contexto:\s*(.*)", message)
    duracion = re.search(r"Duración:\s*(.*)", message)

    return {
        "tema": tema.group(1).strip() if tema else "",
        "competencia": competencia.group(1).strip() if competencia else "",
        "grado": grado.group(1).strip() if grado else "",
        "contexto": contexto.group(1).strip() if contexto else "",
        "duracion": duracion.group(1).strip() if duracion else "2 horas"
    }

# ========================
# Construcción del prompt
# ========================
def build_prompt(inputs, retrieved_docs):
    prompt = (
        "Eres un asistente pedagógico experto en Matemática del currículo peruano. "
        "Genera el entregable en formato JSON **válido** siguiendo exactamente esta estructura:\n\n"
        "{\n"
        '  "tema": "",\n'
        '  "ciclo": "",\n'
        '  "contexto": "",\n'
        '  "horasClase": 2,\n'
        '  "competenciasSeleccionadas": [],\n'
        '  "materialesDisponibles": "",\n'
        '  "competenciaDescripcion": "",\n'
        '  "secuenciaMetodologica": {\n'
        '    "inicio": "",\n'
        '    "desarrollo": "",\n'
        '    "cierre": ""\n'
        '  },\n'
        '  "procesosDidacticos": [],\n'
        '  "materialesDidacticosSugeridos": [],\n'
        '  "actividadesContextualizadas": [],\n'
        '  "distribucionHoras": ""\n'
        "}\n\n"
        "Usa la información recibida para llenar los campos.\n\n"
    )
    prompt += f"Tema: {inputs['tema']}\n"
    prompt += f"Competencia: {inputs['competencia']}\n"
    prompt += f"Grado: {inputs['grado']}\n"
    prompt += f"Contexto del aula: {inputs['contexto']}\n"
    prompt += f"Duración: {inputs['duracion']}\n\n"

    if retrieved_docs:
        prompt += "Referencias curriculares relevantes:\n"
        for doc in retrieved_docs:
            prompt += f"- {doc}\n"

    return prompt

def generate_lesson(session_id, message):
    inputs = parse_teacher_message(message)
    query_text = f"{inputs['tema']} {inputs['competencia']} {inputs['grado']}"
    
    embed_fn.document_mode = False
    result = knowledge_db.query(query_texts=[query_text], n_results=3)
    retrieved_docs = result["documents"][0] if result["documents"] else []

    prompt = build_prompt(inputs, retrieved_docs)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    raw_output = response.text

    # Validar que sea JSON
    try:
        lesson_json = json.loads(raw_output)
    except json.JSONDecodeError:
        # Si Gemini devuelve texto no válido, lo encapsulamos
        lesson_json = {"error": "El modelo no devolvió un JSON válido", "raw": raw_output}

    save_message(session_id, "user", message)
    save_message(session_id, "bot", json.dumps(lesson_json, ensure_ascii=False))
    return lesson_json

# ========================
# API FastAPI (WhatsApp / Frontend)
# ========================
app = FastAPI()

# --- CORS Middleware ---
origins = ["*"]  # Ajusta en producción
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "ok", "message": "Generador de sesiones educativas corriendo 🚀"}

@app.post("/webhook")
async def webhook(request: Request):
    form = await request.form()
    user_message = form.get("Body", "")
    session_id = form.get("From", "default_user")

    if not user_message:
        return JSONResponse({"error": "Por favor envía: Tema, Competencia, Grado y Contexto 📚"})

    lesson_plan = generate_lesson(session_id, user_message)
    return JSONResponse(lesson_plan)
