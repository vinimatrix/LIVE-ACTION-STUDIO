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


def test_adapt_to_latin_spanish():
    agent = ScreenwriterAgent()
    assert agent.adapt_to_latin_spanish("¡¿Por qué no me entendéis?!") == "¡¿Por qué no me entienden?!"
    assert agent.adapt_to_latin_spanish("¿Qué os ha parecido?") == "¿Qué les ha parecido?"
    assert agent.adapt_to_latin_spanish("Tuvo la caradura de mentir.") == "Tuvo el descaro de mentir."


def test_process_scene_with_dialogue():
    agent = ScreenwriterAgent()
    scene_data = {
        "scene_id": 2,
        "description": "Scene 2",
        "duration": 8.0,
        "dialogue": [
            {"character": "Sarada", "text": "¡Ya os lo he explicado!", "emotion": "angry"}
        ]
    }
    result = agent.process_scene(scene_data)
    assert result["scene_id"] == 2
    assert len(result["dialogue"]) == 1
    assert result["dialogue"][0]["character"] == "Sarada"
    assert result["dialogue"][0]["text"] == "¡Ya se lo he explicado!"

