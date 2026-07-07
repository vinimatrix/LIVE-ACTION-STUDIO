# Director Styles System — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 6 directorial style presets (Michael Bay, Russo Brothers, Sam Raimi, Christopher Nolan, Akira Kurosawa, James Gunn) to the AI Live Action Studio pipeline, with auto-selection by mood and manual override.

**Architecture:** New `app/agents/director_styles.py` config module + enhancements to StoryboardAgent (style-aware shot planning, new movement/shot types) + FlowPromptBuilderAgent (director sections in prompts) + SceneComposerAgent (extended pools) + DirectorAgent (pass-through).

**Tech Stack:** Python 3.14, pytest, existing agent classes

## Global Constraints

- All new code must follow existing project patterns (class-based agents, typing)
- New movement names: 360_orbit, handheld, crane_up, crane_down, drone_sweep, whip_pan, dutch_angle, crash_zoom, pov_raimi, imax_steady, arm_car_mount, technocrane, tracking_multi_cam, axial_cut, stedicam_hybrid
- New shot type names: low_angle, high_angle, birds_eye, point_of_view, imax_close_up, telephoto_compression, deep_focus
- Director style keys: michael_bay, russo_brothers, sam_raimi, christopher_nolan, akira_kurosawa, james_gunn
- Test files in `tests/` directory

---

### Task 1: Create `app/agents/director_styles.py` module

**Files:**
- Create: `app/agents/director_styles.py`
- Test: `tests/test_director_styles.py`

**Interfaces:**
- Produces: `DIRECTOR_STYLES` dict, `STYLE_MOOD_MAP` dict, `resolve_style(director_style=None, mood="neutral") -> str | None`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_director_styles.py
import pytest
from app.agents.director_styles import DIRECTOR_STYLES, STYLE_MOOD_MAP, resolve_style

REQUIRED_KEYS = [
    "action_moods", "preferred_movements", "preferred_shot_types",
    "slow_motion", "shot_duration_range", "color_grading", "lighting_contrast"
]


class TestDirectorStyles:
    def test_all_presets_have_required_keys(self):
        for name, preset in DIRECTOR_STYLES.items():
            for key in REQUIRED_KEYS:
                assert key in preset, f"{name} missing key: {key}"

    def test_six_directors_defined(self):
        assert set(DIRECTOR_STYLES.keys()) == {
            "michael_bay", "russo_brothers", "sam_raimi",
            "christopher_nolan", "akira_kurosawa", "james_gunn"
        }

    def test_each_preset_has_at_least_one_movement(self):
        for name, preset in DIRECTOR_STYLES.items():
            assert len(preset["preferred_movements"]) > 0

    def test_each_preset_has_at_least_one_shot_type(self):
        for name, preset in DIRECTOR_STYLES.items():
            assert len(preset["preferred_shot_types"]) > 0

    def test_slow_motion_has_enabled_flag(self):
        for name, preset in DIRECTOR_STYLES.items():
            assert "enabled" in preset["slow_motion"]

    def test_shot_duration_range_is_tuple_of_two(self):
        for name, preset in DIRECTOR_STYLES.items():
            lo, hi = preset["shot_duration_range"]
            assert lo <= hi


class TestStyleMoodMap:
    def test_resolve_style_manual_override(self):
        assert resolve_style("michael_bay") == "michael_bay"

    def test_resolve_style_by_mood(self):
        assert resolve_style(mood="explosive") == "michael_bay"
        assert resolve_style(mood="intense") == "russo_brothers"
        assert resolve_style(mood="epic") == "akira_kurosawa"

    def test_resolve_style_none_for_unknown_mood(self):
        assert resolve_style(mood="unknown_xyz") is None

    def test_resolve_style_override_beats_mood(self):
        assert resolve_style("james_gunn", mood="explosive") == "james_gunn"

    def test_resolve_style_invalid_name_falls_back_to_mood(self):
        result = resolve_style("nonexistent_style", mood="explosive")
        assert result == "michael_bay"

    def test_resolve_style_invalid_name_and_unknown_mood(self):
        assert resolve_style("nonexistent_style", mood="xyz") is None

    def test_resolve_style_empty_mood(self):
        assert resolve_style(mood="") is None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_director_styles.py -v`
Expected: ImportError for `from app.agents.director_styles import ...`

- [ ] **Step 3: Write minimal implementation**

```python
# app/agents/director_styles.py
DIRECTOR_STYLES = {
    "michael_bay": {
        "action_moods": ["explosive", "intense", "epic", "dramatic"],
        "preferred_movements": ["360_orbit", "crane_up", "drone_sweep", "whip_pan"],
        "preferred_shot_types": ["low_angle", "extreme_wide", "close_up"],
        "slow_motion": {"enabled": True, "fps": 120, "min_duration": 2.0, "max_duration": 4.0},
        "lens_flare": True,
        "dutch_angle": 5,
        "shot_duration_range": (1.5, 6.0),
        "explosion_intensity": "heavy",
        "action_pattern": "fast_cutting",
        "color_grading": "teal_orange_high_contrast",
        "lighting_contrast": "high",
    },
    "russo_brothers": {
        "action_moods": ["intense", "epic", "tactical", "dramatic"],
        "preferred_movements": ["handheld", "steadicam", "360_orbit", "tracking"],
        "preferred_shot_types": ["medium", "close_up", "over_the_shoulder"],
        "slow_motion": {"enabled": True, "fps": 60, "min_duration": 1.5, "max_duration": 3.0},
        "lens_flare": False,
        "handheld_intensity": 0.4,
        "shot_duration_range": (2.0, 8.0),
        "action_pattern": "tactical_beats",
        "color_grading": "natural_saturated",
        "lighting_contrast": "natural",
    },
    "sam_raimi": {
        "action_moods": ["intense", "epic", "dramatic", "chaotic"],
        "preferred_movements": ["crash_zoom", "whip_pan", "dutch_angle", "pov_raimi", "handheld"],
        "preferred_shot_types": ["low_angle", "close_up", "extreme_close_up", "pov"],
        "slow_motion": {"enabled": False},
        "lens_flare": False,
        "dutch_angle": 25,
        "shot_duration_range": (1.0, 4.0),
        "explosion_intensity": "over_the_top",
        "action_pattern": "rapid_montage",
        "color_grading": "saturated_contrast",
        "lighting_contrast": "high",
    },
    "christopher_nolan": {
        "action_moods": ["intense", "epic", "dramatic", "suspense"],
        "preferred_movements": ["imax_steady", "tracking", "arm_car_mount", "technocrane", "dolly"],
        "preferred_shot_types": ["medium", "wide", "imax_close_up", "extreme_wide"],
        "slow_motion": {"enabled": False},
        "lens_flare": True,
        "shot_duration_range": (3.0, 15.0),
        "color_grading": "natural_muted",
        "lighting_contrast": "natural",
    },
    "akira_kurosawa": {
        "action_moods": ["epic", "dramatic", "intense"],
        "preferred_movements": ["static", "slow_dolly", "tracking_multi_cam", "axial_cut"],
        "preferred_shot_types": ["wide", "medium", "telephoto_compression", "deep_focus"],
        "slow_motion": {"enabled": False},
        "lens_flare": True,
        "shot_duration_range": (4.0, 12.0),
        "color_grading": "high_contrast_bw",
        "lighting_contrast": "dramatic",
    },
    "james_gunn": {
        "action_moods": ["epic", "intense", "chaotic", "comedic"],
        "preferred_movements": ["stedicam_hybrid", "handheld", "whip_pan", "tracking"],
        "preferred_shot_types": ["medium", "close_up", "wide", "over_the_shoulder"],
        "slow_motion": {"enabled": True, "fps": 48, "min_duration": 1.0, "max_duration": 3.0},
        "lens_flare": False,
        "shot_duration_range": (2.0, 7.0),
        "color_grading": "vivid_colorful",
        "lighting_contrast": "medium",
    },
}

STYLE_MOOD_MAP = {
    "explosive": "michael_bay",
    "intense": "russo_brothers",
    "epic": "akira_kurosawa",
    "dramatic": "sam_raimi",
    "tactical": "russo_brothers",
    "tension": "sam_raimi",
    "suspense": "christopher_nolan",
    "chaotic": "james_gunn",
    "comedic": "james_gunn",
}


def resolve_style(director_style=None, mood="neutral"):
    if director_style and director_style in DIRECTOR_STYLES:
        return director_style
    if director_style and director_style not in DIRECTOR_STYLES:
        return STYLE_MOOD_MAP.get(mood, None)
    return STYLE_MOOD_MAP.get(mood, None)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_director_styles.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add app/agents/director_styles.py tests/test_director_styles.py
git commit -m "feat: add director_styles module with 6 presets and mood mapping"
```

---

### Task 2: Extend SceneComposerAgent shot/movement pools

**Files:**
- Modify: `app/agents/scene_composer/scene_composer.py:136-141`
- Test: `tests/test_scene_composer.py`

**Interfaces:**
- Consumes: `SceneComposerAgent` class (existing interface)
- Produces: Extended `_select_shot()` and `_select_movement()` with new types; `_build_scene()` now accepts and propagates `director_style`; `compose()` accepts `director_style` parameter

- [ ] **Step 1: Write the failing tests**

```python
# Add to tests/test_scene_composer.py, inside TestSceneComposerSelectors class

    def test_select_shot_includes_new_types(self):
        agent = SceneComposerAgent()
        new_shots = {"low_angle", "high_angle", "birds_eye", "point_of_view"}
        all_returned = {agent._select_shot(i, 20) for i in range(20)}
        assert new_shots.issubset(all_returned)

    def test_select_movement_includes_new_types(self):
        agent = SceneComposerAgent()
        new_moves = {"handheld", "360_orbit", "crane_up", "crane_down", "drone_sweep", "whip_pan"}
        all_returned = {agent._select_movement(i) for i in range(30)}
        assert new_moves.issubset(all_returned)

    def test_compose_accepts_director_style(self):
        agent = SceneComposerAgent()
        from tests.test_scene_composer import TestSceneComposer
        scenes = agent.compose(TestSceneComposer.SAMPLE_ANALYSIS, max_scenes=1, director_style="michael_bay")
        assert isinstance(scenes, list)
        assert len(scenes) > 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_scene_composer.py::TestSceneComposerSelectors -v`
Expected: FAIL — missing shot types and movement types

- [ ] **Step 3: Extend shot and movement pools in `_select_shot` and `_select_movement`**

```python
# In app/agents/scene_composer/scene_composer.py:136-142

    def _select_shot(self, index, total):
        shots = ["wide", "medium", "close-up", "over-the-shoulder", "extreme-close-up",
                 "low_angle", "high_angle", "birds_eye", "point_of_view"]
        return shots[index % len(shots)]

    def _select_movement(self, index):
        movements = ["static", "dolly", "pan", "tilt", "steadicam", "handheld",
                     "360_orbit", "crane_up", "crane_down", "drone_sweep", "whip_pan"]
        return movements[index % len(movements)]
```

- [ ] **Step 4: Update `compose()` to accept `director_style` and propagate it**

```python
# Modify app/agents/scene_composer/scene_composer.py:44-46
    def compose(self, manga_analysis: Dict[str, Any], max_scenes: int = 5, director_style: str = None) -> List[Dict[str, Any]]:
        ...
        # Add director_style to each built scene
        raw_scenes = []
        if panels and len(panels) > 1:
            for i, panel in enumerate(panels):
                ...
                sc = self._build_scene(...)
                sc["director_style"] = director_style
                raw_scenes.append(sc)
        elif dialogue:
            ...
            for i, line in enumerate(dialogue):
                ...
                sc = self._build_scene(...)
                sc["director_style"] = director_style
                raw_scenes.append(sc)
        else:
            sc = self._build_scene(...)
            sc["director_style"] = director_style
            raw_scenes.append(sc)

        for sc in raw_scenes:
            sc["duration"] = _estimate_duration(...)

        merged = self._merge_scenes(raw_scenes, self.max_duration)
        for i, sc in enumerate(merged):
            sc["scene_id"] = i + 1
        return merged[:max_scenes]
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_scene_composer.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add app/agents/scene_composer/scene_composer.py tests/test_scene_composer.py
git commit -m "feat: extend shot/movement pools and add director_style to compose()"
```

---

### Task 3: Enhance StoryboardAgent with style-aware action planning

**Files:**
- Modify: `app/agents/storyboard/storyboard.py`
- Test: `tests/test_storyboard.py`

**Interfaces:**
- Consumes: `DIRECTOR_STYLES`, `resolve_style()` from `app.agents.director_styles`
- Produces: `break_down_scene(scene, director_style=None)` now returns shots with `slow_motion`, `lens_flare`, `dutch_angle` fields; `_build_action_styled(scene, config)` method

- [ ] **Step 1: Write the failing tests**

```python
# Add after TestStoryboardInternalMethods in tests/test_storyboard.py

class TestStoryboardStyledAction:
    SAMPLE_ACTION_SCENE = {
        "duration": 10.0,
        "characters": [
            {"name": "Goku", "appearance": "orange gi", "expression": "determined", "position": "center"}
        ],
        "description": "Goku charges at Freezer with full speed, explosion in background",
        "camera": {"shot_type": "wide", "movement": "tracking", "lens": "35mm f/2.8"},
        "lighting": {"time_of_day": "day", "mood_lighting": "intense"},
        "dialogue": [{"character": "Goku", "text": "Freezer!"}],
        "transition": "cut"
    }

    def test_break_down_scene_accepts_director_style(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_ACTION_SCENE, director_style="michael_bay")
        assert len(shots) > 0

    def test_styled_action_shots_have_slow_motion_field(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_ACTION_SCENE, director_style="russo_brothers")
        for shot in shots:
            assert "slow_motion" in shot

    def test_styled_action_shots_have_lens_flare_field(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_ACTION_SCENE, director_style="michael_bay")
        for shot in shots:
            assert "lens_flare" in shot

    def test_styled_action_shots_have_director_style_field(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_ACTION_SCENE, director_style="sam_raimi")
        for shot in shots:
            assert shot["director_style"] == "sam_raimi"

    def test_michael_bay_action_uses_360_orbit(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_ACTION_SCENE, director_style="michael_bay")
        movements = [s["movement"] for s in shots]
        assert any("360_orbit" in m or "drone" in m or "crane" in m or "whip" in m for m in movements)

    def test_russo_brothers_action_uses_handheld(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_ACTION_SCENE, director_style="russo_brothers")
        movements = [s["movement"] for s in shots]
        assert any("handheld" in m or "steadicam" in m for m in movements)

    def test_no_style_falls_back_to_default_behavior(self):
        agent = StoryboardAgent()
        from tests.test_storyboard import TestStoryboardAgent
        shots_default = agent.break_down_scene(TestStoryboardAgent.SAMPLE_SCENE_LONG)
        shots_no_style = agent.break_down_scene(TestStoryboardAgent.SAMPLE_SCENE_LONG, director_style=None)
        assert len(shots_default) == len(shots_no_style)

    def test_sam_raimi_action_has_dutch_angle_field(self):
        agent = StoryboardAgent()
        shots = agent.break_down_scene(self.SAMPLE_ACTION_SCENE, director_style="sam_raimi")
        for shot in shots:
            assert "dutch_angle" in shot
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_storyboard.py::TestStoryboardStyledAction -v`
Expected: FAIL — missing director_style parameter, missing fields

- [ ] **Step 3: Update `break_down_scene()` to accept and use `director_style`**

```python
# Modify app/agents/storyboard/storyboard.py
from typing import Dict, Any, List
from app.agents.director_styles import DIRECTOR_STYLES, resolve_style


class StoryboardAgent:
    MAX_SHOT_DURATION = 8.0
    MIN_SHOT_DURATION = 4.0

    # existing constants...

    def break_down_scene(self, scene: Dict[str, Any], director_style: str = None) -> List[Dict[str, Any]]:
        duration = scene.get("duration", 8.0)
        characters = scene.get("characters", [])
        dialogue = scene.get("dialogue", [])
        mood = scene.get("lighting", {}).get("mood_lighting", "neutral")
        camera = scene.get("camera", {})
        description = scene.get("description", "")

        style = resolve_style(director_style, mood)
        config = DIRECTOR_STYLES.get(style)

        if config and self._is_action_scene(mood):
            return self._build_action_styled(scene, config, style)

        if duration <= 5.0:
            return [self._build_single_shot(scene, 0, duration, camera, ...)]

        # rest of existing logic...
```

- [ ] **Step 4: Add `_build_action_styled()` method**

```python
# Add to StoryboardAgent class
    def _build_action_styled(self, scene, config, style):
        duration = scene["duration"]
        characters = scene.get("characters", [])
        char_names = [c["name"] for c in characters]
        n_shots = min(4, max(3, int(duration / 3)))
        shot_duration = duration / n_shots
        shots = []

        preferred_shots = config["preferred_shot_types"]
        preferred_moves = config["preferred_movements"]
        slow_mo = config["slow_motion"]
        lens_flare = config.get("lens_flare", False)
        dutch_angle = config.get("dutch_angle", 0)

        for i in range(n_shots):
            shot_type = preferred_shots[i % len(preferred_shots)]
            movement = preferred_moves[i % len(preferred_moves)]

            is_slow_mo = slow_mo["enabled"] and i == n_shots - 1
            shot_dur = shot_duration
            if is_slow_mo:
                slow_factor = slow_mo.get("fps", 24) / 24
                shot_dur = min(shot_duration * slow_factor, slow_mo.get("max_duration", 4.0))

            start = i * shot_duration
            end = start + shot_dur

            description = f"{scene.get('description', '')} — {shot_type.replace('_', ' ')} ({movement.replace('_', ' ')})"
            focus = f"Action beat {i + 1}: {shot_type}"

            shots.append(self._build_shot_styled(
                scene, i + 1, shot_type, movement, start, end,
                description, char_names, focus, style,
                slow_mo=is_slow_mo, lens_flare=lens_flare, dutch_angle=dutch_angle,
            ))

        return shots

    def _build_shot_styled(self, scene, shot_number, shot_type, movement,
                           start_time, end_time, description, characters_in_frame,
                           focus, director_style, slow_mo=False, lens_flare=False,
                           dutch_angle=0):
        return {
            "shot_number": shot_number,
            "start_time": start_time,
            "end_time": end_time,
            "shot_type": shot_type,
            "movement": movement,
            "lens": scene.get("camera", {}).get("lens", "35mm f/2.8"),
            "description": description,
            "characters_in_frame": characters_in_frame,
            "focus": focus,
            "transition_in": "cut" if shot_number > 1 else scene.get("transition", "cut"),
            "transition_out": "cut",
            "slow_motion": slow_mo,
            "lens_flare": lens_flare,
            "dutch_angle": dutch_angle,
            "director_style": director_style,
        }
```

- [ ] **Step 5: Add `slow_motion`, `lens_flare`, `dutch_angle`, `director_style` to existing `_build_single_shot()` and `_build_shot()`**

```python
# In _build_single_shot() - add these fields at the end
    def _build_single_shot(self, scene, start_time, end_time, camera, trans_in, trans_out):
        return {
            # existing fields...
            "slow_motion": False,
            "lens_flare": False,
            "dutch_angle": 0,
            "director_style": None,
        }

# In _build_shot() - add these fields at the end
    def _build_shot(self, scene, shot_number, shot_type, movement, lens,
                    start_time, end_time, description, characters_in_frame,
                    focus, transition_in, transition_out):
        return {
            # existing fields...
            "slow_motion": False,
            "lens_flare": False,
            "dutch_angle": 0,
            "director_style": None,
        }
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `python -m pytest tests/test_storyboard.py -v`
Expected: All PASS (including new tests)

- [ ] **Step 7: Commit**

```bash
git add app/agents/storyboard/storyboard.py tests/test_storyboard.py
git commit -m "feat: add style-aware action planning to StoryboardAgent"
```

---

### Task 4: Enhance FlowPromptBuilderAgent with director sections

**Files:**
- Modify: `app/agents/flow_prompt_builder/flow_prompt_builder.py`
- Test: `tests/test_flow_prompt_builder.py`

**Interfaces:**
- Consumes: `DIRECTOR_STYLES` from `app.agents.director_styles`
- Produces: `build_prompts(scenes, character_mapping, director_style=None)` and `build_storyboard_prompts(scenes, character_mapping, storyboard_agent=None, director_style=None)` now include DIRECCIÓN section and slow-mo/flare annotations in shots

- [ ] **Step 1: Write the failing tests**

```python
# Add after TestFlowPromptBuilderStoryboard in tests/test_flow_prompt_builder.py

class TestFlowPromptBuilderDirector:
    SAMPLE_SCENES = [
        {
            "scene_id": 1,
            "duration": 8.0,
            "characters": [
                {"name": "Goku", "appearance": "orange gi", "expression": "determined", "position": "center"},
            ],
            "description": "Goku charges at Freezer with explosion",
            "camera": {"shot_type": "low_angle", "movement": "360_orbit", "lens": "35mm f/2.8"},
            "lighting": {"time_of_day": "sunset", "mood_lighting": "explosive"},
            "dialogue": [{"character": "Goku", "text": "Freezer!"}],
            "transition": "cut",
            "director_style": "michael_bay",
        }
    ]
    CHARACTER_MAPPING = {"Goku": "personaje_1"}

    def test_build_prompts_includes_director_section(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING, director_style="michael_bay")
        prompt_text = prompts[0]["prompt_text"]
        assert "DIRECCIÓN" in prompt_text

    def test_build_prompts_includes_style_name(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING, director_style="michael_bay")
        prompt_text = prompts[0]["prompt_text"]
        assert "Michael Bay" in prompt_text

    def test_storyboard_prompts_includes_slow_motion_flag(self):
        agent = FlowPromptBuilderAgent()
        from app.agents.storyboard.storyboard import StoryboardAgent
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent, director_style="michael_bay"
        )
        prompt_text = prompts[0]["prompt_text"]
        assert "SLOW-MO" in prompt_text

    def test_build_prompts_no_style_no_director_section(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        prompt_text = prompts[0]["prompt_text"]
        assert "DIRECCIÓN" not in prompt_text
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_flow_prompt_builder.py::TestFlowPromptBuilderDirector -v`
Expected: FAIL — missing director_style parameter in build_prompts

- [ ] **Step 3: Update `build_prompts()` to accept and include director_style**

```python
# Modify app/agents/flow_prompt_builder/flow_prompt_builder.py
from typing import Dict, Any, List, Optional
from app.agents.storyboard.storyboard import StoryboardAgent
from app.agents.director_styles import DIRECTOR_STYLES, resolve_style


class FlowPromptBuilderAgent:
    def build_prompts(self, scenes: List[Dict[str, Any]], character_mapping: Dict[str, str],
                      director_style: Optional[str] = None) -> List[Dict[str, Any]]:
        prompts = []
        start_time = 0.0
        for i, scene in enumerate(scenes):
            duration = scene.get("duration", 8.0)
            prompt_text = self._build_prompt(scene, character_mapping, i + 1, start_time, director_style)
            prompts.append({
                "scene_id": scene["scene_id"],
                "scene_number": i + 1,
                "duration": duration,
                "prompt_text": prompt_text
            })
            start_time += duration
        return prompts

    def _build_prompt(self, scene: Dict[str, Any], character_mapping: Dict[str, str],
                      scene_num: int, start_time: float,
                      director_style: Optional[str] = None) -> str:
        # ... existing code ...

        # After SPECS TÉCNICAS section, add DIRECCIÓN section
        # Find the ANTI-ALUCINACIÓN line and insert before it

        lines.append("")
        style = resolve_style(director_style, scene.get("lighting", {}).get("mood_lighting", ""))
        config = DIRECTOR_STYLES.get(style)
        if config:
            style_name = style.replace("_", " ").title()
            lines.append("DIRECCIÓN:")
            lines.append(f"  - Estilo: {style_name}")
            if config["slow_motion"]["enabled"]:
                for shot in scene.get("storyboard_shots", []):
                    if shot.get("slow_motion"):
                        fps = config["slow_motion"]["fps"]
                        lines.append(f"  - Slow motion: SHOT {shot['shot_number']} ({shot.get('real_duration', 2.0):.1f}s a {fps}fps)")
            if config.get("lens_flare"):
                lines.append("  - Flares: Activados (anamórficos)")
            if config.get("dutch_angle", 0) > 0:
                lines.append(f"  - Dutch angle: {config['dutch_angle']}°")
            if config.get("color_grading"):
                grading_name = config["color_grading"].replace("_", " ").title()
                lines.append(f"  - Color grading: {grading_name}")
            lines.append("")

        # ... rest of existing code ...
```

- [ ] **Step 4: Update `build_storyboard_prompts()` similarly**

```python
    def build_storyboard_prompts(self, scenes, character_mapping, storyboard_agent=None,
                                  director_style=None):
        if storyboard_agent is None:
            storyboard_agent = StoryboardAgent()

        prompts = []
        start_time = 0.0
        for i, scene in enumerate(scenes):
            duration = scene.get("duration", 8.0)
            shots = storyboard_agent.break_down_scene(scene, director_style=director_style)
            prompt_text = self._build_hybrid_prompt(scene, shots, character_mapping, i + 1, start_time, director_style)
            prompts.append({
                "scene_id": scene["scene_id"],
                "scene_number": i + 1,
                "duration": duration,
                "prompt_text": prompt_text
            })
            start_time += duration
        return prompts
```

Update `_build_hybrid_prompt()` signature and add slow-mo/flare lines in shot blocks:

```python
    def _build_hybrid_prompt(self, scene, shots, character_mapping,
                              scene_num, start_time, director_style=None):
        # ... existing code ...
        
        # In the shot rendering section, after the focus line, add:
        if shot.get("slow_motion"):
            lines.append(f"║  SLOW-MO: ✅ ({shot.get('duration', 2.0):.1f}s)")
        if shot.get("lens_flare"):
            lines.append("║  FLARE: ✅")
        if shot.get("dutch_angle", 0) > 0:
            lines.append(f"║  DUTCH ANGLE: {shot['dutch_angle']}°")
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_flow_prompt_builder.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add app/agents/flow_prompt_builder/flow_prompt_builder.py tests/test_flow_prompt_builder.py
git commit -m "feat: add director-style sections to FlowPromptBuilder prompts"
```

---

### Task 5: Wire DirectorAgent to pass director_style through pipeline

**Files:**
- Modify: `app/agents/director/director.py`

**Interfaces:**
- Consumes: `director_style` from `options` dict
- Produces: Passes `director_style` to `SceneComposerAgent.compose()`, `StoryboardAgent.break_down_scene()`, `FlowPromptBuilderAgent.build_prompts()`/`build_storyboard_prompts()`

- [ ] **Step 1: Read current director.py to understand existing flow**

```bash
cat app/agents/director/director.py
```

- [ ] **Step 2: Modify `process_manga_request()` to extract `director_style` from options and pass it**

```python
# Modify app/agents/director/director.py

    def process_manga_request(self, manga_data: Dict[str, Any], options: Dict[str, Any] = None) -> Dict[str, Any]:
        options = options or {}
        director_style = options.get("director_style")
        # ... existing code ...
        
        analysis = self.manga_analyzer.analyze(image_base64, filename, manga_series)
        scenes = self.scene_composer.compose(analysis, max_scenes=options.get("max_scenes", 5), director_style=director_style)
        
        # When passing to storyboard / flow builder:
        # ... existing code for character manager, environment manager ...
        
        for scene in scenes:
            shots = self.storyboard.break_down_scene(scene, director_style=director_style)
            scene["storyboard_shots"] = shots
        
        prompts = self.flow_builder.build_prompts(scenes, character_mapping, director_style=director_style)
        
        # ... rest of existing code ...
```

(Adjust based on actual director.py structure after reading it)

- [ ] **Step 3: Run existing tests to verify nothing broke**

Run: `python -m pytest tests/test_director.py -v`
Expected: All PASS

- [ ] **Step 4: Commit**

```bash
git add app/agents/director/director.py
git commit -m "feat: wire director_style through DirectorAgent pipeline"
```

---

### Task 6: Final verification

- [ ] **Step 1: Run all tests**

Run: `python -m pytest tests/ -v --tb=short`
Expected: All tests pass

- [ ] **Step 2: Commit any outstanding changes**

```bash
git add -A
git commit -m "chore: final adjustments after director styles implementation"
```
