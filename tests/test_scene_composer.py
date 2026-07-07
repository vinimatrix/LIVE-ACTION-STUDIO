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


from app.agents.scene_composer.scene_composer import (
    _estimate_duration, _normalize, _tokens_of, MOOD_SPEED
)


class TestSceneComposerInternalMethods:
    def test_estimate_duration_base_only(self):
        d = _estimate_duration([], "", "neutral")
        assert 3.0 <= d <= 10.0

    def test_estimate_duration_with_dialogue(self):
        d = _estimate_duration(["Hello", "World"], "", "neutral")
        assert d > 3.0

    def test_estimate_duration_with_action(self):
        d = _estimate_duration([], "running", "neutral")
        assert d == 5.0

    def test_estimate_duration_speed_mood_tenso(self):
        d = _estimate_duration([], "", "tenso")
        neutral = _estimate_duration([], "", "neutral")
        neutral_raw = 3.0
        expected = max(3.0, min(10.0, neutral_raw * MOOD_SPEED["tenso"]))
        assert d == expected

    def test_estimate_duration_speed_mood_calma(self):
        d = _estimate_duration([], "", "calma")
        neutral = _estimate_duration([], "", "neutral")
        neutral_raw = 3.0
        expected = max(3.0, min(10.0, neutral_raw * MOOD_SPEED["calma"]))
        assert d == expected

    def test_estimate_duration_clamps_minimum(self):
        d = _estimate_duration([], "", "tenso")
        assert d >= 3.0

    def test_estimate_duration_clamps_maximum(self):
        d = _estimate_duration(["A"] * 20, "", "calma")
        assert d <= 10.0

    def test_estimate_duration_unknown_mood_defaults_to_1(self):
        d = _estimate_duration([], "", "unknown_mood_xyz")
        assert d == 3.0

    def test_estimate_duration_mood_with_accent_normalized(self):
        d_accent = _estimate_duration([], "", "sombrío")
        d_no_accent = _estimate_duration([], "", "sombrío")
        assert d_accent == d_no_accent

    def test_normalize_lowercases(self):
        assert _normalize("HELLO") == "hello"

    def test_normalize_removes_accents(self):
        assert _normalize("canción") == "cancion"
        assert _normalize("épico") == "epico"
        assert _normalize("motivación") == "motivacion"
        assert _normalize("ímpetu") == "impetu"
        assert _normalize("único") == "unico"
        assert _normalize("niño") == "nino"

    def test_normalize_empty_string(self):
        assert _normalize("") == ""

    def test_normalize_numbers_and_symbols(self):
        assert _normalize("¡Hola! ¿Qué tal? 123") == "¡hola! ¿que tal? 123"

    def test_tokens_of_basic(self):
        scene = {"description": "Hello world", "dialogue": [{"character": "A", "text": "Hi"}]}
        assert _tokens_of(scene) == 11 + 2

    def test_tokens_of_no_dialogue(self):
        scene = {"description": "Hello world", "dialogue": []}
        assert _tokens_of(scene) == 11

    def test_tokens_of_multiple_dialogues(self):
        scene = {"description": "Test", "dialogue": [{"text": "Hello"}, {"text": "World"}]}
        assert _tokens_of(scene) == 4 + 5 + 5

    def test_tokens_of_empty_description(self):
        scene = {"description": "", "dialogue": [{"text": "Hi"}]}
        assert _tokens_of(scene) == 2


class TestSceneComposerMerge:
    def test_merge_scenes_empty_returns_empty_list(self):
        agent = SceneComposerAgent()
        assert agent._merge_scenes([], 10.0) == []

    def test_merge_scenes_single_scene(self):
        agent = SceneComposerAgent()
        scenes = [{"duration": 5.0, "dialogue": [{"text": "Hi"}], "description": "Test"}]
        merged = agent._merge_scenes(scenes, 10.0)
        assert len(merged) == 1

    def test_merge_scenes_combines_within_limit(self):
        agent = SceneComposerAgent()
        scenes = [
            {"duration": 4.0, "dialogue": [{"text": "A"}], "description": "First"},
            {"duration": 4.0, "dialogue": [{"text": "B"}], "description": "Second"},
        ]
        merged = agent._merge_scenes(scenes, 10.0)
        assert len(merged) == 1
        assert merged[0]["duration"] == 8.0
        assert len(merged[0]["dialogue"]) == 2

    def test_merge_scenes_does_not_exceed_max_total(self):
        agent = SceneComposerAgent()
        scenes = [
            {"duration": 6.0, "dialogue": [{"text": "A"}], "description": "First"},
            {"duration": 6.0, "dialogue": [{"text": "B"}], "description": "Second"},
        ]
        merged = agent._merge_scenes(scenes, 10.0)
        assert merged[0]["duration"] <= 10.0

    def test_merge_scenes_separates_when_over_limit(self):
        agent = SceneComposerAgent()
        scenes = [
            {"duration": 6.0, "dialogue": [{"text": "A"}], "description": "First"},
            {"duration": 6.0, "dialogue": [{"text": "B"}], "description": "Second"},
        ]
        merged = agent._merge_scenes(scenes, 7.0)
        assert len(merged) == 2

    def test_merge_scenes_description_combines(self):
        agent = SceneComposerAgent()
        scenes = [
            {"duration": 4.0, "dialogue": [], "description": "First scene"},
            {"duration": 4.0, "dialogue": [], "description": "Second scene"},
        ]
        merged = agent._merge_scenes(scenes, 10.0)
        assert "First scene" in merged[0]["description"]
        assert "Second scene" in merged[0]["description"]

    def test_merge_scenes_truncates_long_description(self):
        agent = SceneComposerAgent()
        long_a = "A" * 500
        long_b = "B" * 500
        scenes = [
            {"duration": 4.0, "dialogue": [], "description": long_a},
            {"duration": 4.0, "dialogue": [], "description": long_b},
        ]
        merged = agent._merge_scenes(scenes, 10.0)
        assert len(merged[0]["description"]) <= 800


class TestSceneComposerSelectors:
    def test_select_shot_cycles_through_options(self):
        agent = SceneComposerAgent()
        shots = [agent._select_shot(i, 10) for i in range(10)]
        assert shots[0] == "wide"
        assert shots[1] == "medium"
        assert shots[2] == "close-up"
        assert shots[3] == "over-the-shoulder"
        assert shots[4] == "extreme-close-up"
        assert shots[5] == "wide"

    def test_select_movement_cycles_through_options(self):
        agent = SceneComposerAgent()
        moves = [agent._select_movement(i) for i in range(10)]
        assert moves[0] == "static"
        assert moves[1] == "dolly"
        assert moves[2] == "pan"
        assert moves[3] == "tilt"
        assert moves[4] == "steadicam"
        assert moves[5] == "static"

    def test_build_scene_has_all_required_keys(self):
        agent = SceneComposerAgent()
        scene = agent._build_scene(1, [{"name": "Goku"}], "Planet", "Fighting", [], "epic", "wide", "dolly")
        assert "scene_id" in scene
        assert "duration" in scene
        assert "characters" in scene
        assert "description" in scene
        assert "camera" in scene
        assert "lighting" in scene
        assert "dialogue" in scene
        assert "transition" in scene

    def test_build_scene_with_character_dicts(self):
        agent = SceneComposerAgent()
        chars = [{"name": "Goku", "appearance": "orange gi", "expression": "angry", "position": "center"}]
        scene = agent._build_scene(1, chars, "Planet", "Fighting", [], "epic", "wide", "dolly")
        assert scene["characters"][0]["name"] == "Goku"
        assert scene["characters"][0]["appearance"] == "orange gi"
        assert scene["characters"][0]["expression"] == "angry"

    def test_build_scene_lighting_sunset_detection(self):
        agent = SceneComposerAgent()
        scene = agent._build_scene(1, [], "sunset on the beach", "", [], "calma", "wide", "static")
        assert scene["lighting"]["time_of_day"] == "sunset"

    def test_build_scene_lighting_default_day(self):
        agent = SceneComposerAgent()
        scene = agent._build_scene(1, [], "Forest", "", [], "neutral", "wide", "static")
        assert scene["lighting"]["time_of_day"] == "day"

    def test_build_scene_transition_fade_in_first(self):
        agent = SceneComposerAgent()
        scene = agent._build_scene(1, [], "Forest", "", [], "neutral", "wide", "static")
        assert scene["transition"] == "fade_in"

    def test_build_scene_transition_cut_after_first(self):
        agent = SceneComposerAgent()
        scene = agent._build_scene(2, [], "Forest", "", [], "neutral", "wide", "static")
        assert scene["transition"] == "cut"
