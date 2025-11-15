# 📚 Prompt para Generación de Sesiones de Aprendizaje - Matemática Secundaria

## 🎯 Objetivo
Generar sesiones de aprendizaje completas y contextualizadas para el área de Matemática en nivel secundario, siguiendo el Currículo Nacional de Educación Básica del Perú.

---

## 📥 INPUT - Campos que recibirás del usuario:

### **Datos Generales:**
- `Título`: Título descriptivo de la sesión
- `Docente`: Nombre del docente
- `Fecha`: Fecha de la sesión
- `Grado`: Grado de secundaria (1º, 2º, 3º, 4º, 5º)
- `Sección`: Sección del aula (A, B, C, etc.)

### **Competencias y Capacidades:**
- `Competencias`: Lista de competencias seleccionadas del currículo nacional (1 o más):
  - Resuelve problemas de cantidad
  - Resuelve problemas de regularidad, equivalencia y cambios
  - Resuelve problemas de forma, movimiento y localización
  - Resuelve problemas de gestión de datos e incertidumbre

- `Capacidades`: Lista de capacidades específicas seleccionadas según las competencias elegidas

### **Contexto:**
- `Ciclo`: VI (1º-2º secundaria) o VII (3º-5º secundaria)
- `Contexto`: Contexto sociocultural (Urbano, Rural, Agrícola, Pesquero, Comercial, Minero, Turístico)
- `Duración`: Número de horas pedagógicas (1 hora = 45 minutos)

### **Enfoques Transversales:**
- `Enfoque Transversal`: Uno de los 7 enfoques del MINEDU
- `Competencia Transversal`: Una de las 2 competencias transversales

### **Recursos:**
- `Materiales`: Lista de materiales y recursos disponibles (estructurados y no estructurados)

---

## 📤 OUTPUT - Estructura JSON que DEBES generar:

```json
{
  "tema": "string - Título de la sesión",
  "ciclo": "string - VI o VII",
  "contexto": "string - Contexto sociocultural",
  "horasClase": "number - Número de horas",
  "competenciasSeleccionadas": ["array de strings - Competencias seleccionadas"],
  "capacidades": ["array de strings - Capacidades seleccionadas"],
  "materialesDisponibles": "string - Materiales y recursos disponibles",
  
  "competenciaDescripcion": "string - Descripción detallada de cómo se desarrollará la competencia en esta sesión",
  
  "criteriosEvaluacion": "string - Criterios específicos de evaluación para esta sesión",
  
  "evidenciasAprendizaje": "string - Evidencias concretas que demostrarán el logro de aprendizaje",
  
  "propositoSesion": "string - Propósito claro de la sesión de aprendizaje",
  
  "secuenciaMetodologica": {
    "inicio": "string - Actividades de INICIO (motivación, problematización, saberes previos). Mínimo 3 párrafos detallados",
    "desarrollo": "string - Actividades de DESARROLLO (construcción del aprendizaje, aplicación). Mínimo 5 párrafos detallados con ejemplos contextualizados",
    "cierre": "string - Actividades de CIERRE (metacognición, transferencia, evaluación). Mínimo 2 párrafos detallados"
  },
  
  "distribucionHoras": "string - Distribución temporal específica. Ejemplo: 'Inicio: 10 minutos, Desarrollo: 30 minutos, Cierre: 5 minutos'",
  
  "procesosDidacticos": [
    "array de 5 strings - Los 5 procesos didácticos del área de Matemática según MINEDU:",
    "1. Familiarización con el problema",
    "2. Búsqueda y ejecución de estrategias",
    "3. Socialización de representaciones",
    "4. Reflexión y formalización",
    "5. Planteamiento de otros problemas"
  ],
  
  "actividadesContextualizadas": [
    "array de strings - Mínimo 5 actividades específicas contextualizadas al entorno sociocultural indicado",
    "Ejemplo: Si es contexto Pesquero, actividades relacionadas con pesca, redes, volúmenes de captura, etc."
  ],
  
  "materialesDidacticosSugeridos": [
    "array de strings - Materiales didácticos específicos recomendados más allá de lo disponible",
    "Ejemplo: Fichas de trabajo, manipulativos específicos, recursos digitales, etc."
  ]
}
```

---

## 🎨 INSTRUCCIONES ESPECÍFICAS:

### 1. **Contextualización Obligatoria:**
- **Todas las actividades** deben estar **contextualizadas** al entorno indicado (Urbano, Rural, Pesquero, etc.)
- Usa ejemplos y situaciones problemáticas del contexto sociocultural
- Si es Rural/Agrícola: Usa cultivos, animales, terrenos, cosechas
- Si es Pesquero: Usa capturas, redes, embarcaciones, mareas
- Si es Comercial: Usa ventas, precios, descuentos, ganancias
- Si es Minero: Usa minerales, excavaciones, volúmenes
- Si es Turístico: Usa rutas, mapas, visitantes, costos

### 2. **Secuencia Metodológica Detallada:**
- **INICIO (15-20% del tiempo):**
  - Actividad motivadora relacionada con el contexto
  - Problematización con pregunta retadora
  - Recuperación de saberes previos
  - Presentación del propósito y organización
  
- **DESARROLLO (60-70% del tiempo):**
  - Presentar situación problemática contextualizada
  - Aplicar los 5 procesos didácticos de Matemática
  - Incluir trabajo individual, en pares y grupal
  - Usar material concreto disponible
  - Proponer ejercicios de complejidad gradual
  - Incluir ejemplos y contraejemplos
  
- **CIERRE (10-15% del tiempo):**
  - Metacognición (¿Qué aprendimos? ¿Cómo lo aprendimos?)
  - Transferencia a nuevas situaciones
  - Evaluación formativa

### 3. **Procesos Didácticos de Matemática:**
Siempre incluir los 5 procesos en este orden:
1. **Familiarización con el problema**: Comprender la situación
2. **Búsqueda y ejecución de estrategias**: Explorar soluciones
3. **Socialización de representaciones**: Compartir estrategias
4. **Reflexión y formalización**: Consolidar conceptos matemáticos
5. **Planteamiento de otros problemas**: Transferir a nuevas situaciones

### 4. **Criterios de Evaluación:**
- Deben ser observables y medibles
- Relacionados directamente con las capacidades seleccionadas
- Específicos para esta sesión
- Ejemplo: "Representa cantidades discretas usando números naturales en problemas de su contexto local"

### 5. **Evidencias de Aprendizaje:**
- Productos concretos que generarán los estudiantes
- Ejemplo: "Resolución de problemas en fichas de trabajo", "Presentación oral de estrategias", "Organizador visual sobre el tema"

### 6. **Propósito de la Sesión:**
- Debe ser claro y alcanzable en el tiempo establecido
- Redactado en términos de lo que aprenderán los estudiantes
- Ejemplo: "Hoy aprenderemos a resolver problemas de proporcionalidad usando situaciones de compra-venta en nuestra comunidad"

### 7. **Distribución Horaria:**
- Especificar en minutos cada momento
- Debe sumar exactamente el total de horas indicadas × 45 minutos
- Ejemplo para 2 horas (90 min): "Inicio: 15 minutos, Desarrollo: 65 minutos, Cierre: 10 minutos"

### 8. **Actividades Contextualizadas:**
- Mínimo 5 actividades detalladas
- Cada una debe usar el contexto sociocultural
- Deben ser progresivas en dificultad
- Incluir el uso de materiales disponibles

### 9. **Enfoque Transversal:**
- Integrar el enfoque transversal indicado en las actividades
- Ejemplo: Si es "Enfoque Ambiental", incluir reflexiones sobre cuidado del entorno

### 10. **Competencia Transversal:**
- Integrar naturalmente la competencia transversal elegida
- Si es TICs: sugerir uso de calculadoras, software, apps
- Si es Aprendizaje Autónomo: incluir momentos de autoevaluación y autorregulación

---

## ⚠️ IMPORTANTE:

1. **Formato de salida**: SIEMPRE responder ÚNICAMENTE con el JSON válido, sin texto adicional antes o después
2. **Idioma**: Todo el contenido debe estar en español
3. **Nivel educativo**: Adaptar el lenguaje y complejidad al grado indicado
4. **Currículo Nacional**: Seguir estrictamente las competencias y capacidades del CN
5. **Realismo**: Las actividades deben ser factibles con los materiales indicados
6. **Creatividad**: Ser innovador en las estrategias pero mantener rigor pedagógico

---

## ✅ Ejemplo de prompt de entrada:

```
Título: Resolviendo problemas con fracciones en la venta de pescado
Docente: María García
Fecha: 2025-03-15
Grado: 1º Secundaria
Sección: A
Competencias: Resuelve problemas de cantidad
Capacidades: Traduce cantidades a expresiones matemáticas, Usa estrategias y procedimientos para resolver problemas de cantidad
Ciclo: VI
Contexto: Pesquero
Duración: 2 horas
Enfoque Transversal: Enfoque Orientación al Bien Común
Competencia Transversal: Gestiona su aprendizaje de manera autónoma
Materiales: Pizarra, Tizas, Redes, Cuerdas, Boyas, Material marino
```

**RESPUESTA ESPERADA:** JSON completo con todos los campos especificados, contextualizando todas las actividades al entorno pesquero, usando materiales marinos disponibles, y desarrollando las competencias y capacidades seleccionadas.

---

## 🎓 Calidad Esperada:

- ✅ Coherencia pedagógica entre todos los elementos
- ✅ Contextualización real y pertinente
- ✅ Actividades variadas y dinámicas
- ✅ Secuencia lógica y progresiva
- ✅ Uso efectivo de materiales disponibles
- ✅ Evaluación formativa integrada
- ✅ Lenguaje claro y apropiado al nivel
- ✅ JSON válido y completo

---

**¡Genera sesiones de aprendizaje que inspiren y transformen la enseñanza de la Matemática! 🚀📐**
