# Advanced Editing Features — Design Specification

**Date:** 2026-06-29
**Project:** AI Live Action Studio
**Parent Spec:** 2026-06-29-ai-live-action-studio-design.md

## Overview

Replace the simulated Editor Agent with real FFmpeg-powered editing capabilities for transitions, color grading, and text overlays, with automatic fallback to simulation when FFmpeg is unavailable.

## Architecture

Three new modules under `app/agents/editor/`:

```
app/agents/editor/
  __init__.py
  editor.py               # Updated with pipeline integration
  tasks.py                # Unchanged
  transitions.py          # NEW
  color_grading.py        # NEW
  text_overlay.py         # NEW
tests/
  test_editor.py          # Updated
  test_transitions.py     # NEW
  test_color_grading.py   # NEW
  test_text_overlay.py    # NEW
```

## Components

### 1. Transitions Module (`transitions.py`)

**Classes:**
- `TransitionType(str, enum.Enum)` — `FADE_IN`, `FADE_OUT`, `CROSSFADE`, `DISSOLVE`, `CUT`
- `Transition` — single responsibility: apply a transition between clips or to a single clip

**Methods:**
- `apply(input_path, output_path, transition_type, duration=0.5, **params) -> dict`
  - Uses FFmpeg `xfade` filter for crossfade/dissolve between two inputs (requires a companion method `apply_between`)
  - `apply_single` for fade-in/fade-out on a single clip using `fade` filter
  - Falls back to copy input → output if FFmpeg check fails

**FFmpeg commands:**

```bash
# Fade in
ffmpeg -i input.mp4 -vf "fade=t=in:st=0:d=0.5" output.mp4

# Crossfade between two clips
ffmpeg -i clip1.mp4 -i clip2.mp4 -filter_complex "xfade=transition=fade:duration=0.5:offset=3.5" output.mp4
```

**Return value:** `{file_path, transition_type, duration, ffmpeg_used: bool}`

### 2. Color Grading Module (`color_grading.py`)

**Classes:**
- `ColorGrade` — apply color adjustments to a video clip

**Methods:**
- `apply(input_path, output_path, brightness=1.0, contrast=1.0, saturation=1.0, temperature=0.0, **params) -> dict`
  - `brightness`: 0.0–2.0 (1.0 = no change)
  - `contrast`: 0.0–2.0 (1.0 = no change)
  - `saturation`: 0.0–2.0 (1.0 = no change)
  - `temperature`: -1.0 (cool/blue) to 1.0 (warm/orange), 0.0 = neutral
  - Falls back to copy if FFmpeg unavailable

**FFmpeg commands:**

```bash
# Brightness/contrast/saturation via eq filter
ffmpeg -i input.mp4 -vf "eq=brightness=0.1:contrast=1.2:saturation=1.1" output.mp4

# Temperature via colorbalance (shadows, midtones, highlights)
ffmpeg -i input.mp4 -vf "colorbalance=rs=0.1:gs=-0.05:bs=-0.1" output.mp4
```

**Temperature mapping:** Convert -1..1 to FFmpeg `colorbalance` shadow/midtone/highlight adjustments uniformly. Positive = warmer (more red, less blue), Negative = cooler (less red, more blue).

**Return value:** `{file_path, params_applied: dict, ffmpeg_used: bool}`

### 3. Text Overlay Module (`text_overlay.py`)

**Classes:**
- `TextOverlay` — overlay text onto a video clip

**Methods:**
- `apply(input_path, output_path, text, position="bottom", font_size=24, font_color="white", opacity=1.0, start_time=0.0, duration=None, **params) -> dict`
  - `position`: `"top"`, `"bottom"`, `"center"`, or `(x, y)` tuple for custom
  - `opacity`: applied via `alpha` parameter in `drawtext`
  - `start_time` / `duration`: controls when text appears and disappears via `enable` expression
  - Falls back to copy if FFmpeg unavailable

**FFmpeg commands:**

```bash
# Basic bottom-center text
ffmpeg -i input.mp4 -vf "drawtext=text='Hello':fontsize=24:fontcolor=white:x=(w-text_w)/2:y=h-th-20" output.mp4

# Timed text (appears at 2s for 5s)
ffmpeg -i input.mp4 -vf "drawtext=text='Hello':enable='between(t,2,7)'" output.mp4
```

**Position mapping:** Convert named positions to x/y coordinates.

**Return value:** `{file_path, text, position, start_time, duration, ffmpeg_used: bool}`

### 4. EditorAgent Integration

**Updated `EditorAgent.assemble_video()` new optional params:**
- `transitions: List[Dict]` — each dict: `{type, duration, params}`
- `color_grading: Dict` — `{brightness, contrast, saturation, temperature}`
- `text_overlays: List[Dict]` — each dict: `{text, position, font_size, font_color, opacity, start_time, duration}`

**Processing pipeline (in order):**

```
[raw clips] → Color Grading → Text Overlays → Transitions → [final output]
```
Each step writes a temp file and passes it as input to the next step. The last step writes the final output. If any step's FFmpeg call fails or FFmpeg is unavailable, that step is skipped (file copied through).

**Config:**

Add to `app/core/config.py`:
```python
FFMPEG_PATH: str = "ffmpeg"
```

A helper function `_check_ffmpeg()` uses `shutil.which` to test availability once and caches the result.

## Testing

### Test Files

**`tests/test_transitions.py` (2 tests):**
- `test_transition_initialization` — verify module loads
- `test_apply_transition` — call apply with simulation fallback, verify output dict shape

**`tests/test_color_grading.py` (2 tests):**
- `test_color_grading_initialization`
- `test_apply_color_grading` — verify param ranges and return values

**`tests/test_text_overlay.py` (2 tests):**
- `test_text_overlay_initialization`
- `test_apply_text_overlay` — verify text, position, timing in return

**`tests/test_editor.py` (updated):**
- Existing `test_assemble_video` updated to pass new optional params
- Verify pipeline runs end-to-end in simulation mode

All tests use simulation fallback — no FFmpeg dependency.

## Future Phases (Not in Scope)

- **WebSocket real-time job updates** — separate spec
- **Real AI model integrations** — separate spec (replace simulated generators with actual Ollama/ComfyUI/Kling calls)

## Error Handling

- Each module catches `subprocess.CalledProcessError`, `FileNotFoundError`, and `OSError`
- If FFmpeg fails at any step, logs the error and copies input to output (degraded but functional)
- `ffmpeg_used: bool` in return dict lets callers detect whether real processing happened
