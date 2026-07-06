# Storyboard Agent & Hybrid Prompt Engine Design

**Fecha:** 2026-07-06
**Estado:** Diseño aprobado

## Resumen

Extender el pipeline Manga → Flow/Omni Prompt Engine con un **StoryboardAgent** que descompone cada escena en múltiples shots individuales (4-8s cada uno), y un **formato de prompt híbrido** que combina contexto global de escena con prompts individuales por shot. Esto reduce alucinaciones y permite copiar cada shot directamente a Flow.

## Arquitectura

### Flujo extendido

```
Usuario sube página de manga
         │
         ▼
┌─ MangaAnalyzerAgent ──────────────────────┐
│  Analiza: personajes, escenario, acción,   │
│  diálogo, mood, paneles                    │
└──────────────────────┬────────────────────┘
                       ▼
┌─ SceneComposerAgent ───────────────────────┐
│  Compone 1-N escenas (≤10s c/u)            │
│  scene = {scene_id, duration, characters,  │
│           description, camera, lighting,    │
│           dialogue, transition}             │
└──────────────────────┬────────────────────┘
                       ▼
┌─ StoryboardAgent (NUEVO) ──────────────────┐
│  Toma 1 escena → N shots (4-8s c/u)        │
│  Cada shot: shot_type, movement, lens,      │
│  duration, action, transition               │
└──────────────────────┬────────────────────┘
                       ▼
┌─ FlowPromptBuilderAgent (EXTENDIDO) ────────┐
│  build_prompts() → scene prompts (existente) │
│  build_storyboard_prompts() → hybrid prompts │
│    ┌──────────────────────────────────────┐ │
│    │ CONTEXTO GLOBAL (escena)             │ │
│    │ ─────────────────────────────────    │ │
│    │ PERSONAJES, ESCENARIO, MOOD,         │ │
│    │ ANTI-ALUCINACIÓN global              │ │
│    ├──────────────────────────────────────┤ │
│    │ STORYBOARD:                          │ │
│    │ SHOT 1: prompt individual completo   │ │
│    │ SHOT 2: prompt individual completo   │ │
│    │ ...                                  │ │
│    └──────────────────────────────────────┘ │
└──────────────────────┬────────────────────┘
                       ▼
          PROMPT HÍBRIDO LISTO
          (copy-paste a Flow/Omni)
```

## Componentes

### 1. StoryboardAgent (NUEVO)

**Archivo:** `app/agents/storyboard/storyboard.py`
**Tests:** `tests/test_storyboard.py`

#### Interfaz

```python
class StoryboardAgent:
    def break_down_scene(self, scene: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Toma una escena compuesta y devuelve N shots.
        Cada shot es un dict con:
          - shot_number: int
          - start_time: float
          - end_time: float
          - shot_type: str (wide, medium, close-up, extreme-close-up)
          - movement: str (static, dolly, pan, tilt, crane, tracking, steadicam)
          - lens: str (ej. "35mm f/2.8")
          - description: str (acción específica del shot)
          - characters_in_frame: List[str] (personajes visibles)
          - focus: str (en qué se enfoca la cámara)
          - transition_in: str (cómo se entra al shot)
          - transition_out: str (cómo se sale del shot)
        """
        pass
```

#### Lógica de descomposición

- Si la escena dura ≤5s → 1 shot (la escena completa)
- Si la escena dura 6-8s → 2 shots (ej: wide + close-up)
- Si la escena dura 9-10s → 2-3 shots
- Cada shot entre 4-8s de duración
- Patrones de descomposición:
  - **Diálogo 1 personaje:** wide (establece) → medium (personaje habla) → close-up (reacción)
  - **Diálogo 2 personajes:** wide (ambos) → over-shoulder (A) → over-shoulder (B) → close-up (clímax)
  - **Acción:** wide (contexto) → tracking (movimiento) → close-up (impacto/efecto)
  - **Silencio/mood:** wide (atmósfera) → slow push-in (tensión) → extreme-close-up (detalle)

#### Decisiones de cinematografía

Basadas en el mood y tipo de escena:

| Mood | Shot types preferidos | Movements preferidos |
|------|----------------------|---------------------|
| tensión | close-up, ECU | slow push-in, static |
| acción | wide, medium | tracking, handheld, pan |
| diálogo | medium, over-shoulder | static, dolly |
| tristeza | wide, close-up | slow dolly out, static |
| épico | extreme-wide, wide | crane, dolly |

### 2. FlowPromptBuilderAgent (EXTENDIDO)

**Archivo:** `app/agents/flow_prompt_builder/flow_prompt_builder.py`

#### Nuevo método

```python
def build_storyboard_prompts(
    self,
    scenes: List[Dict[str, Any]],
    character_mapping: Dict[str, str]
) -> List[Dict[str, Any]]:
    """
    Para cada escena:
      1. Usa StoryboardAgent para dividir en shots
      2. Genera bloque de contexto global (reusa _build_prompt para la escena)
      3. Para cada shot, genera prompt individual con:
         - PERSONAJES (referencias heredadas del contexto)
         - CÁMARA (shot type, movement, lens específicos del shot)
         - ACCIÓN (descripción específica del shot)
         - ILUMINACIÓN (heredada del contexto)
         - SPECS TÉCNICAS (heredadas)
         - ANTI-ALUCINACIÓN (por shot: "mantener exactamente este shot")
    """
    pass
```

#### Formato de salida (híbrido)

```
╔══════════════════════════════════════════════════════════════╗
║ ESCENA 1 — Contexto Global                                  ║
║ ─────────────────────────────────────────────────────────── ║
║ PERSONAJES:                                                 ║
║   - Sarada (Flow ref: sarada_tbv): enojada, primer plano    ║
║   - Shikamaru (Flow ref: shikamaru_tbv): severo, fondo      ║
║                                                             ║
║ ESCENARIO: Oficina del Hokage, día, luz natural cenital     ║
║ MOOD: Tensión política, frustración                         ║
║                                                             ║
║ SPECS TÉCNICAS: (globales)                                  ║
║   - Resolución: 8K (7680x4320)                              ║
║   - Estilo: live-action hiperrealista, cinematográfico      ║
║   - Sin CGI, sin renderizado 3D                             ║
║   - Profundidad de campo: acorde al shot                    ║
║                                                             ║
║ ANTI-ALUCINACIÓN (global):                                  ║
║   - Mantener diseño exacto de Sarada (ref: sarada_tbv)      ║
║   - Mantener diseño exacto de Shikamaru (ref: shikamaru_tbv)║
║   - Fondo coherente: Oficina del Hokage                     ║
╚══════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════╗
║ SHOT 1 (0.0s → 3.5s)                                       ║
║ ─────────────────────────────────────────────────────────── ║
║ TIPO: Medium Shot | MOV: Dolly In | LENTE: 35mm f/2.8     ║
║ TRANSICIÓN: Fade In                                        ║
║                                                             ║
║ PERSONAJES: Sarada (ref: sarada_tbv), enojada, frame center ║
║ ACCIÓN: Sarada golpea el escritorio con impotencia, grita   ║
║ ILUMINACIÓN: Luz cenital, sombras marcadas, mood tenso      ║
║ ANTI-ALUCINACIÓN: Solo Sarada en cuadro, mantener posesión  ║
╚══════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════╗
║ SHOT 2 (3.5s → 7.0s)                                       ║
║ ─────────────────────────────────────────────────────────── ║
║ TIPO: Extreme Close-up | MOV: Static | LENTE: 85mm f/1.4   ║
║ TRANSICIÓN: Cut                                            ║
║                                                             ║
║ PERSONAJES: Shikamaru (ref: shikamaru_tbv), severo, ojos    ║
║ ACCIÓN: Shikamaru entrecierra los ojos, gravedad en rostro  ║
║ ILUMINACIÓN: Luz dura lateral, realza textura piel          ║
║ ANTI-ALUCINACIÓN: Solo ojos y nariz de Shikamaru en cuadro  ║
╚══════════════════════════════════════════════════════════════╝
```

### 3. procesar_pagina.py (ACTUALIZADO)

**Archivo:** `procesar_pagina.py`

#### Cambios

- Después de generar los scene prompts (existente), ejecutar `StoryboardAgent.break_down_scene()` por cada escena
- Pasar los shots a `FlowPromptBuilderAgent.build_storyboard_prompts()`
- Guardar ambos en el archivo de salida: primero prompts de escena (existente), luego prompts de storyboard
- Flag `--storyboard` (default: True) para activar/desactivar

#### Formato de archivo de salida

```
=== PROMPTS DE ESCENA ===
[prompt escena 1]
...
=== PROMPTS DE STORYBOARD ===
[prompt híbrido escena 1]
...
```

### Flujo de datos completo

```
manga_data = {
    "filename": "pagina1.jpg",
    "image": "base64...",
    "character_mapping": {"Sarada": "sarada_tbv"},
    "options": {"max_scenes": 3}
}

DirectorAgent.process_manga_request(manga_data)
  → MangaAnalyzer.analyze(image, filename)        → analysis dict
  → SceneComposer.compose(analysis, max_scenes)    → [scene, ...]
  
  → FlowPromptBuilder.build_prompts(scenes, mapping) → scene prompts
  → (NUEVO) StoryboardAgent.break_down_scene(scene)   → [shot, ...]
  → (NUEVO) FlowPromptBuilder.build_storyboard_prompts(...) → hybrid prompts
  
  → Save to DB: Job, Scene, Asset (scene prompts + storyboard assets)
```

### Anti-alucinación por shot

Cada shot incluye restricciones específicas:
1. "Mantener exactamente este encuadre: [shot_type], [movement]"
2. "Solo [personajes_en_frame] visibles en este shot"
3. "No cambiar la expresión de [personaje] respecto a: [expresión]"
4. "Fondo debe coincidir con: [descripción escenario] en todo el storyboard"

### Tests

#### `tests/test_storyboard.py` (NUEVO)
- `test_break_down_short_scene_single_shot` — escena ≤5s → 1 shot
- `test_break_down_dialogue_scene_two_shots` — escena 6-8s → 2 shots
- `test_break_down_action_scene_three_shots` — escena 9-10s → 3 shots
- `test_shot_durations_within_bounds` — cada shot entre 4-8s
- `test_characters_inherited_from_scene` — personajes se heredan correctamente
- `test_different_moods_produce_different_shot_types` — mood tensión → close-ups

#### `tests/test_flow_prompt_builder.py` (EXTENDER)
- `test_build_storyboard_prompts_structure` — verificar formato híbrido
- `test_storyboard_prompt_contains_global_context` — contexto global presente
- `test_each_shot_has_self_contained_prompt` — cada shot es autocontenido
- `test_storyboard_prompt_character_mapping` — mapping se aplica correctamente

### Archivos afectados

| Archivo | Acción |
|---------|--------|
| `app/agents/storyboard/__init__.py` | CREAR |
| `app/agents/storyboard/storyboard.py` | CREAR |
| `app/agents/flow_prompt_builder/flow_prompt_builder.py` | EXTENDER |
| `procesar_pagina.py` | MODIFICAR |
| `tests/test_storyboard.py` | CREAR |
| `tests/test_flow_prompt_builder.py` | EXTENDER |

### Lo que NO cambia

- `DirectorAgent` no requiere cambios (sigue orquestando, los storyboard prompts se generan después de los scene prompts)
- `MangaAnalyzerAgent` no cambia
- `SceneComposerAgent` no cambia
- Modelos de BD no cambian (los storyboard prompts se guardan como Assets con `asset_type="prompt"` y metadata indicando `type="storyboard"`)
- API endpoints no cambian
