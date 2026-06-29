import os
import pytest
from app.agents.fx_generator.fx_generator import FXGeneratorAgent


def test_fx_generator_initialization():
    agent = FXGeneratorAgent()
    assert agent is not None
    assert hasattr(agent, 'output_dir')


def test_generate_effect():
    agent = FXGeneratorAgent()
    prompt = "Explosion with smoke"
    result = agent.generate_effect(prompt, duration=3.0)

    assert "file_path" in result
    assert result["file_path"].endswith(".mov")
    assert result["mime_type"] == "video/quicktime"
    assert result["prompt_used"] == prompt
    assert result["duration"] == 3.0
    assert "generation_params" in result

    if os.path.exists(result["file_path"]):
        os.remove(result["file_path"])
