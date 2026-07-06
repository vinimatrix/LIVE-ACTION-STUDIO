# Storyboard Agent & Hybrid Prompt Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a StoryboardAgent that breaks scenes into multiple shots, extend FlowPromptBuilderAgent to generate hybrid scene+storyboard prompts, and update procesar_pagina.py to output both.

**Architecture:** New `app/agents/storyboard/` package with StoryboardAgent that decomposes scenes into 4-8s shots based on mood/dialogue/action patterns. FlowPromptBuilderAgent gains `build_storyboard_prompts()` that outputs hybrid format (global context + per-shot prompts). `procesar_pagina.py` runs both generators sequentially.

**Tech Stack:** Python 3.14, pytest with mocker

## Global Constraints

- All scene data structures match existing `SceneComposerAgent` output
- StoryboardAgent does NOT call Ollama — pure deterministic logic based on scene data
- Each shot duration between 4-8 seconds (inclusive)
- Shot types: wide, medium, close-up, extreme-close-up, over-the-shoulder, extreme-wide
- Camera movements: static, dolly, pan, tilt, crane, tracking, steadicam, handheld
- Tests follow existing patterns (pytest with classes, no external dependencies)

---

### Task 1: Create StoryboardAgent

**Files:**
- Create: `app/agents/storyboard/__init__.py`
- Create: `app/agents/storyboard/storyboard.py`
- Create: `tests/test_storyboard.py`

**Interfaces:**
- Consumes: scene dict from SceneComposerAgent (`{"scene_id": int, "duration": float, "characters": list, "description": str, "camera": dict, "lighting": dict, "dialogue": list, "transition": str}`)
- Produces: `StoryboardAgent.break_down_scene(scene) -> List[Dict]` — each shot: `{"shot_number": int, "start_time": float, "end_time": float, "shot_type": str, "movement": str, "lens": str, "description": str, "characters_in_frame": list, "focus": str, "transition_in": str, "transition_out": str}`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_storyboard.py
import pytest
from app.agents.storyboard.storyboard import StoryboardAgent

class TestStoryboardAgent:
    SAMPLE_SCENE_SHORT = {
        "scene_id": 1,
        "duration": 4.0,
        "characters": [
            {"name": "Goku", "appearance": "orange gi", "expression": "angry", "position": "center"}
        ],
        "description": "Goku powering up",
        "camera": {"shot_type": "medium", "movement": "dolly", "lens": "35mm f/2.8"},
        "lighting": {"time_of_day": "sunset", "mood_lighting": "epic"},
        "dialogue": [{"character": "Goku", "text": "AHHH!"}],
        "transition": "fade_in"
    }

    SAMPLE_SCENE_MEDIUM = {
        "scene_id": 2,
        "duration": 7.0,
        "characters": [
            {"name": "Goku", "appearance": "orange gi", "expression": "angry", "position": "left"},
            {"name": "Freezer", "appearance": "white armor", "expression": "smirking", "position": "right"}
        ],
        "description": "Goku confronts Freezer on the battlefield",
        "camera": {"shot_type": "wide", "movement": "static", "lens": "24mm f/4"},
        "lighting": {"time_of_day": "day", "mood_lighting": "tense"},
        "dialogue": [
            {"character": "Goku", "text": "Freezer!"},
            {"character": "Freezer", "text": "Foolish Saiyan."}
        ],
        "transition": "cut"
    }

    SAMPLE_SCENE_LONG = {
        "scene_id": 3,
        "duration": 10.0,
        "characters": [
            {"name": "Goku", "appearance": "orange gi", "expression": "determined", "position": "center"}
        ],
        "description": "Goku charges at Freezer with full speed",
        "camera": {"shot_type": "wide", "movement": "tracking", "lens": "35mm f/2.8"},
        "lighting": {"time_of_day": "day", "mood_lighting": "intense"},
        "dialogue": [],
        "transition": "cut"
    }

    SAMPLE_TENSE_SCENE = {
        "scene_id": 4,
        "duration": 8.0,
        "characters": [
            {"name": "Freezer", "appearance": "white armor", "expression": "smirking", "position": "center"}
        ],
        "description": "Freezer slowly approaches the wounded Goku",
        "camera": {"shot_type": "wide", "movement": "static", "lens": "35mm f/2.8"},
        "lighting": {"time_of_day": "night", "mood_lighting": "tense"},
        "dialogue": [{"character": "Freezer", "text": "Any last words?"}],
        "transition": "cut"
    }

    def test_short_scene_returns_single_shot(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_SCENE_SHORT)
        assert len(shots) == 1

    def test_medium_scene_returns_two_shots(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_SCENE_MEDIUM)
        assert len(shots) == 2

    def test_long_scene_returns_three_shots(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_SCENE_LONG)
        assert len(shots) == 3

    def test_each_shot_duration_between_4_and_8_seconds(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_SCENE_MEDIUM)
        for shot in shots:
            duration = shot["end_time"] - shot["start_time"]
            assert 4.0 <= duration <= 8.0

    def test_shot_times_are_continuous(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_SCENE_MEDIUM)
        assert shots[0]["start_time"] == 0.0
        for i in range(1, len(shots)):
            assert shots[i]["start_time"] == shots[i-1]["end_time"]
        assert shots[-1]["end_time"] == self.SAMPLE_SCENE_MEDIUM["duration"]

    def test_characters_inherited_from_scene(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_SCENE_MEDIUM)
        for shot in shots:
            assert len(shot["characters_in_frame"]) > 0

    def test_each_shot_has_required_fields(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_SCENE_MEDIUM)
        required = ["shot_number", "start_time", "end_time", "shot_type",
                     "movement", "lens", "description", "characters_in_frame",
                     "focus", "transition_in", "transition_out"]
        for shot in shots:
            for field in required:
                assert field in shot, f"Missing field: {field}"

    def test_tense_scene_prefers_close_ups(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_TENSE_SCENE)
        shot_types = [s["shot_type"] for s in shots]
        assert any(t in ("close-up", "extreme-close-up") for t in shot_types)

    def test_dialogue_scene_includes_over_shoulder(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_SCENE_MEDIUM)
        shot_types = [s["shot_type"] for s in shots]
        assert "over-the-shoulder" in shot_types
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_storyboard.py -v`

Expected: All tests FAIL with `ModuleNotFoundError: No module named 'app.agents.storyboard'`

- [ ] **Step 3: Create `app/agents/storyboard/__init__.py`**

```python
from .storyboard import StoryboardAgent

__all__ = ["StoryboardAgent"]
```

- [ ] **Step 4: Write the StoryboardAgent implementation**

```python
# app/agents/storyboard/storyboard.py
from typing import Dict, Any, List


class StoryboardAgent:
    MAX_SHOT_DURATION = 8.0
    MIN_SHOT_DURATION = 4.0

    # Shot type patterns by mood
    MOOD_SHOT_PATTERNS = {
        "tense": ["close-up", "extreme-close-up", "close-up"],
        "intense": ["wide", "medium", "close-up"],
        "epic": ["extreme-wide", "wide", "close-up"],
        "sad": ["wide", "close-up", "extreme-close-up"],
        "peaceful": ["extreme-wide", "wide", "medium"],
    }

    # Default patterns by scenario
    PATTERN_DIALOGUE_1 = ["medium", "close-up"]
    PATTERN_DIALOGUE_2 = ["wide", "over-the-shoulder", "over-the-shoulder", "close-up"]
    PATTERN_ACTION = ["wide", "tracking", "close-up"]
    PATTERN_SILENT = ["wide", "slow_push-in", "extreme-close-up"]

    def break_down_scene(self, scene: Dict[str, Any]) -> List[Dict[str, Any]]:
        duration = scene.get("duration", 8.0)
        characters = scene.get("characters", [])
        dialogue = scene.get("dialogue", [])
        mood = scene.get("lighting", {}).get("mood_lighting", "neutral")
        camera = scene.get("camera", {})
        description = scene.get("description", "")

        if duration <= 5.0:
            return [self._build_single_shot(scene, 0, duration, camera, "fade_in" if scene.get("transition") == "fade_in" else "cut", "cut")]

        if len(dialogue) >= 2 and len(set(d["character"] for d in dialogue)) >= 2:
            return self._build_dialogue_two(scene)
        elif len(dialogue) == 1:
            return self._build_dialogue_one(scene)
        elif self._is_action_scene(mood):
            return self._build_action(scene)
        else:
            return self._build_silent_mood(scene, mood)

    def _build_single_shot(self, scene, start_time, end_time, camera, trans_in, trans_out):
        return {
            "shot_number": 1,
            "start_time": start_time,
            "end_time": end_time,
            "shot_type": camera.get("shot_type", "wide"),
            "movement": camera.get("movement", "static"),
            "lens": camera.get("lens", "35mm f/2.8"),
            "description": scene.get("description", ""),
            "characters_in_frame": [c["name"] for c in scene.get("characters", [])],
            "focus": scene.get("description", ""),
            "transition_in": trans_in,
            "transition_out": trans_out
        }

    def _build_dialogue_one(self, scene):
        duration = scene["duration"]
        mid = duration / 2
        return [
            self._build_shot(scene, 1, "medium", "static", "35mm f/2.8",
                0.0, mid, scene.get("description", ""),
                [c["name"] for c in scene.get("characters", [])],
                "Establecer personaje en entorno",
                scene.get("transition", "cut"), "cut"),
            self._build_shot(scene, 2, "close-up", "slow push-in", "50mm f/2.0",
                mid, duration, f"Close-up de {scene['characters'][0]['name']}: {scene['characters'][0].get('expression', 'neutral')}",
                [scene['characters'][0]['name']],
                f"Expresión facial de {scene['characters'][0]['name']}",
                "cut", "cut")
        ]

    def _build_dialogue_two(self, scene):
        duration = scene["duration"]
        characters = scene.get("characters", [])
        char_names = [c["name"] for c in characters]
        n_shots = 4
        shot_duration = duration / n_shots
        shots = []

        # Shot 1: Wide establishing both
        shots.append(self._build_shot(scene, 1, "wide", "static", "24mm f/4",
            0.0, shot_duration, f"Ambos personajes en cuadro: {', '.join(char_names)}",
            char_names, "Relación espacial entre personajes",
            scene.get("transition", "cut"), "cut"))

        # Shot 2: Over-shoulder character A
        shots.append(self._build_shot(scene, 2, "over-the-shoulder", "static", "35mm f/2.8",
            shot_duration, shot_duration * 2, f"Sobre el hombro de {char_names[0]}: {char_names[1]} reacciona",
            [char_names[0], char_names[1]], f"Reacción de {char_names[1]}",
            "cut", "cut"))

        # Shot 3: Over-shoulder character B
        shots.append(self._build_shot(scene, 3, "over-the-shoulder", "static", "35mm f/2.8",
            shot_duration * 2, shot_duration * 3, f"Sobre el hombro de {char_names[1]}: {char_names[0]} responde",
            [char_names[0], char_names[1]], f"Respuesta de {char_names[0]}",
            "cut", "cut"))

        # Shot 4: Close-up clímax
        shots.append(self._build_shot(scene, 4, "close-up", "slow push-in", "50mm f/2.0",
            shot_duration * 3, duration, f"Clímax: {char_names[0]} confronta a {char_names[1]}",
            [char_names[0]], f"Momento culminante del diálogo",
            "cut", "cut"))

        return shots

    def _build_action(self, scene):
        duration = scene["duration"]
        characters = scene.get("characters", [])
        n_shots = 3
        shot_duration = duration / n_shots
        return [
            self._build_shot(scene, 1, "wide", "tracking", "24mm f/4",
                0.0, shot_duration, scene.get("description", ""),
                [c["name"] for c in characters], "Contexto de la acción",
                scene.get("transition", "cut"), "cut"),
            self._build_shot(scene, 2, "medium", "tracking", "35mm f/2.8",
                shot_duration, shot_duration * 2, f"Movimiento de {characters[0]['name'] if characters else 'personaje'} en acción",
                [c["name"] for c in characters], "Seguimiento del movimiento",
                "cut", "cut"),
            self._build_shot(scene, 3, "close-up", "static", "50mm f/2.0",
                shot_duration * 2, duration, "Impacto o efecto de la acción",
                [c["name"] for c in characters], "Momento de impacto",
                "cut", "cut")
        ]

    def _build_silent_mood(self, scene, mood):
        duration = scene["duration"]
        characters = scene.get("characters", [])
        pattern = self.MOOD_SHOT_PATTERNS.get(mood, self.PATTERN_SILENT)
        n_shots = min(len(pattern), max(2, int(duration / 5)))
        shot_duration = duration / n_shots
        shots = []
        for i in range(n_shots):
            shot_type = pattern[i] if i < len(pattern) else "medium"
            movement = "static" if shot_type in ("close-up", "extreme-close-up") else "slow dolly"
            if i == n_shots - 1:
                lens = "85mm f/1.4" if shot_type == "extreme-close-up" else "50mm f/2.0"
            else:
                lens = "24mm f/4" if shot_type in ("wide", "extreme-wide") else "35mm f/2.8"
            shots.append(self._build_shot(scene, i + 1, shot_type, movement, lens,
                i * shot_duration, (i + 1) * shot_duration,
                f"{shot_type.replace('_', ' ').title()} — construyendo atmósfera ({mood})",
                [c["name"] for c in characters] if i == 0 else [],
                f"Enfoque en {shot_type}: atmósfera {mood}",
                "cut" if i > 0 else scene.get("transition", "cut"), "cut"))
        return shots

    def _build_shot(self, scene, shot_number, shot_type, movement, lens,
                    start_time, end_time, description, characters_in_frame,
                    focus, transition_in, transition_out):
        return {
            "shot_number": shot_number,
            "start_time": start_time,
            "end_time": end_time,
            "shot_type": shot_type,
            "movement": movement,
            "lens": lens,
            "description": description,
            "characters_in_frame": characters_in_frame,
            "focus": focus,
            "transition_in": transition_in,
            "transition_out": transition_out
        }

    def _is_action_scene(self, mood: str) -> bool:
        return mood in ("intense", "epic", "dramatic", "explosive")
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_storyboard.py -v`

Expected: All tests PASS

- [ ] **Step 6: Commit**

```bash
git add app/agents/storyboard/ tests/test_storyboard.py
git commit -m "feat: add StoryboardAgent for shot-by-shot scene breakdown"
```

---

### Task 2: Extend FlowPromptBuilderAgent with storyboard prompts

**Files:**
- Modify: `app/agents/flow_prompt_builder/flow_prompt_builder.py`
- Modify: `tests/test_flow_prompt_builder.py`

**Interfaces:**
- Consumes: `StoryboardAgent.break_down_scene(scene) -> List[Dict]`
- Produces: `FlowPromptBuilderAgent.build_storyboard_prompts(scenes, character_mapping, storyboard_agent) -> List[Dict]` — each with `{"scene_id": int, "scene_number": int, "prompt_text": str}` in hybrid format

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_flow_prompt_builder.py`:

```python
from app.agents.storyboard.storyboard import StoryboardAgent

class TestFlowPromptBuilderStoryboard:
    SAMPLE_SCENES = [
        {
            "scene_id": 1,
            "duration": 7.0,
            "characters": [
                {"name": "Goku", "appearance": "orange gi, spiky black hair",
                 "expression": "angry", "position": "left"},
                {"name": "Freezer", "appearance": "white armor",
                 "expression": "smirking", "position": "right"}
            ],
            "description": "Goku confronts Freezer on the battlefield",
            "camera": {"shot_type": "wide", "movement": "static", "lens": "24mm f/4"},
            "lighting": {"time_of_day": "day", "mood_lighting": "tense"},
            "dialogue": [
                {"character": "Goku", "text": "Freezer!"},
                {"character": "Freezer", "text": "Foolish Saiyan."}
            ],
            "transition": "cut"
        }
    ]
    CHARACTER_MAPPING = {"Goku": "personaje_1", "Freezer": "personaje_2"}

    def test_build_storyboard_prompts_returns_list(self):
        agent = FlowPromptBuilderAgent()
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent
        )
        assert isinstance(prompts, list)
        assert len(prompts) == 1

    def test_storyboard_prompt_contains_global_context(self):
        agent = FlowPromptBuilderAgent()
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent
        )
        prompt_text = prompts[0]["prompt_text"]
        assert "ESCENA 1" in prompt_text
        assert "Contexto Global" in prompt_text
        assert "SHOT 1" in prompt_text

    def test_storyboard_prompt_contains_per_shot_sections(self):
        agent = FlowPromptBuilderAgent()
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent
        )
        prompt_text = prompts[0]["prompt_text"]
        # Each shot should have its own camera, action, and anti-alucinación
        for shot_num in (1, 2):
            assert f"SHOT {shot_num}" in prompt_text
            assert "TIPO:" in prompt_text
            assert "MOV:" in prompt_text

    def test_storyboard_prompt_has_character_mapping(self):
        agent = FlowPromptBuilderAgent()
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent
        )
        prompt_text = prompts[0]["prompt_text"]
        assert "personaje_1" in prompt_text
        assert "personaje_2" in prompt_text

    def test_storyboard_prompt_includes_anti_alucinacion(self):
        agent = FlowPromptBuilderAgent()
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent
        )
        prompt_text = prompts[0]["prompt_text"]
        assert "ANTI-ALUCINACIÓN" in prompt_text
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_flow_prompt_builder.py::TestFlowPromptBuilderStoryboard -v`

Expected: FAIL with `AttributeError: 'FlowPromptBuilderAgent' object has no attribute 'build_storyboard_prompts'`

- [ ] **Step 3: Extend FlowPromptBuilderAgent**

Update `app/agents/flow_prompt_builder/flow_prompt_builder.py` — add import and new method:

```python
from typing import Dict, Any, List
from app.agents.storyboard.storyboard import StoryboardAgent

# (existing class FlowPromptBuilderAgent, keep existing methods)

    def build_storyboard_prompts(
        self,
        scenes: List[Dict[str, Any]],
        character_mapping: Dict[str, str],
        storyboard_agent: StoryboardAgent = None
    ) -> List[Dict[str, Any]]:
        if storyboard_agent is None:
            storyboard_agent = StoryboardAgent()

        prompts = []
        start_time = 0.0
        for i, scene in enumerate(scenes):
            duration = scene.get("duration", 8.0)
            shots = storyboard_agent.break_down_scene(scene)
            prompt_text = self._build_hybrid_prompt(scene, shots, character_mapping, i + 1, start_time)
            prompts.append({
                "scene_id": scene["scene_id"],
                "scene_number": i + 1,
                "duration": duration,
                "prompt_text": prompt_text
            })
            start_time += duration
        return prompts

    def _build_hybrid_prompt(
        self,
        scene: Dict[str, Any],
        shots: List[Dict[str, Any]],
        character_mapping: Dict[str, str],
        scene_num: int,
        start_time: float
    ) -> str:
        duration = scene.get("duration", 8.0)
        end_time = start_time + duration
        lines = []

        # ── GLOBAL CONTEXT BLOCK ──
        lines.append(f"ESCENA {scene_num} — Contexto Global ({self._fmt_time(start_time)} - {self._fmt_time(end_time)})")
        lines.append("─" * 70)
        lines.append("")
        lines.append("PERSONAJES:")
        for c in scene.get("characters", []):
            name = c.get("name", "Unknown")
            flow_ref = character_mapping.get(name, name)
            expression = c.get("expression", "neutral")
            lines.append(f"  - {name} (Flow ref: {flow_ref}): {expression}")
        lines.append("")
        lines.append("ESCENARIO:")
        lighting = scene.get("lighting", {})
        lines.append(f"  - Descripción: {scene.get('description', '')}")
        lines.append(f"  - Hora: {lighting.get('time_of_day', 'day')}")
        lines.append(f"  - Mood: {lighting.get('mood_lighting', 'neutral')}")
        lines.append("")
        lines.append("SPECS TÉCNICAS:")
        lines.append("  - Resolución: 8K (7680x4320)")
        lines.append("  - Estilo: live-action hiperrealista, cinematográfico, fotorrealista")
        lines.append("  - Texturas: extremadamente detalladas, poros de la piel realistas, texturas PBR")
        lines.append("  - Iluminación: volumetric lighting, cinematic lighting, global illumination")
        lines.append("  - Post-procesado: color grading cinematográfico, grain sutil de película analógica, sin CGI, sin renderizado 3D")
        lines.append("  - Motion blur: obturador 180°, movimiento realista natural")
        lines.append("")
        lines.append("ANTI-ALUCINACIÓN (global):")
        for c in scene.get("characters", []):
            name = c.get("name", "")
            flow_ref = character_mapping.get(name, name)
            lines.append(f"  - Mantener consistencia total de {name} (ref: {flow_ref}) exactamente como en la referencia de Flow")
        lines.append("  - No alucinar ni añadir objetos, personajes o elementos no descritos")
        lines.append("  - Fondo coherente con la descripción del escenario en todos los shots")
        lines.append("  - Respetar iluminación y hora del día especificadas")
        lines.append("")

        # ── STORYBOARD SHOTS ──
        lines.append("STORYBOARD:")
        lines.append("")
        for shot in shots:
            shot_start = self._fmt_time(shot["start_time"])
            shot_end = self._fmt_time(shot["end_time"])
            shot_type = shot["shot_type"].replace("_", " ").title()
            movement = shot["movement"].replace("_", " ").title()
            lines.append(f"╔══ SHOT {shot['shot_number']} ({shot_start} → {shot_end}) ═══════════════════════════════════════")
            lines.append(f"║  TIPO: {shot_type}")
            lines.append(f"║  MOV: {movement}")
            lines.append(f"║  LENTE: {shot['lens']}")
            lines.append(f"║  TRANSICIÓN IN: {shot['transition_in'].replace('_', ' ').title()}")
            lines.append(f"║  TRANSICIÓN OUT: {shot['transition_out'].replace('_', ' ').title()}")
            lines.append("║")
            lines.append(f"║  PERSONAJES EN CUADRO:")
            for char_name in shot["characters_in_frame"]:
                flow_ref = character_mapping.get(char_name, char_name)
                lines.append(f"║    - {char_name} (ref: {flow_ref})")
            lines.append("║")
            lines.append(f"║  ACCIÓN: {shot['description']}")
            lines.append(f"║  FOCO: {shot['focus']}")
            lines.append("║")
            lines.append("║  ANTI-ALUCINACIÓN (shot específico):")
            lines.append(f"║    - Mantener exactamente este encuadre: {shot_type}, {movement}")
            if shot["characters_in_frame"]:
                lines.append(f"║    - Solo {', '.join(shot['characters_in_frame'])} visible(s) en este shot")
                for char_name in shot["characters_in_frame"]:
                    expr = next((c.get("expression", "neutral") for c in scene.get("characters", [])
                                 if c["name"] == char_name), "neutral")
                    lines.append(f"║    - No cambiar expresión de {char_name}: {expr}")
            lines.append(f"╚══ FIN SHOT {shot['shot_number']} {'═' * 50}")
            lines.append("")

        return "\n".join(lines)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_flow_prompt_builder.py -v`

Expected: All tests PASS (both existing + new storyboard tests)

- [ ] **Step 5: Commit**

```bash
git add app/agents/flow_prompt_builder/flow_prompt_builder.py tests/test_flow_prompt_builder.py
git commit -m "feat: add build_storyboard_prompts to FlowPromptBuilderAgent"
```

---

### Task 3: Update procesar_pagina.py

**Files:**
- Modify: `procesar_pagina.py`

- [ ] **Step 1: Update the script**

Modify `procesar_pagina.py`:

Add import after line 14 (`from app.agents.director.director import DirectorAgent`):
```python
from app.agents.storyboard.storyboard import StoryboardAgent
from app.agents.flow_prompt_builder.flow_prompt_builder import FlowPromptBuilderAgent
```

Replace the `print()` section after `job_id = director.process_manga_request(manga_request)` (lines 97-136) with expanded logic:

```python
    job_id = director.process_manga_request(manga_request)

    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        print(f"\n¡PROCESAMIENTO COMPLETADO EXITOSAMENTE!")
        print(f"Job ID: {job.id}")

        # ── 1. RECUPERAR SCENE PROMPTS ──
        assets = db.query(Asset).filter(Asset.job_id == job_id, Asset.asset_type == "prompt").all()
        if not assets:
            print("No se generaron prompts. Revisa los logs de Ollama o del agente.")
            return

        assets = sorted(assets, key=lambda a: a.generation_metadata.get("scene_number", 0))
        all_scene_prompts = []
        for asset in assets:
            prompt_text = asset.generation_metadata.get("prompt", "")
            all_scene_prompts.append(prompt_text)
            all_scene_prompts.append("\n" + "=" * 80 + "\n")

        # ── 2. GENERAR STORYBOARD PROMPTS ──
        print("\n=== GENERANDO PROMPTS DE STORYBOARD ===")
        scenes_data = []
        scenes_db = db.query(Scene).filter(Scene.job_id == job_id).all()
        for sc in scenes_db:
            sc_meta = next((a.generation_metadata for a in assets if a.scene_id == sc.id), {})
            scenes_data.append({
                "scene_id": sc.id,
                "duration": sc.duration,
                "characters": sc_meta.get("characters", []),
                "description": sc.description,
                "camera": sc_meta.get("camera", {}),
                "lighting": sc_meta.get("lighting", {}),
                "dialogue": sc_meta.get("dialogue", []),
                "transition": "cut"
            })

        # Reuse character_mapping already parsed above (from --char_map arg)
        storyboard_agent = StoryboardAgent()
        prompt_builder = FlowPromptBuilderAgent()
        storyboard_prompts = prompt_builder.build_storyboard_prompts(
            scenes_data, character_mapping, storyboard_agent
        )

        all_storyboard_prompts = []
        for sp in storyboard_prompts:
            all_storyboard_prompts.append(sp["prompt_text"])
            all_storyboard_prompts.append("\n" + "=" * 80 + "\n")

        # ── 3. GUARDAR ARCHIVO DE SALIDA ──
        output_dir = os.path.dirname(args.output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        output_lines = []
        output_lines.append("=== PROMPTS DE ESCENA ===")
        output_lines.append("")
        output_lines.extend(all_scene_prompts)
        output_lines.append("")
        output_lines.append("=" * 80)
        output_lines.append("")
        output_lines.append("=== PROMPTS DE STORYBOARD ===")
        output_lines.append("")
        output_lines.extend(all_storyboard_prompts)

        with open(args.output, "w", encoding="utf-8") as out_file:
            out_file.write("\n".join(output_lines))

        print(f"\n=== RESULTADOS ===")
        print(f"Prompts de escena generados: {len(assets)}")
        print(f"Prompts de storyboard generados: {len(storyboard_prompts)}")
        print(f"\nArchivo guardado en: {args.output}")
        print(f"\n--- PRIMER PROMPT DE STORYBOARD ---")
        if all_storyboard_prompts:
            print(all_storyboard_prompts[0])

    finally:
        db.close()
```

- [ ] **Step 2: Verify the script loads without errors**

Run: `python -c "import sys; sys.path.insert(0, '.'); from procesar_pagina import main; print('Import OK')"`

Expected: `Import OK`

- [ ] **Step 3: Run all tests to verify nothing is broken**

Run: `python -m pytest tests/ -v`

Expected: All tests PASS

- [ ] **Step 4: Commit**

```bash
git add procesar_pagina.py
git commit -m "feat: add storyboard prompt generation to procesar_pagina.py"
```

---

### Task 4: Final verification and integration test

**Files:** (none — verification only)

- [ ] **Step 1: Run full test suite**

Run: `python -m pytest tests/ -v`

Expected output: All tests PASS, including:
  - `test_storyboard.py` — 9 tests
  - `test_flow_prompt_builder.py` — 4 existing + 5 new = 9 tests
  - All other existing tests

- [ ] **Step 2: Verify the procesar_pagina.py script runs end-to-end with --help**

Run: `python procesar_pagina.py --help`

Expected: Shows usage with all arguments

- [ ] **Step 3: Final commit with all changes**

```bash
git add -A
git status
git commit -m "feat: complete storyboard agent and hybrid prompt pipeline"
```
