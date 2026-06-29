import os
import pytest
from app.agents.voice_generator.voice_generator import VoiceGeneratorAgent


def test_voice_generator_initialization():
    agent = VoiceGeneratorAgent()
    assert agent is not None
    assert hasattr(agent, 'output_dir')


def test_generate_voice():
    agent = VoiceGeneratorAgent()
    prompt = "Hello, this is a test voice"
    result = agent.generate_voice(prompt, character_id=1)

    assert "file_path" in result
    assert result["file_path"].endswith(".wav")
    assert result["mime_type"] == "audio/wav"
    assert result["prompt_used"] == prompt
    assert result["character_id"] == 1
    assert "generation_params" in result

    if os.path.exists(result["file_path"]):
        os.remove(result["file_path"])
