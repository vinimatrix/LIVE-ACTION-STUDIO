# Director Styles System — Design Spec

**Date:** 2026-07-07
**Status:** Design
**Version:** 1

## 1. Overview

Add a director-style system to the AI Live Action Studio pipeline that allows the StoryboardAgent and FlowPromptBuilderAgent to generate shots and prompts with the signature cinematography of specific directors. The style is auto-selected based on scene mood but can be manually overridden.

## 2. Architecture

### 2.1 New Module: `app/agents/director_styles.py`

A configuration-only module containing:

- `DIRECTOR_STYLES` dict with presets for 6 directors
- `STYLE_MOOD_MAP` dict mapping mood values to default styles
- `resolve_style()` helper function

```
app/agents/director_styles.py
```

### 2.2 Affected Modules

| Module | Change |
|--------|--------|
| `app/agents/director_styles.py` | **NEW** — style presets and resolver |
| `app/agents/storyboard/storyboard.py` | Add style-aware shot planning, new movements/shots |
| `app/agents/scene_composer/scene_composer.py` | Extend shot type and movement pools |
| `app/agents/flow_prompt_builder/flow_prompt_builder.py` | Add director/slow-mo/flare sections to prompts |
| `app/agents/director/director.py` | Pass `director_style` through options |

### 2.3 Data Flow

```
API Request (options.director_style optional)
  → DirectorAgent.process_manga_request()
    → SceneComposerAgent.compose()  [enhanced shot/move pools]
      → StoryboardAgent.break_down_scene(style=resolve_style())
        → _build_action_styled(config)
      → FlowPromptBuilderAgent.build_prompts(director_style)
        → prompts include DIRECTION, SLOW-MO, FLARE sections
```

## 3. Director Presets

### 3.1 Michael Bay

| Parameter | Value |
|-----------|-------|
| Action moods | explosive, intense, epic, dramatic |
| Preferred movements | 360_orbit, crane_up, drone_sweep, whip_pan |
| Preferred shot types | low_angle, extreme_wide, close_up |
| Slow motion | 120fps, 2-4s bursts |
| Lens flares | Yes (anamorphic) |
| Dutch angle | 5° |
| Shot duration range | 1.5–6.0s (fast cutting) |
| Color grading | Teal-orange high contrast |
| Signature | Heroic slow-mo, explosions, low angles, fast cuts |

### 3.2 Russo Brothers

| Parameter | Value |
|-----------|-------|
| Action moods | intense, epic, tactical, dramatic |
| Preferred movements | handheld, steadicam, 360_orbit, tracking |
| Preferred shot types | medium, close_up, over_the_shoulder |
| Slow motion | 60fps, 1.5-3s, selective impacts |
| Handheld intensity | 0.4 (moderate) |
| Shot duration range | 2.0–8.0s |
| Color grading | Natural saturated |
| Signature | Handheld action, long takes, 360° circling fights, tactical beats |

### 3.3 Sam Raimi

| Parameter | Value |
|-----------|-------|
| Action moods | intense, epic, dramatic, chaotic |
| Preferred movements | crash_zoom, whip_pan, dutch_angle, pov_raimi, handheld |
| Preferred shot types | low_angle, close_up, extreme_close_up, pov |
| Slow motion | Disabled |
| Dutch angle | 25° (exaggerated) |
| Shot duration range | 1.0–4.0s |
| Color grading | Saturated contrast |
| Signature | Dutch angles, rapid crash zooms, POV demon cam, cutaway reaction extras |

### 3.4 Christopher Nolan

| Parameter | Value |
|-----------|-------|
| Action moods | intense, epic, dramatic, suspense |
| Preferred movements | imax_steady, tracking, arm_car_mount, technocrane, dolly |
| Preferred shot types | medium, wide, imax_close_up, extreme_wide |
| Slow motion | Disabled (prefers practical speed) |
| Lens flares | Yes (anamorphic) |
| Shot duration range | 3.0–15.0s (longer takes) |
| Color grading | Natural muted |
| Signature | IMAX format, practical effects, cross-cutting, deep focus |

### 3.5 Akira Kurosawa

| Parameter | Value |
|-----------|-------|
| Action moods | epic, dramatic, intense |
| Preferred movements | static, slow_dolly, tracking_multi_cam, axial_cut |
| Preferred shot types | wide, medium, telephoto_compression, deep_focus |
| Slow motion | Disabled |
| Shot duration range | 4.0–12.0s |
| Color grading | High contrast BW |
| Signature | Wipe transitions, multi-camera action, weather as mood, axial cuts |

### 3.6 James Gunn

| Parameter | Value |
|-----------|-------|
| Action moods | epic, intense, chaotic, comedic |
| Preferred movements | stedicam_hybrid, handheld, whip_pan, tracking |
| Preferred shot types | medium, close_up, wide, over_the_shoulder |
| Slow motion | 48fps, 1-3s, comedic/heroic |
| Shot duration range | 2.0–7.0s |
| Color grading | Vivid colorful |
| Signature | Music-synced action, comedic framing, stabilized rig, colorful explosions |

## 4. StoryboardAgent Changes

### 4.1 New Movement Types

```
360_orbit, handheld, crane_up, crane_down, drone_sweep, whip_pan,
dutch_angle, crash_zoom, pov_raimi, imax_steady, arm_car_mount,
technocrane, tracking_multi_cam, axial_cut, stedicam_hybrid
```

### 4.2 New Shot Types

```
low_angle, high_angle, birds_eye, point_of_view, imax_close_up,
telephoto_compression, deep_focus
```

### 4.3 New Shot Fields

```python
{
    "slow_motion": bool,
    "lens_flare": bool,
    "dutch_angle": float,  # degrees
    "director_style": str,
}
```

### 4.4 `break_down_scene()` Enhancement

```python
def break_down_scene(self, scene, director_style=None):
    style = resolve_style(director_style, scene.get("lighting", {}).get("mood_lighting"))
    config = DIRECTOR_STYLES.get(style)
    # For action scenes with a director style, use _build_action_styled
    if config and self._is_action_scene(mood):
        return self._build_action_styled(scene, config)
    # Existing logic for non-action or no-style
```

### 4.5 `_build_action_styled()` Method

Generates 3-5 shots based on the director's preferred shot types and movements. For Michael Bay:
```
Shot 1: low_angle + 360_orbit → establishing power
Shot 2: extreme_wide + drone_sweep → scale of explosion
Shot 3: close_up + whip_pan + slow_motion → impact moment
Shot 4: low_angle + static + flare → heroic pose
```

For Russo Brothers:
```
Shot 1: wide + handheld → chaotic establishing
Shot 2: medium + steadicam → following action
Shot 3: close_up + 360_orbit → circling combat
Shot 4: close_up + slow_motion → impact (selective)
```

### 4.6 Slow Motion Handling

When `slow_motion.enabled` is True:
- The shot dict gets `slow_motion: True` and `slow_motion_fps`
- The shot's `duration` is multiplied by the slow-mo factor (e.g., 120fps/24fps = 5x)
- The `end_time` is adjusted accordingly
- The original "real-time" duration is stored in `real_duration`

## 5. SceneComposerAgent Changes

Shot type pool expanded:
```python
shots = ["wide", "medium", "close-up", "over-the-shoulder", "extreme-close-up",
         "low_angle", "high_angle", "birds_eye", "point_of_view"]
```

Movement pool expanded:
```python
movements = ["static", "dolly", "pan", "tilt", "steadicam", "handheld",
             "360_orbit", "crane_up", "crane_down", "drone_sweep", "whip_pan"]
```

`_build_scene()` now propagates `director_style`, `slow_motion`, `lens_flare`, `dutch_angle` in the scene dict.

## 6. FlowPromptBuilderAgent Changes

New sections in the generated prompt:

```
DIRECCIÓN:
  - Estilo: Michael Bay
  - Slow motion: SHOT 3 (2.5s a 120fps) — impacto de explosión
  - Flares: Activados (anamórficos)
  - Dutch angle: 5°
  - Color grading: teal-orange high contrast
```

In storyboard shot blocks:
```
║  SLOW-MO: ✅ (120fps, 2.5s)
║  FLARE: ✅
║  CÁMARA: 360° orbit alrededor del personaje
```

## 7. DirectorAgent Changes

`process_manga_request()` now reads `options.director_style` and passes it through the pipeline:

```python
def process_manga_request(self, manga_data, options=None):
    director_style = (options or {}).get("director_style")
    scenes = scene_composer.compose(analysis, max_scenes=5, director_style=director_style)
    storyboard.shots = storyboard.break_down_scene(scene, director_style=director_style)
    prompts = flow_builder.build_prompts(scenes, character_mapping, director_style=director_style)
```

## 8. API

POST `/api/v1/process-manga` accepts optional `director_style`:

```json
{
    "filename": "boruto_chapter_1.png",
    "options": {
        "director_style": "michael_bay"
    }
}
```

If not specified, `resolve_style()` auto-selects based on scene mood.

## 9. Tests

### 9.1 New Test File: `tests/test_director_styles.py`

- `test_presets_have_required_keys()` — each director has all required fields
- `test_resolve_style_manual_override()` — explicit style is returned
- `test_resolve_style_by_mood()` — mood maps to correct director
- `test_resolve_style_none()` — unknown mood returns None
- `test_resolve_style_invalid_name()` — falls back to mood mapping
- `test_mood_map_covers_all_action_moods()` — every mood in presets has mapping

### 9.2 Enhanced Tests

- `test_storyboard.py`: test `_build_action_styled()` for Bay and Russo, verify slow_motion flags, new movement types
- `test_flow_prompt_builder.py`: verify DIRECCIÓN section appears, slow-mo/shots listed
- `test_scene_composer.py`: verify new shot types and movements cycle correctly

## 10. Out of Scope

- Actual video generation of slow-motion or 360° orbits (handled by VideoGenerationAgent downstream)
- CinematographyAgent standalone agent (may be created in future if needed)
- Runtime director style switching mid-scene
- Color grading at the pixel level (prompt-based only)
