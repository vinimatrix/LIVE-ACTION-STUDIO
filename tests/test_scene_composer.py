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
