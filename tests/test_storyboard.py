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
        "duration": 8.0,
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
        shots = agent.break_down_scene(self.SAMPLE_SCENE_SHORT)
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
        scene = {
            "duration": 16.0,
            "characters": [
                {"name": "Goku", "expression": "angry"},
                {"name": "Freezer", "expression": "smirking"}
            ],
            "dialogue": [
                {"character": "Goku", "text": "Freezer!"},
                {"character": "Freezer", "text": "Foolish Saiyan."}
            ],
            "camera": {"shot_type": "wide", "movement": "static", "lens": "24mm f/4"},
            "lighting": {"time_of_day": "day", "mood_lighting": "tense"},
            "transition": "cut"
        }
        shots = agent.break_down_scene(scene)
        shot_types = [s["shot_type"] for s in shots]
        assert "over-the-shoulder" in shot_types


class TestStoryboardInternalMethods:
    def test_is_action_scene_returns_true_for_known_moods(self):
        agent = StoryboardAgent()
        assert agent._is_action_scene("intense") is True
        assert agent._is_action_scene("epic") is True
        assert agent._is_action_scene("dramatic") is True
        assert agent._is_action_scene("explosive") is True

    def test_is_action_scene_returns_false_for_unknown_moods(self):
        agent = StoryboardAgent()
        assert agent._is_action_scene("tense") is False
        assert agent._is_action_scene("calm") is False
        assert agent._is_action_scene("neutral") is False
        assert agent._is_action_scene("sad") is False
        assert agent._is_action_scene("peaceful") is False

    def test_is_action_scene_empty_string(self):
        agent = StoryboardAgent()
        assert agent._is_action_scene("") is False

    def test_build_dialogue_one_returns_two_shots(self):
        agent = StoryboardAgent()
        scene = {
            "duration": 8.0,
            "characters": [
                {"name": "Goku", "appearance": "orange gi", "expression": "angry", "position": "center"}
            ],
            "description": "Goku speaks",
            "camera": {"shot_type": "medium", "movement": "static", "lens": "35mm f/2.8"},
            "lighting": {"time_of_day": "day", "mood_lighting": "neutral"},
            "dialogue": [{"character": "Goku", "text": "I will defeat you!"}],
            "transition": "cut"
        }
        shots = agent._build_dialogue_one(scene)
        assert len(shots) == 2

    def test_build_dialogue_one_first_shot_medium(self):
        agent = StoryboardAgent()
        scene = {
            "duration": 8.0,
            "characters": [{"name": "Goku", "expression": "angry"}],
            "description": "Goku speaks",
            "dialogue": [{"character": "Goku", "text": "I will defeat you!"}],
        }
        shots = agent._build_dialogue_one(scene)
        assert shots[0]["shot_type"] == "medium"

    def test_build_dialogue_one_second_shot_close_up(self):
        agent = StoryboardAgent()
        scene = {
            "duration": 8.0,
            "characters": [{"name": "Goku", "expression": "angry"}],
            "description": "Goku speaks",
            "dialogue": [{"character": "Goku", "text": "I will defeat you!"}],
        }
        shots = agent._build_dialogue_one(scene)
        assert shots[1]["shot_type"] == "close-up"

    def test_build_dialogue_one_times_are_continuous(self):
        agent = StoryboardAgent()
        scene = {
            "duration": 8.0,
            "characters": [{"name": "Goku", "expression": "angry"}],
            "description": "Goku speaks",
            "dialogue": [{"character": "Goku", "text": "I will defeat you!"}],
        }
        shots = agent._build_dialogue_one(scene)
        assert shots[0]["start_time"] == 0.0
        assert shots[0]["end_time"] == shots[1]["start_time"]
        assert shots[1]["end_time"] == 8.0

    def test_build_dialogue_one_second_shot_has_character_name(self):
        agent = StoryboardAgent()
        scene = {
            "duration": 8.0,
            "characters": [{"name": "Goku", "expression": "angry"}],
            "description": "Goku speaks",
            "dialogue": [{"character": "Goku", "text": "I will defeat you!"}],
        }
        shots = agent._build_dialogue_one(scene)
        assert "Goku" in shots[1]["description"]
