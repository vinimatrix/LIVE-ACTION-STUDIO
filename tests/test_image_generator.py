import os
import pytest
from app.agents.image_generator.image_generator import ImageGeneratorAgent


def test_image_generator_initialization():
    agent = ImageGeneratorAgent()
    assert agent is not None
    assert hasattr(agent, 'output_dir')


def test_generate_image():
    agent = ImageGeneratorAgent()
    prompt = "A beautiful landscape"
    result = agent.generate_image(prompt, scene_id=1)

    assert "file_path" in result
    assert result["file_path"].endswith(".png")
    assert result["mime_type"] == "image/png"
    assert result["prompt_used"] == prompt
    assert "generation_params" in result

    if os.path.exists(result["file_path"]):
        os.remove(result["file_path"])
