# Manga → Flow/Omni Prompt Engine

**Fecha:** 2026-07-03
**Estado:** Aprobado

## Resumen

Transformar el AI Live Action Studio de un pipeline de generación local (imposible sin GPU) a un **motor de análisis de manga que genera prompts estructurados y listos para usar** en Flow/Omni, donde el usuario ya tiene sus personajes creados.

## Arquitectura

### Flujo

```
Usuario sube página de manga (imagen JPG/PNG + texto opcional)
         │
         ▼
┌─ POST /api/v1/manga/analyze ──────────────────────────┐
│  Body: { "image": base64, "filename": "pagina1.jpg" } │
└──────────────────────┬────────────────────────────────┘
                       ▼
┌─ MangaAnalyzerAgent ───────────────────────────────────┐
│  1. Envía imagen a Ollama (gemma4 multimodal)          │
│  2. Extrae: personajes, escenario, acción, diálogo,    │
│     emociones, paneles, dirección de lectura           │
│  3. Devuelve análisis estructurado JSON                │
└──────────────────────┬────────────────────────────────┘
                       ▼
┌─ SceneComposerAgent ───────────────────────────────────┐
│  1. Recibe análisis del manga                          │
│  2. Divide en escenas (máx 10s cada una)               │
│  3. Para cada escena:                                  │
│     - Personajes presentes + emociones                 │
│     - Descripción de la acción                         │
│     - Shot de cámara (wide/medium/close-up/ECU)        │
│     - Movimiento de cámara (static/pan/tilt/dolly/     │
│       crane/steadicam)                                 │
│     - Iluminación (hora del día, fuente de luz, mood)  │
│     - Duración estimada (≤10s)                         │
│  4. Usa Ollama para decisiones cinematográficas        │
└──────────────────────┬────────────────────────────────┘
                       ▼
┌─ FlowPromptBuilderAgent ───────────────────────────────┐
│  1. Toma la composición de escenas                     │
│  2. Mapea personajes del manga a refs de Flow          │
│     (usuario provee mapping: "Goku" → "personaje_1")  │
│  3. Genera prompt estructurado con secciones:          │
│     - PERSONAJES: nombre, Flow ref, apariencia,        │
│       expresión, pose, posición en cuadro              │
│     - ESCENARIO: locación, hora, clima, props          │
│     - CÁMARA: shot type, movimiento, lente,            │
│       profundidad de campo                             │
│     - ILUMINACIÓN: key light, fill light, rim light,   │
│       color temperature, sombras                       │
│     - MOOD/ATMOSFERA: tono emocional, paleta de color  │
│     - ACCIÓN: qué ocurre en la escena, duración ≤10s   │
│     - SPECS TÉCNICAS: 8k, hiperrealista, cinematográ-  │
│       fico, texturas, volumetric lighting, grain        │
│     - ANTI-ALUCINACIÓN: restricciones explícitas       │
│  4. Devuelve prompt listo para copiar/pegar            │
└──────────────────────┬────────────────────────────────┘
                       ▼
         PROMPT ESTRUCTURADO LISTO
         (copy-paste a Flow/Omni)
```

### Componentes

#### 1. MangaAnalyzerAgent (NUEVO)
- Input: imagen de manga (base64), filename opcional
- Output: JSON con análisis estructurado
- Usa Ollama gemma4 con prompt de sistema especializado en análisis de manga
- Extrae:
  - `panels`: lista de paneles identificados
  - `characters`: personajes detectados (nombre, apariencia, expresión, posición)
  - `setting`: descripción del escenario
  - `action`: acción principal
  - `dialogue`: diálogos extraídos
  - `mood`: estado de ánimo/atmósfera
  - `reading_direction`: dirección de lectura (si aplica)

#### 2. SceneComposerAgent (REFACTOR desde Director + Screenwriter)
- Input: análisis del manga + user preferences
- Output: lista de escenas compuestas
- Cada escena:
  - `scene_id`: int
  - `duration`: float (≤10s)
  - `characters`: lista de personajes en escena
  - `description`: texto de la acción
  - `camera`: shot type, movement, lens
  - `lighting`: condiciones de iluminación
  - `dialogue`: líneas de diálogo
  - `transition`: cómo se conecta con la siguiente escena

#### 3. FlowPromptBuilderAgent (REFACTOR desde PromptBuilder)
- Input: lista de escenas + character mapping del usuario
- Output: prompt estructurado en markdown
- Mapeo de personajes: el usuario provee un dict
  `{"Goku": "personaje_1", "Vegeta": "personaje_2"}`
- El prompt se genera con plantillas que aseguran:
  - Estructura consistente
  - Todas las secciones requeridas
  - Restricciones anti-alucinación
  - Compatibilidad con Flow/Omni

### API Endpoints (REFACTOR)

#### `POST /api/v1/manga/analyze`
Analiza una página de manga y devuelve el prompt listo.

**Request:**
```json
{
  "image": "base64_encoded_image...",
  "filename": "manga_capitulo1_pagina1.jpg",
  "character_mapping": {
    "Goku": "personaje_1",
    "Vegeta": "personaje_2",
    "Freezer": "personaje_3"
  },
  "options": {
    "max_scenes": 5,
    "style": "hyperrealistic_cinematic",
    "resolution": "8k"
  }
}
```

**Response (202 Accepted):**
```json
{
  "job_id": 123,
  "status": "processing",
  "message": "Analizando manga..."
}
```

#### `GET /api/v1/jobs/{job_id}`
Estado del análisis.

**Response (processing):**
```json
{
  "job_id": 123,
  "status": "processing",
  "progress": 45,
  "current_step": "Componiendo escenas..."
}
```

**Response (completed):**
```json
{
  "job_id": 123,
  "status": "completed",
  "result": {
    "manga_analysis": { ... },
    "scenes": [ ... ],
    "prompts": [
      {
        "scene_id": 1,
        "scene_number": 1,
        "duration": 8.5,
        "prompt_text": "...markdown prompt listo para copiar..."
      }
    ]
  }
}
```

### Modelos de datos

Se reutilizan los modelos existentes (`Job`, `Scene`, `Asset`) con ajustes menores.

**Scene** se simplifica:
- Eliminar campos de generación que ya no aplican (shot_type, camera_movement pasan a ser texto libre en el prompt)
- Agregar `prompt_generated` (Text) para almacenar el prompt final

**Asset** se mantiene pero ahora almacena los prompts generados en lugar de archivos.

### Lo que se elimina

- `app/agents/video_generator/` - completo
- `app/agents/voice_generator/` - completo
- `app/agents/music_generator/` - completo
- `app/agents/fx_generator/` - completo
- `app/agents/editor/` - completo
- `app/agents/image_generator/tasks.py` - solo tasks (el agente se refactoriza)
- `app/agents/screenwriter/screenwriter.py` - se reemplaza por SceneComposer
- `app/agents/director/director.py` - se refactoriza para el nuevo flujo

### Lo que se crea

- `app/agents/manga_analyzer/` - MangaAnalyzerAgent
- `app/agents/scene_composer/` - SceneComposerAgent
- `app/agents/flow_prompt_builder/` - FlowPromptBuilderAgent

### Lo que se refactoriza

- `app/agents/prompt_builder/prompt_builder.py` → contenido pasa a flow_prompt_builder
- `app/agents/character_manager/` → recibe método para mapear a Flow
- `app/agents/environment_manager/` → queda pero simplificado
- `app/api/v1/endpoints/manga.py` → endpoint analyze reemplaza a process
- `app/agents/director/director.py` → orquestador del nuevo pipeline
- `app/agents/screenwriter/screenwriter.py` → lógica integrada en SceneComposer

### Tests

- `tests/test_manga_analyzer.py` - testear análisis con imágenes de prueba
- `tests/test_scene_composer.py` - testear composición de escenas
- `tests/test_flow_prompt_builder.py` - testear generación de prompts
- `tests/test_api.py` - actualizar tests de API para nuevo endpoint
- `tests/test_director.py` - actualizar para nuevo flujo

### Anti-alucinación

El prompt generado incluye restricciones explícitas:
- "Mantener el diseño de [personaje] exactamente como en la referencia de Flow"
- "No añadir objetos, personajes o elementos que no estén descritos en la escena"
- "El fondo debe ser coherente con la descripción del escenario"
- "Respetar la hora del día y condiciones de iluminación especificadas"
- "No cambiar la expresión facial ni la pose del personaje respecto a lo indicado"

## Orden de implementación

1. Crear MangaAnalyzerAgent (Ollama visión)
2. Crear SceneComposerAgent
3. Crear FlowPromptBuilderAgent
4. Refactorizar DirectorAgent como orquestador
5. Refactorizar endpoints de API
6. Eliminar agentes de generación obsoletos
7. Tests
8. Rebuild Docker y verificación final
