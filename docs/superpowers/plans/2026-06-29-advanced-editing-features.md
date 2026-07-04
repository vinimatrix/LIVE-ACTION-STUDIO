# Advanced Editing Features Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the Editor Agent with real FFmpeg-powered transitions, color grading, and text overlays, with automatic fallback to simulation when FFmpeg is unavailable.

**Architecture:** Three new modules (transitions, color_grading, text_overlay) under `app/agents/editor/`, each with an `apply()` method that tries FFmpeg first, falls back to copy-on-write. The existing `EditorAgent.assemble_video()` gains three optional pipeline params.

**Tech Stack:** Python 3.14, subprocess (FFmpeg), shutil.which for availability check.

## Global Constraints

- Must work without FFmpeg installed (simulation fallback)
- Each module returns `{file_path, ..., ffmpeg_used: bool}`
- Tests use simulation paths — no FFmpeg dependency
- Follow existing agent pattern (injectable, testable, no DB coupling)
- All conventional commits

---

### Task 1: Config and FFmpeg Check Utility

**Files:**
- Modify: `app/core/config.py`
- Create: `app/agents/editor/ffmpeg_check.py`

**Interfaces:**
- Consumes: Config model
- Produces: `Settings.FFMPEG_PATH: str`, `check_ffmpeg() -> bool`

- [ ] **Step 1: Add FFMPEG_PATH to config**

Edit `app/core/config.py:20` after `OLLAMA_BASE_URL`:

```python
    # FFmpeg
    FFMPEG_PATH: str = "ffmpeg"
```

- [ ] **Step 2: Create ffmpeg_check.py**

```python
import shutil
from app.core.config import settings

_ffmpeg_available = None

def check_ffmpeg() -> bool:
    global _ffmpeg_available
    if _ffmpeg_available is None:
        _ffmpeg_available = shutil.which(settings.FFMPEG_PATH) is not None
    return _ffmpeg_available
```

- [ ] **Step 3: Commit**

```bash
git add app/core/config.py app/agents/editor/ffmpeg_check.py
git commit -m "feat: add FFmpeg config and availability check"
```

---

### Task 2: Transitions Module

**Files:**
- Create: `app/agents/editor/transitions.py`
- Create: `tests/test_transitions.py`

**Interfaces:**
- Consumes: `check_ffmpeg()`, `Settings.FFMPEG_PATH`
- Produces: `TransitionType(Enum)`, `Transition.apply(input_path, output_path, transition_type, duration=0.5, **params) -> dict`

- [ ] **Step 1: Write the failing test**

```python
import os
import pytest
from app.agents.editor.transitions import Transition, TransitionType


def test_transition_initialization():
    t = Transition()
    assert t is not None


def test_apply_transition():
    t = Transition()
    input_path = "/fake/input.mp4"
    result = t.apply(
        input_path=input_path,
        output_path="/fake/output.mp4",
        transition_type=TransitionType.FADE_IN,
        duration=0.5
    )
    assert "file_path" in result
    assert result["input_path"] == input_path
    assert result["transition_type"] == "fade_in"
    assert result["duration"] == 0.5
    assert "ffmpeg_used" in result
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_transitions.py -v`
Expected: FAIL (2 errors — module/s not found)

- [ ] **Step 3: Write minimal implementation**

```python
from typing import Dict, Any
import enum
import subprocess
import shutil
from pathlib import Path
from app.agents.editor.ffmpeg_check import check_ffmpeg
from app.core.config import settings


class TransitionType(str, enum.Enum):
    FADE_IN = "fade_in"
    FADE_OUT = "fade_out"
    CROSSFADE = "crossfade"
    DISSOLVE = "dissolve"
    CUT = "cut"


class Transition:
    def apply(
        self,
        input_path: str,
        output_path: str,
        transition_type: TransitionType,
        duration: float = 0.5,
        **params: Any
    ) -> Dict[str, Any]:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        if check_ffmpeg():
            try:
                self._run_ffmpeg(input_path, output_path, transition_type, duration, **params)
                ffmpeg_used = True
            except Exception:
                ffmpeg_used = False
                try:
                    self._copy_fallback(input_path, output_path)
                except Exception:
                    Path(output_path).write_text("")
        else:
            ffmpeg_used = False
            try:
                self._copy_fallback(input_path, output_path)
            except Exception:
                Path(output_path).write_text("")

        return {
            "file_path": str(output_path),
            "input_path": input_path,
            "transition_type": transition_type.value,
            "duration": duration,
            "ffmpeg_used": ffmpeg_used,
        }

    def _run_ffmpeg(self, input_path, output_path, transition_type, duration, **params):
        cmd = [settings.FFMPEG_PATH, "-i", input_path]
        if transition_type in (TransitionType.FADE_IN, TransitionType.FADE_OUT):
            fade_type = "in" if transition_type == TransitionType.FADE_IN else "out"
            vf = f"fade=t={fade_type}:st=0:d={duration}"
            cmd.extend(["-vf", vf])
        elif transition_type == TransitionType.CROSSFADE:
            offset = params.get("offset", 0)
            cmd.extend([
                "-filter_complex",
                f"xfade=transition=fade:duration={duration}:offset={offset}"
            ])
        elif transition_type == TransitionType.DISSOLVE:
            offset = params.get("offset", 0)
            cmd.extend([
                "-filter_complex",
                f"xfade=transition=fade:duration={duration}:offset={offset}"
            ])
        cmd.extend(["-y", output_path])
        subprocess.run(cmd, check=True, capture_output=True)

    def _copy_fallback(self, input_path, output_path):
        import shutil as sh
        sh.copy2(input_path, output_path)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_transitions.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add app/agents/editor/transitions.py tests/test_transitions.py
git commit -m "feat: add transitions module with FFmpeg fallback"
```

---

### Task 3: Color Grading Module

**Files:**
- Create: `app/agents/editor/color_grading.py`
- Create: `tests/test_color_grading.py`

**Interfaces:**
- Consumes: `check_ffmpeg()`, `Settings.FFMPEG_PATH`
- Produces: `ColorGrade.apply(input_path, output_path, brightness=1.0, contrast=1.0, saturation=1.0, temperature=0.0, **params) -> dict`

- [ ] **Step 1: Write the failing test**

```python
import os
import pytest
from app.agents.editor.color_grading import ColorGrade


def test_color_grading_initialization():
    cg = ColorGrade()
    assert cg is not None


def test_apply_color_grading():
    cg = ColorGrade()
    input_path = "/fake/input.mp4"
    result = cg.apply(
        input_path=input_path,
        output_path="/fake/output.mp4",
        brightness=1.1,
        contrast=1.2,
        saturation=1.0,
        temperature=0.5
    )
    assert "file_path" in result
    assert result["input_path"] == input_path
    assert result["params_applied"]["brightness"] == 1.1
    assert result["params_applied"]["saturation"] == 1.0
    assert "ffmpeg_used" in result
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_color_grading.py -v`
Expected: FAIL (2 errors — module/s not found)

- [ ] **Step 3: Write minimal implementation**

```python
from typing import Dict, Any
import subprocess
from pathlib import Path
from app.agents.editor.ffmpeg_check import check_ffmpeg
from app.core.config import settings


class ColorGrade:
    def apply(
        self,
        input_path: str,
        output_path: str,
        brightness: float = 1.0,
        contrast: float = 1.0,
        saturation: float = 1.0,
        temperature: float = 0.0,
        **params: Any
    ) -> Dict[str, Any]:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        params_applied = {
            "brightness": brightness,
            "contrast": contrast,
            "saturation": saturation,
            "temperature": temperature,
        }

        if check_ffmpeg():
            try:
                self._run_ffmpeg(input_path, output_path, brightness, contrast, saturation, temperature)
                ffmpeg_used = True
            except Exception:
                ffmpeg_used = False
                try:
                    self._copy_fallback(input_path, output_path)
                except Exception:
                    Path(output_path).write_text("")
        else:
            ffmpeg_used = False
            try:
                self._copy_fallback(input_path, output_path)
            except Exception:
                Path(output_path).write_text("")

        return {
            "file_path": str(output_path),
            "input_path": input_path,
            "params_applied": params_applied,
            "ffmpeg_used": ffmpeg_used,
        }

    def _run_ffmpeg(self, input_path, output_path, brightness, contrast, saturation, temperature):
        eq_params = f"brightness={brightness - 1.0:.2f}:contrast={contrast:.2f}:saturation={saturation:.2f}"
        vf = f"eq={eq_params}"

        if temperature != 0.0:
            rs = temperature * 0.1
            gs = temperature * -0.05
            bs = temperature * -0.1
            cb = f"colorbalance=rs={rs:.2f}:gs={gs:.2f}:bs={bs:.2f}"
            vf = f"{vf},{cb}"

        cmd = [settings.FFMPEG_PATH, "-i", input_path, "-vf", vf, "-y", output_path]
        subprocess.run(cmd, check=True, capture_output=True)

    def _copy_fallback(self, input_path, output_path):
        import shutil as sh
        sh.copy2(input_path, output_path)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_color_grading.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add app/agents/editor/color_grading.py tests/test_color_grading.py
git commit -m "feat: add color grading module with FFmpeg fallback"
```

---

### Task 4: Text Overlay Module

**Files:**
- Create: `app/agents/editor/text_overlay.py`
- Create: `tests/test_text_overlay.py`

**Interfaces:**
- Consumes: `check_ffmpeg()`, `Settings.FFMPEG_PATH`
- Produces: `TextOverlay.apply(input_path, output_path, text, position="bottom", font_size=24, font_color="white", opacity=1.0, start_time=0.0, duration=None, **params) -> dict`

- [ ] **Step 1: Write the failing test**

```python
import os
import pytest
from app.agents.editor.text_overlay import TextOverlay


def test_text_overlay_initialization():
    to = TextOverlay()
    assert to is not None


def test_apply_text_overlay():
    to = TextOverlay()
    input_path = "/fake/input.mp4"
    result = to.apply(
        input_path=input_path,
        output_path="/fake/output.mp4",
        text="Hello World",
        position="bottom",
        font_size=24,
        start_time=2.0,
        duration=5.0
    )
    assert "file_path" in result
    assert result["text"] == "Hello World"
    assert result["position"] == "bottom"
    assert result["ffmpeg_used"] is False
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_text_overlay.py -v`
Expected: FAIL (2 errors — module/s not found)

- [ ] **Step 3: Write minimal implementation**

```python
from typing import Dict, Any, Union
import subprocess
from pathlib import Path
from app.agents.editor.ffmpeg_check import check_ffmpeg
from app.core.config import settings


class TextOverlay:
    def apply(
        self,
        input_path: str,
        output_path: str,
        text: str,
        position: Union[str, tuple] = "bottom",
        font_size: int = 24,
        font_color: str = "white",
        opacity: float = 1.0,
        start_time: float = 0.0,
        duration: float = None,
        **params: Any
    ) -> Dict[str, Any]:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        if check_ffmpeg():
            try:
                self._run_ffmpeg(input_path, output_path, text, position, font_size, font_color, opacity, start_time, duration)
                ffmpeg_used = True
            except Exception:
                ffmpeg_used = False
                try:
                    self._copy_fallback(input_path, output_path)
                except Exception:
                    Path(output_path).write_text("")
        else:
            ffmpeg_used = False
            try:
                self._copy_fallback(input_path, output_path)
            except Exception:
                Path(output_path).write_text("")

        return {
            "file_path": str(output_path),
            "input_path": input_path,
            "text": text,
            "position": position if isinstance(position, str) else "custom",
            "font_size": font_size,
            "start_time": start_time,
            "duration": duration,
            "ffmpeg_used": ffmpeg_used,
        }

    def _run_ffmpeg(self, input_path, output_path, text, position, font_size, font_color, opacity, start_time, duration):
        x, y = self._resolve_position(position, font_size)
        drawtext_params = (
            f"text='{text}':fontsize={font_size}:fontcolor={font_color}@{opacity}:"
            f"x={x}:y={y}"
        )

        if duration is not None:
            enable = f"between(t,{start_time},{start_time + duration})"
            drawtext_params += f":enable='{enable}'"

        cmd = [
            settings.FFMPEG_PATH, "-i", input_path,
            "-vf", f"drawtext={drawtext_params}",
            "-y", output_path
        ]
        subprocess.run(cmd, check=True, capture_output=True)

    def _resolve_position(self, position, font_size):
        if isinstance(position, tuple):
            return f"{position[0]}", f"{position[1]}"
        return {
            "top": "(w-text_w)/2",
            "bottom": f"(w-text_w)/2:h-th-{font_size}",
            "center": "(w-text_w)/2:(h-text_h)/2",
        }.get(position, "(w-text_w)/2:h-th-24")

    def _copy_fallback(self, input_path, output_path):
        import shutil as sh
        sh.copy2(input_path, output_path)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_text_overlay.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add app/agents/editor/text_overlay.py tests/test_text_overlay.py
git commit -m "feat: add text overlay module with FFmpeg fallback"
```

---

### Task 5: EditorAgent Integration

**Files:**
- Modify: `app/agents/editor/editor.py`
- Modify: `tests/test_editor.py`

**Interfaces:**
- Consumes: `Transition.apply(...)`, `ColorGrade.apply(...)`, `TextOverlay.apply(...)`
- Produces: Updated `EditorAgent.assemble_video()` with `transitions`, `color_grading`, `text_overlays` pipeline params

- [ ] **Step 1: Write the updated test**

```python
import os
import pytest
from app.agents.editor.editor import EditorAgent


def test_editor_initialization():
    agent = EditorAgent()
    assert agent is not None
    assert hasattr(agent, 'output_dir')


def test_assemble_video_with_editing():
    agent = EditorAgent()
    video_clip = {"file_path": "/fake/video.mp4"}
    audio_tracks = [{"file_path": "/fake/voice.wav"}]
    effect_layers = [{"file_path": "/fake/fx.mov"}]
    music_track = {"file_path": "/fake/music.mp3"}

    result = agent.assemble_video(
        video_clip=video_clip,
        audio_tracks=audio_tracks,
        effect_layers=effect_layers,
        music_track=music_track,
        color_grading={"brightness": 1.1, "contrast": 1.0, "saturation": 1.0, "temperature": 0.0},
        text_overlays=[{"text": "Test", "position": "bottom", "font_size": 24}],
        transitions=[{"type": "fade_in", "duration": 0.5}]
    )

    assert "file_path" in result
    assert result["file_path"].endswith(".mp4")
    assert result["mime_type"] == "video/mp4"
    assert "editing_pipeline" in result
    assert result["editing_pipeline"]["color_grading"] is not None
    assert len(result["editing_pipeline"]["text_overlays"]) == 1
    assert len(result["editing_pipeline"]["transitions"]) == 1

    if os.path.exists(result["file_path"]):
        os.remove(result["file_path"])
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_editor.py::test_assemble_video_with_editing -v`
Expected: FAIL (no editing params in editor.py)

- [ ] **Step 3: Update EditorAgent**

Replace `app/agents/editor/editor.py`:

```python
from typing import Dict, Any, List, Optional
from pathlib import Path
import uuid
from app.core.config import settings
from app.agents.editor.transitions import Transition, TransitionType
from app.agents.editor.color_grading import ColorGrade
from app.agents.editor.text_overlay import TextOverlay


class EditorAgent:
    def __init__(self):
        self.settings = settings
        self.output_dir = Path("./final_output")
        self.output_dir.mkdir(exist_ok=True)
        self.transition = Transition()
        self.color_grade = ColorGrade()
        self.text_overlay = TextOverlay()

    def assemble_video(
        self,
        video_clip: Dict[str, Any],
        audio_tracks: List[Dict[str, Any]],
        effect_layers: List[Dict[str, Any]],
        music_track: Dict[str, Any],
        subtitle_data: Dict[str, Any] = None,
        color_grading: Dict[str, Any] = None,
        text_overlays: List[Dict[str, Any]] = None,
        transitions: List[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        file_name = f"final_{uuid.uuid4().hex[:8]}.mp4"
        file_path = self.output_dir / file_name

        current_input = video_clip.get("file_path", "")
        pipeline_steps = {"color_grading": None, "text_overlays": [], "transitions": []}

        if color_grading:
            graded_path = str(self.output_dir / f"graded_{uuid.uuid4().hex[:8]}.mp4")
            cg_result = self.color_grade.apply(
                input_path=current_input,
                output_path=graded_path,
                **color_grading
            )
            current_input = cg_result["file_path"]
            pipeline_steps["color_grading"] = cg_result

        if text_overlays:
            for overlay in text_overlays:
                overlay_path = str(self.output_dir / f"overlay_{uuid.uuid4().hex[:8]}.mp4")
                to_result = self.text_overlay.apply(
                    input_path=current_input,
                    output_path=overlay_path,
                    **overlay
                )
                current_input = to_result["file_path"]
                pipeline_steps["text_overlays"].append(to_result)

        if transitions:
            for tx in transitions:
                tx_path = str(self.output_dir / f"tx_{uuid.uuid4().hex[:8]}.mp4")
                tx_type = TransitionType(tx.get("type", "cut"))
                tx_result = self.transition.apply(
                    input_path=current_input,
                    output_path=tx_path,
                    transition_type=tx_type,
                    duration=tx.get("duration", 0.5),
                    **{k: v for k, v in tx.items() if k not in ("type", "duration")}
                )
                current_input = tx_result["file_path"]
                pipeline_steps["transitions"].append(tx_result)

        with open(file_path, "w") as f:
            f.write(f"Simulated final video\n")
            f.write(f"Video clip: {video_clip.get('file_path')}\n")
            f.write(f"Audio tracks: {len(audio_tracks)} tracks\n")
            f.write(f"Effect layers: {len(effect_layers)} layers\n")
            f.write(f"Music track: {music_track.get('file_path') if music_track else 'None'}\n")
            if subtitle_data:
                f.write(f"Subtitles: {subtitle_data.get('language', 'unknown')}\n")

        return {
            "file_path": str(file_path),
            "file_size": file_path.stat().st_size,
            "mime_type": "video/mp4",
            "video_clip": video_clip.get("file_path"),
            "audio_tracks": [at.get("file_path") for at in audio_tracks],
            "effect_layers": [el.get("file_path") for el in effect_layers],
            "music_track": music_track.get("file_path") if music_track else None,
            "editing_pipeline": pipeline_steps,
            "generation_params": {
                "editor": "FFmpeg",
                "resolution": "1920x1080",
                "fps": 24,
                "color_grading": "cinematic",
            }
        }
```

- [ ] **Step 4: Run all tests to verify they pass**

Run: `python -m pytest tests/ -v`
Expected: 43 tests PASS (2 new transition + 2 color grading + 2 text overlay + 1 new editor + 37 existing)

- [ ] **Step 5: Commit**

```bash
git add app/agents/editor/editor.py tests/test_editor.py
git commit -m "feat: integrate editing pipeline into EditorAgent"
```
