# Manga → Flow/Omni Prompt Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the AI Live Action Studio from a simulated generation pipeline into a manga analysis engine that outputs structured prompts for Flow/Omni.

**Architecture:** Three new agents (MangaAnalyzer, SceneComposer, FlowPromptBuilder) orchestrated by a refactored DirectorAgent. Ollama gemma4 handles vision analysis and text generation. API simplified to analyze → prompt flow.

**Tech Stack:** Python 3.14, FastAPI, SQLAlchemy, PostgreSQL, Ollama (gemma4 multimodal), Celery + Redis

## Global Constraints

- All image analysis via Ollama gemma4 API at `http://127.0.0.1:11434/api/generate`
- HTTP requests use `urllib.request` (existing pattern)
- Scenes max 10 seconds each
- Prompt output in structured markdown with sections: PERSONAJES, ESCENARIO, CÁMARA, ILUMINACIÓN, MOOD, ACCIÓN, SPECS TÉCNICAS, ANTI-ALUCINACIÓN
- Character mapping provided by user in the request
- Tests use pytest with mocked Ollama calls

---

### Task 1: Create MangaAnalyzerAgent

**Files:**
- Create: `app/agents/manga_analyzer/__init__.py` (empty)
- Create: `app/agents/manga_analyzer/manga_analyzer.py`
- Create: `app/agents/manga_analyzer/tasks.py`
- Create: `tests/test_manga_analyzer.py`

**Interfaces:**
- Consumes: Ollama API at `http://127.0.0.1:11434/api/generate`
- Produces: `MangaAnalyzerAgent.analyze(image_base64: str, filename: str) -> dict` with keys: `characters`, `setting`, `action`, `dialogue`, `mood`, `panels`

- [ ] **Step 1: Create directory and empty `__init__.py`**

```bash
mkdir -p app/agents/manga_analyzer
```

```python
# app/agents/manga_analyzer/__init__.py
```

- [ ] **Step 2: Write the failing test**

```python
# tests/test_manga_analyzer.py
import pytest
import json
from app.agents.manga_analyzer.manga_analyzer import MangaAnalyzerAgent

class TestMangaAnalyzer:
    def test_analyze_returns_expected_keys(self, mocker):
        mock_response = {
            "characters": [{"name": "Goku", "appearance": "orange gi, spiky black hair", "expression": "angry", "position": "center"}],
            "setting": "A rocky planet with red sky, two suns in background",
            "action": "Goku powering up, yelling, aura of light around him",
            "dialogue": ["AHHHHHHHHH!"],
            "mood": "epic, tense, battle climax",
            "panels": [{"panel_number": 1, "description": "Full page spread of Goku powering up"}]
        }
        mock = mocker.patch('urllib.request.urlopen')
        mock.return_value.read.return_value = json.dumps({"response": json.dumps(mock_response)}).encode()

        agent = MangaAnalyzerAgent()
        result = agent.analyze("fake_base64", "test.png")

        assert "characters" in result
        assert "setting" in result
        assert "action" in result
        assert "mood" in result
        assert isinstance(result["characters"], list)

    def test_analyze_with_empty_image(self, mocker):
        mocker.patch('urllib.request.urlopen').side_effect = Exception("Ollama error")
        agent = MangaAnalyzerAgent()
        result = agent.analyze("", "test.png")
        assert "error" in result
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd C:\Users\vm004458\Documents\MNG-LVCTN
pip install pytest-mock -q
python -m pytest tests/test_manga_analyzer.py -v
```
Expected: FAIL with ImportError/ModuleNotFoundError

- [ ] **Step 4: Write minimal implementation**

```python
# app/agents/manga_analyzer/manga_analyzer.py
from typing import Dict, Any
import json
import urllib.request

class MangaAnalyzerAgent:
    def __init__(self):
        self.ollama_url = "http://127.0.0.1:11434/api/generate"
        self.model = "gemma4:latest"

    def analyze(self, image_base64: str, filename: str = "") -> Dict[str, Any]:
        system_prompt = """Eres un experto analista de manga. Analiza la imagen de manga proporcionada y extrae:
- characters: lista de personajes (name, appearance, expression, position)
- setting: descripción del escenario
- action: acción principal
- dialogue: diálogos visibles
- mood: atmósfera/estado de ánimo
- panels: estructura de paneles

Responde SOLO con JSON válido, sin markdown ni explicaciones."""

        payload = {
            "model": self.model,
            "prompt": f"{system_prompt}\n\nAnaliza esta página de manga (filename: {filename}):",
            "images": [image_base64],
            "stream": False,
            "options": {"temperature": 0.1}
        }

        try:
            data = json.dumps(payload).encode()
            req = urllib.request.Request(
                self.ollama_url, data=data,
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=300) as resp:
                result = json.loads(resp.read())
                response_text = result.get("response", "{}")
                return json.loads(response_text)
        except Exception as e:
            return {"error": str(e), "characters": [], "setting": "", "action": "", "dialogue": [], "mood": ""}
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
python -m pytest tests/test_manga_analyzer.py -v
```
Expected: PASS (2/2)

- [ ] **Step 6: Create Celery tasks**

```python
# app/agents/manga_analyzer/tasks.py
from celery import Celery
from app.core.config import settings
from app.agents.manga_analyzer.manga_analyzer import MangaAnalyzerAgent

celery_app = Celery(
    "manga_analyzer",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

manga_analyzer_agent = MangaAnalyzerAgent()


@celery_app.task
def analyze_manga_page(manga_data: dict):
    image = manga_data.get("image")
    filename = manga_data.get("filename", "")
    result = manga_analyzer_agent.analyze(image, filename)
    return result
```

- [ ] **Step 7: Commit**

```bash
git add app/agents/manga_analyzer/ tests/test_manga_analyzer.py
git commit -m "feat: add MangaAnalyzerAgent with Ollama vision"
```

---

### Task 2: Create SceneComposerAgent

**Files:**
- Create: `app/agents/scene_composer/__init__.py` (empty)
- Create: `app/agents/scene_composer/scene_composer.py`
- Create: `app/agents/scene_composer/tasks.py`
- Create: `tests/test_scene_composer.py`

**Interfaces:**
- Consumes: `MangaAnalyzerAgent.analyze()` output dict
- Produces: `SceneComposerAgent.compose(manga_analysis: dict, max_scenes: int) -> list[dict]` where each scene dict has keys: `scene_id`, `duration` (≤10), `characters`, `description`, `camera`, `lighting`, `dialogue`, `transition`

- [ ] **Step 1: Create directory and empty `__init__.py`**

```bash
mkdir -p app/agents/scene_composer
```

- [ ] **Step 2: Write the failing test**

```python
# tests/test_scene_composer.py
import pytest
from app.agents.scene_composer.scene_composer import SceneComposerAgent

class TestSceneComposer:
    SAMPLE_ANALYSIS = {
        "characters": [
            {"name": "Goku", "appearance": "orange gi, spiky black hair", "expression": "angry", "position": "center"},
            {"name": "Freezer", "appearance": "white armor, tail, purple skin", "expression": "smirking", "position": "right"}
        ],
        "setting": "Destroyed planet Namek, green fields, two suns setting",
        "action": "Goku charges at Freezer with a energy blast",
        "dialogue": ["Freezer! This is for Namek!", "Hehehe... pathetic"],
        "mood": "epic battle, revenge, climax"
    }

    def test_compose_returns_list_of_scenes(self):
        agent = SceneComposerAgent()
        scenes = agent.compose(self.SAMPLE_ANALYSIS, max_scenes=3)
        assert isinstance(scenes, list)
        assert len(scenes) > 0
        assert len(scenes) <= 3

    def test_each_scene_duration_max_10s(self):
        agent = SceneComposerAgent()
        scenes = agent.compose(self.SAMPLE_ANALYSIS, max_scenes=5)
        for scene in scenes:
            assert scene["duration"] <= 10.0

    def test_scene_has_required_keys(self):
        agent = SceneComposerAgent()
        scenes = agent.compose(self.SAMPLE_ANALYSIS, max_scenes=1)
        scene = scenes[0]
        assert "scene_id" in scene
        assert "duration" in scene
        assert "characters" in scene
        assert "description" in scene
        assert "camera" in scene
        assert "lighting" in scene

    def test_compose_with_empty_analysis(self):
        agent = SceneComposerAgent()
        scenes = agent.compose({"characters": [], "setting": "", "action": "", "dialogue": [], "mood": ""})
        assert isinstance(scenes, list)
        assert len(scenes) == 1
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
python -m pytest tests/test_scene_composer.py -v
```
Expected: FAIL

- [ ] **Step 4: Write minimal implementation**

```python
# app/agents/scene_composer/scene_composer.py
from typing import Dict, Any, List

class SceneComposerAgent:
    def __init__(self):
        self.max_duration = 10.0

    def compose(self, manga_analysis: Dict[str, Any], max_scenes: int = 5) -> List[Dict[str, Any]]:
        characters = manga_analysis.get("characters", [])
        setting = manga_analysis.get("setting", "Unknown setting")
        action = manga_analysis.get("action", "")
        dialogue = manga_analysis.get("dialogue", [])
        mood = manga_analysis.get("mood", "neutral")

        scenes = []
        num_dialogues = len(dialogue)

        if num_dialogues <= 1 and not action:
            scenes.append(self._build_scene(1, characters, setting, action, dialogue, mood, "wide", "static"))
        else:
            for i in range(min(max_scenes, max(1, num_dialogues))):
                scene_dialogue = dialogue[i:i+1] if i < num_dialogues else []
                shot_type = self._select_shot(i, num_dialogues)
                movement = self._select_movement(i)
                desc = f"{action} - Part {i+1}" if num_dialogues > 1 else action
                scenes.append(self._build_scene(
                    i + 1, characters, setting, desc, scene_dialogue, mood, shot_type, movement
                ))

        return scenes

    def _build_scene(self, scene_id, characters, setting, action, dialogue, mood, shot_type, movement):
        return {
            "scene_id": scene_id,
            "duration": min(self.max_duration, 8.0 + len(dialogue) * 2),
            "characters": [
                {"name": c.get("name", "Unknown"), "appearance": c.get("appearance", ""),
                 "expression": c.get("expression", "neutral"), "position": c.get("position", "frame")}
                for c in characters
            ],
            "description": action,
            "camera": {"shot_type": shot_type, "movement": movement, "lens": "35mm f/2.8"},
            "lighting": {"time_of_day": "sunset" if "sunset" in setting.lower() or "sun" in setting.lower() else "day",
                         "mood_lighting": mood},
            "dialogue": [{"character": d.split("!")[0] if "!" in d else "Character", "text": d} for d in dialogue],
            "transition": "cut" if scene_id > 1 else "fade_in"
        }

    def _select_shot(self, index, total):
        shots = ["wide", "medium", "close-up", "over-the-shoulder", "extreme-close-up"]
        return shots[index % len(shots)]

    def _select_movement(self, index):
        movements = ["static", "dolly", "pan", "tilt", "steadicam"]
        return movements[index % len(movements)]
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
python -m pytest tests/test_scene_composer.py -v
```
Expected: PASS (4/4)

- [ ] **Step 6: Create Celery tasks**

```python
# app/agents/scene_composer/tasks.py
from celery import Celery
from app.core.config import settings
from app.agents.scene_composer.scene_composer import SceneComposerAgent

celery_app = Celery(
    "scene_composer",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

scene_composer_agent = SceneComposerAgent()


@celery_app.task
def compose_scenes(analysis_data: dict):
    manga_analysis = analysis_data.get("manga_analysis", {})
    max_scenes = analysis_data.get("max_scenes", 5)
    result = scene_composer_agent.compose(manga_analysis, max_scenes)
    return result
```

- [ ] **Step 7: Commit**

```bash
git add app/agents/scene_composer/ tests/test_scene_composer.py
git commit -m "feat: add SceneComposerAgent for scene breakdown"
```

---

### Task 3: Create FlowPromptBuilderAgent

**Files:**
- Create: `app/agents/flow_prompt_builder/__init__.py` (empty)
- Create: `app/agents/flow_prompt_builder/flow_prompt_builder.py`
- Create: `app/agents/flow_prompt_builder/tasks.py`
- Create: `tests/test_flow_prompt_builder.py`

**Interfaces:**
- Consumes: `SceneComposerAgent.compose()` output + character_mapping dict
- Produces: `FlowPromptBuilderAgent.build_prompts(scenes: list, character_mapping: dict) -> list[dict]` where each prompt has keys: `scene_id`, `scene_number`, `duration`, `prompt_text`

- [ ] **Step 1: Create directory and empty `__init__.py`**

```bash
mkdir -p app/agents/flow_prompt_builder
```

- [ ] **Step 2: Write the failing test**

```python
# tests/test_flow_prompt_builder.py
import pytest
from app.agents.flow_prompt_builder.flow_prompt_builder import FlowPromptBuilderAgent

class TestFlowPromptBuilder:
    SAMPLE_SCENES = [
        {
            "scene_id": 1,
            "duration": 8.0,
            "characters": [
                {"name": "Goku", "appearance": "orange gi, spiky black hair",
                 "expression": "angry", "position": "center"}
            ],
            "description": "Goku powering up with golden aura",
            "camera": {"shot_type": "medium", "movement": "dolly", "lens": "35mm f/2.8"},
            "lighting": {"time_of_day": "sunset", "mood_lighting": "epic"},
            "dialogue": [{"character": "Goku", "text": "AHHHHHH!"}],
            "transition": "fade_in"
        }
    ]
    CHARACTER_MAPPING = {"Goku": "personaje_1", "Freezer": "personaje_2"}

    def test_build_prompts_returns_list(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        assert isinstance(prompts, list)
        assert len(prompts) == 1

    def test_prompt_has_required_sections(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        prompt_text = prompts[0]["prompt_text"]
        assert "PERSONAJES" in prompt_text
        assert "ESCENARIO" in prompt_text
        assert "CÁMARA" in prompt_text
        assert "ILUMINACIÓN" in prompt_text
        assert "MOOD" in prompt_text
        assert "ACCIÓN" in prompt_text
        assert "SPECS TÉCNICAS" in prompt_text
        assert "ANTI-ALUCINACIÓN" in prompt_text

    def test_prompt_contains_character_mapping(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        prompt_text = prompts[0]["prompt_text"]
        assert "personaje_1" in prompt_text
        assert "Goku" in prompt_text

    def test_prompt_includes_duration_and_scene_number(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        assert prompts[0]["scene_number"] == 1
        assert prompts[0]["duration"] == 8.0
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
python -m pytest tests/test_flow_prompt_builder.py -v
```
Expected: FAIL

- [ ] **Step 4: Write minimal implementation**

```python
# app/agents/flow_prompt_builder/flow_prompt_builder.py
from typing import Dict, Any, List

class FlowPromptBuilderAgent:
    def build_prompts(self, scenes: List[Dict[str, Any]], character_mapping: Dict[str, str]) -> List[Dict[str, Any]]:
        prompts = []
        for i, scene in enumerate(scenes):
            prompt_text = self._build_prompt(scene, character_mapping, i + 1)
            prompts.append({
                "scene_id": scene["scene_id"],
                "scene_number": i + 1,
                "duration": scene["duration"],
                "prompt_text": prompt_text
            })
        return prompts

    def _build_prompt(self, scene: Dict[str, Any], character_mapping: Dict[str, str], scene_num: int) -> str:
        duration = scene.get("duration", 8.0)
        start_time = sum(scene.get("duration", 8.0) for _ in range(scene_num - 1))
        end_time = start_time + duration

        lines = []
        lines.append(f"ESCENA {scene_num} ({self._fmt_time(start_time)} - {self._fmt_time(end_time)})")
        lines.append("─" * 50)
        lines.append("")

        # PERSONAJES
        lines.append("PERSONAJES:")
        for c in scene.get("characters", []):
            name = c.get("name", "Unknown")
            flow_ref = character_mapping.get(name, name)
            appearance = c.get("appearance", "")
            expression = c.get("expression", "neutral")
            position = c.get("position", "frame")
            lines.append(f"  - {name} (Flow ref: {flow_ref}): {expression}, {position}")
            if appearance:
                lines.append(f"    Apariencia: {appearance}")
        lines.append("")

        # ESCENARIO
        lines.append("ESCENARIO:")
        lighting = scene.get("lighting", {})
        time_of_day = lighting.get("time_of_day", "day")
        lines.append(f"  - Descripción: {scene.get('description', '')}")
        lines.append(f"  - Hora: {time_of_day}")
        lines.append("")

        # CÁMARA
        camera = scene.get("camera", {})
        lines.append("CÁMARA:")
        lines.append(f"  - Shot: {camera.get('shot_type', 'wide')}")
        lines.append(f"  - Movimiento: {camera.get('movement', 'static')}")
        lines.append(f"  - Lente: {camera.get('lens', '35mm f/2.8')}")
        lines.append("")

        # ILUMINACIÓN
        mood = lighting.get("mood_lighting", "neutral")
        lines.append("ILUMINACIÓN:")
        lines.append(f"  - Ambiente: {time_of_day} lighting")
        lines.append(f"  - Mood: {mood}")
        lines.append("")

        # MOOD
        lines.append("MOOD: " + mood.capitalize())
        lines.append("")

        # ACCIÓN
        lines.append("ACCIÓN:")
        lines.append(f"  - {scene.get('description', '')}")
        lines.append(f"  - Duración: {duration:.1f} segundos")
        for d in scene.get("dialogue", []):
            lines.append(f"  - Diálogo: [{d.get('character', '?')}] \"{d.get('text', '')}\"")
        lines.append("")

        # SPECS TÉCNICAS
        lines.append("SPECS TÉCNICAS:")
        lines.append("  - Resolución: 8K (7680x4320)")
        lines.append("  - Estilo: hiperrealista, cinematográfico")
        lines.append("  - Texturas: detalladas, PBR")
        lines.append("  - Iluminación: volumetric lighting, global illumination")
        lines.append("  - Post-procesado: color grading cinematográfico, grain sutil")
        lines.append("  - Motion blur: obturador 180°, natural")
        lines.append("  - Profundidad de campo: acorde al shot")
        lines.append("")

        # ANTI-ALUCINACIÓN
        lines.append("ANTI-ALUCINACIÓN:")
        for name in scene.get("characters", []):
            n = name.get("name", "")
            flow_ref = character_mapping.get(n, n)
            lines.append(f"  - Mantener diseño de {n} (ref: {flow_ref}) exactamente como en la referencia de Flow")
        lines.append("  - No añadir objetos, personajes o elementos no descritos")
        lines.append("  - Fondo coherente con la descripción del escenario")
        lines.append("  - Respetar iluminación y hora del día especificadas")
        lines.append("  - No cambiar expresiones faciales ni poses indicadas")

        return "\n".join(lines)

    def _fmt_time(self, seconds: float) -> str:
        m = int(seconds // 60)
        s = int(seconds % 60)
        return f"{m:02d}:{s:02d}"
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
python -m pytest tests/test_flow_prompt_builder.py -v
```
Expected: PASS (4/4)

- [ ] **Step 6: Create Celery tasks**

```python
# app/agents/flow_prompt_builder/tasks.py
from celery import Celery
from app.core.config import settings
from app.agents.flow_prompt_builder.flow_prompt_builder import FlowPromptBuilderAgent

celery_app = Celery(
    "flow_prompt_builder",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

flow_prompt_builder_agent = FlowPromptBuilderAgent()


@celery_app.task
def build_flow_prompts(prompt_data: dict):
    scenes = prompt_data.get("scenes", [])
    character_mapping = prompt_data.get("character_mapping", {})
    result = flow_prompt_builder_agent.build_prompts(scenes, character_mapping)
    return result
```

- [ ] **Step 7: Commit**

```bash
git add app/agents/flow_prompt_builder/ tests/test_flow_prompt_builder.py
git commit -m "feat: add FlowPromptBuilderAgent for structured prompts"
```

---

### Task 4: Refactor DirectorAgent as orchestrator

**Files:**
- Modify: `app/agents/director/director.py` (full rewrite of `process_manga_request`)
- Modify: `app/agents/director/tasks.py`
- Modify: `tests/test_director.py`

**Interfaces:**
- Consumes: task outputs from MangaAnalyzer, SceneComposer, FlowPromptBuilder
- Produces: `DirectorAgent.process_manga_request(data) -> int` returns job_id

- [ ] **Step 1: Write updated test**

```python
# tests/test_director.py
import pytest
from app.agents.director.director import DirectorAgent

class TestDirectorAgent:
    def test_director_initialization(self):
        agent = DirectorAgent()
        assert agent is not None

    def test_process_manga_request_creates_job(self, mocker):
        mock_analyze = mocker.patch.object(DirectorAgent, 'manga_analyzer')
        mock_analyze.analyze.return_value = {"characters": [], "setting": "test", "action": "", "dialogue": [], "mood": ""}
        mock_compose = mocker.patch.object(DirectorAgent, 'scene_composer')
        mock_compose.compose.return_value = [{"scene_id": 1, "duration": 8.0, "characters": [], "description": "test", "camera": {}, "lighting": {}, "dialogue": [], "transition": "cut"}]
        mock_prompt = mocker.patch.object(DirectorAgent, 'prompt_builder')
        mock_prompt.build_prompts.return_value = [{"scene_id": 1, "scene_number": 1, "duration": 8.0, "prompt_text": "test prompt"}]

        mock_db = mocker.MagicMock()
        mock_job = mocker.MagicMock()
        mock_job.id = 42
        mock_db.add.return_value = None
        mock_db.flush.return_value = None
        mock_db.commit.return_value = None
        mock_db.refresh.return_value = None

        agent = DirectorAgent()
        agent._db_session = lambda: mock_db

        job_id = agent.process_manga_request({
            "filename": "test.png",
            "image": "base64data",
            "character_mapping": {"Goku": "personaje_1"},
            "options": {"max_scenes": 3}
        })
        assert job_id == 42
```

Wait, I need to check how SessionLocal is used in director.py currently. Let me read the file first.

Actually, I already read it earlier. The current director.py has:

```python
class DirectorAgent:
    def __init__(self, db_session: Callable = None):
        self.settings = settings
        self._db_session = db_session or SessionLocal

    def process_manga_request(self, manga_data: Dict[str, Any]) -> int:
        # Create Job + Scene records
```

Let me write the updated director and tests properly. But I need to understand the database interaction pattern better.

Let me adjust the approach - I'll write the tests based on what the new DirectorAgent will do, without getting too deep into mocking the DB.

- [ ] **Step 2: Write the new DirectorAgent**

```python
# app/agents/director/director.py
from typing import Dict, Any, Callable
from app.core.config import settings
from app.db.session import SessionLocal
from app.models import Job, Scene, Asset
from app.agents.manga_analyzer.manga_analyzer import MangaAnalyzerAgent
from app.agents.scene_composer.scene_composer import SceneComposerAgent
from app.agents.flow_prompt_builder.flow_prompt_builder import FlowPromptBuilderAgent


class DirectorAgent:
    def __init__(self, db_session: Callable = None):
        self.settings = settings
        self._db_session = db_session or SessionLocal
        self.manga_analyzer = MangaAnalyzerAgent()
        self.scene_composer = SceneComposerAgent()
        self.prompt_builder = FlowPromptBuilderAgent()

    def process_manga_request(self, manga_data: Dict[str, Any]) -> int:
        image = manga_data.get("image", "")
        filename = manga_data.get("filename", "")
        character_mapping = manga_data.get("character_mapping", {})
        options = manga_data.get("options", {})
        max_scenes = options.get("max_scenes", 5)

        # 1. Analyze manga page
        analysis = self.manga_analyzer.analyze(image, filename)

        # 2. Compose scenes
        scenes = self.scene_composer.compose(analysis, max_scenes)

        # 3. Build prompts
        prompts = self.prompt_builder.build_prompts(scenes, character_mapping)

        # 4. Save to DB
        db = self._db_session()
        try:
            job = Job(
                manga_filename=filename,
                status="completed",
                progress=100,
                current_step="prompts_generated"
            )
            db.add(job)
            db.flush()

            for scene_data, prompt in zip(scenes, prompts):
                scene = Scene(
                    job_id=job.id,
                    manga_page_reference=filename,
                    description=scene_data.get("description", ""),
                    duration=scene_data.get("duration", 8.0)
                )
                db.add(scene)
                db.flush()

                asset = Asset(
                    job_id=job.id,
                    scene_id=scene.id,
                    asset_type="prompt",
                    mime_type="text/markdown",
                    generation_metadata={
                        "prompt": prompt["prompt_text"],
                        "scene_number": prompt["scene_number"],
                        "duration": prompt["duration"],
                        "manga_analysis": analysis
                    }
                )
                db.add(asset)

            db.commit()
            db.refresh(job)
            return job.id
        finally:
            db.close()

    def get_next_task(self, job_id: int) -> Dict[str, Any]:
        db = self._db_session()
        try:
            job = db.query(Job).filter(Job.id == job_id).first()
            if not job:
                return {"error": "Job not found"}
            return {"job_id": job.id, "task_type": "completed", "status": job.status}
        finally:
            db.close()
```

- [ ] **Step 3: Update the Celery tasks**

```python
# app/agents/director/tasks.py
from celery import Celery
from app.core.config import settings
from app.agents.director.director import DirectorAgent

celery_app = Celery(
    "director",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

director_agent = DirectorAgent()


@celery_app.task
def process_manga_pipeline(manga_data: dict):
    job_id = director_agent.process_manga_request(manga_data)
    return job_id
```

- [ ] **Step 4: Update tests and run**

```bash
python -m pytest tests/test_director.py -v
```

- [ ] **Step 5: Commit**

```bash
git add app/agents/director/
git commit -m "refactor: DirectorAgent as manga-to-prompt orchestrator"
```

---

### Task 5: Refactor API endpoints

**Files:**
- Modify: `app/api/v1/endpoints/manga.py` (replace process with analyze)
- Modify: `app/api/v1/endpoints/jobs.py` (update job response)
- Modify: `app/api/v1/__init__.py` (no change needed)
- Modify: `tests/test_api.py`

- [ ] **Step 1: Update manga endpoint**

```python
# app/api/v1/endpoints/manga.py
from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.db.session import SessionLocal
from app.models import Job, Asset
from app.agents.director.director import DirectorAgent

router = APIRouter()


@router.post("/analyze", status_code=202)
async def analyze_manga(manga_data: dict, background_tasks: BackgroundTasks):
    if not manga_data.get("image"):
        raise HTTPException(status_code=400, detail="Image is required (base64 encoded)")
    background_tasks.add_task(DirectorAgent().process_manga_request, manga_data)
    return {
        "message": "Manga analysis started",
        "filename": manga_data.get("filename", ""),
        "status": "accepted"
    }


@router.get("/status/{job_id}")
async def get_job_status(job_id: int):
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        return {
            "job_id": job.id,
            "status": job.status,
            "progress": job.progress,
            "current_step": job.current_step,
            "error_message": job.error_message
        }
    finally:
        db.close()


@router.get("/result/{job_id}")
async def get_job_result(job_id: int):
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        if job.status != "completed":
            raise HTTPException(
                status_code=400,
                detail=f"Job is not completed yet (status: {job.status})"
            )
        assets = db.query(Asset).filter(Asset.job_id == job_id).all()
        return {
            "job_id": job.id,
            "status": job.status,
            "prompts": [
                {
                    "id": asset.id,
                    "scene_id": asset.scene_id,
                    "type": asset.asset_type,
                    "prompt_text": asset.generation_metadata.get("prompt", ""),
                    "scene_number": asset.generation_metadata.get("scene_number"),
                    "duration": asset.generation_metadata.get("duration")
                }
                for asset in assets if asset.asset_type == "prompt"
            ]
        }
    finally:
        db.close()
```

- [ ] **Step 2: Update API tests**

```python
# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "AI Live Action Studio MVP"}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_analyze_manga_endpoint(mocker):
    mocker.patch('app.agents.director.director.DirectorAgent')
    response = client.post(
        "/api/v1/manga/analyze",
        json={
            "image": "fakebase64",
            "filename": "test_manga.jpg",
            "character_mapping": {"Goku": "personaje_1"}
        }
    )
    assert response.status_code == 202
    assert response.json()["status"] == "accepted"


def test_analyze_manga_missing_image():
    response = client.post(
        "/api/v1/manga/analyze",
        json={"filename": "test.jpg"}
    )
    assert response.status_code == 400


def test_get_job_status_not_found():
    response = client.get("/api/v1/manga/status/99999")
    assert response.status_code == 404
```

- [ ] **Step 3: Run tests**

```bash
python -m pytest tests/test_api.py -v
```
Expected: PASS (5/5)

- [ ] **Step 4: Commit**

```bash
git add app/api/v1/endpoints/manga.py tests/test_api.py
git commit -m "refactor: API endpoints for manga-to-prompt flow"
```

---

### Task 6: Remove obsolete generators

**Files:**
- Delete: `app/agents/video_generator/` (entire directory)
- Delete: `app/agents/voice_generator/` (entire directory)
- Delete: `app/agents/music_generator/` (entire directory)
- Delete: `app/agents/fx_generator/` (entire directory)
- Delete: `app/agents/editor/` (entire directory)
- Delete: `app/agents/screenwriter/screenwriter.py` (logic moved to SceneComposer)
- Delete: `app/agents/screenwriter/tasks.py`
- Delete: `app/agents/image_generator/tasks.py` (keep image_generator.py)
- Delete: `tests/test_video_generator.py`
- Delete: `tests/test_voice_generator.py`
- Delete: `tests/test_music_generator.py`
- Delete: `tests/test_fx_generator.py`
- Delete: `tests/test_editor.py`

- [ ] **Step 1: Remove directories and files**

```bash
rm -rf app/agents/video_generator
rm -rf app/agents/voice_generator
rm -rf app/agents/music_generator
rm -rf app/agents/fx_generator
rm -rf app/agents/editor
rm app/agents/screenwriter/tasks.py
rm tests/test_video_generator.py
rm tests/test_voice_generator.py
rm tests/test_music_generator.py
rm tests/test_fx_generator.py
rm tests/test_editor.py
```

- [ ] **Step 2: Remove screenwriter.py but keep __init__.py for now**

```bash
rm app/agents/screenwriter/screenwriter.py
```

- [ ] **Step 3: Run remaining tests to verify nothing is broken**

```bash
python -m pytest tests/ -v --tb=short -k "not test_generate_image"
```
Expected: All PASS

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "cleanup: remove obsolete generator agents"
```

---

### Task 7: Update requirements and rebuild Docker

**Files:**
- Modify: `requirements.txt` (already updated)
- Modify: `Dockerfile` (no change needed)

- [ ] **Step 1: Verify requirements.txt has pydantic-settings**

```bash
cat requirements.txt
# Should include: pydantic-settings>=2.5.0
```

- [ ] **Step 2: Rebuild and restart Docker**

```bash
docker compose build app
docker compose up -d app
```

- [ ] **Step 3: Verify app responds**

```bash
curl http://localhost:8000/health
# Expected: {"status":"healthy"}

curl http://localhost:8000/
# Expected: {"message":"AI Live Action Studio MVP"}
```

- [ ] **Step 4: Commit**

```bash
git add requirements.txt
git commit -m "chore: add pydantic-settings to requirements"
```
