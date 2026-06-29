import os
import pytest
from app.agents.video_generator.video_generator import VideoGeneratorAgent


def test_video_generator_initialization():
    agent = VideoGeneratorAgent()
    assert agent is not None
    assert hasattr(agent, 'output_dir')


def test_generate_video():
    agent = VideoGeneratorAgent()
    image_path = "/fake/image.png"
    prompt = "A beautiful landscape"
    result = agent.generate_video(image_path, prompt, duration=4.5)

    assert "file_path" in result
    assert result["file_path"].endswith(".mp4")
    assert result["mime_type"] == "video/mp4"
    assert result["image_used"] == image_path
    assert result["prompt_used"] == prompt
    assert result["duration"] == 4.5
    assert "generation_params" in result

    if os.path.exists(result["file_path"]):
        os.remove(result["file_path"])
