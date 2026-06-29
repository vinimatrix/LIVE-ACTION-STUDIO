import os
import pytest
from app.agents.music_generator.music_generator import MusicGeneratorAgent


def test_music_generator_initialization():
    agent = MusicGeneratorAgent()
    assert agent is not None
    assert hasattr(agent, 'output_dir')


def test_generate_music():
    agent = MusicGeneratorAgent()
    prompt = "Uplifting orchestral score"
    result = agent.generate_music(prompt, duration=10.0)

    assert "file_path" in result
    assert result["file_path"].endswith(".mp3")
    assert result["mime_type"] == "audio/mp3"
    assert result["prompt_used"] == prompt
    assert result["duration"] == 10.0
    assert "generation_params" in result

    if os.path.exists(result["file_path"]):
        os.remove(result["file_path"])
