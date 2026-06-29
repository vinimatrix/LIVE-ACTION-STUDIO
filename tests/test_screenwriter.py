import pytest
from app.agents.screenwriter.screenwriter import ScreenwriterAgent


def test_screenwriter_initialization():
    agent = ScreenwriterAgent()
    assert agent is not None


def test_process_scene():
    agent = ScreenwriterAgent()
    scene_data = {
        "scene_id": 1,
        "description": "A character stands on a hill",
        "duration": 5.0
    }

    result = agent.process_scene(scene_data)

    assert result["scene_id"] == 1
    assert len(result["dialogue"]) == 1
    assert result["dialogue"][0]["character"] == "Narrator"
    assert len(result["actions"]) == 2
    assert "camera_notes" in result
