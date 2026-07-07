import os
import pytest
from app.agents.image_generator.image_generator import ImageGeneratorAgent


def test_image_generator_initialization():
    agent = ImageGeneratorAgent()
    assert agent is not None
    assert hasattr(agent, 'output_dir')


def test_generate_image(mocker):
    import urllib.error
    mocker.patch('urllib.request.urlopen', side_effect=urllib.error.URLError("Mocked Connection Refused"))

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


def test_get_workflow_returns_dict():
    agent = ImageGeneratorAgent()
    workflow = agent.get_workflow("test prompt")
    assert isinstance(workflow, dict)


def test_get_workflow_has_all_required_nodes():
    agent = ImageGeneratorAgent()
    workflow = agent.get_workflow("test prompt")
    for node_id in ("3", "4", "5", "6", "7", "8", "9"):
        assert node_id in workflow, f"Missing node {node_id}"


def test_get_workflow_contains_prompt_text():
    agent = ImageGeneratorAgent()
    prompt = "A beautiful landscape with mountains"
    workflow = agent.get_workflow(prompt)
    assert workflow["6"]["inputs"]["text"] == prompt


def test_get_workflow_default_seed():
    agent = ImageGeneratorAgent()
    workflow = agent.get_workflow("test")
    assert workflow["3"]["inputs"]["seed"] == 12345


def test_get_workflow_resolution():
    agent = ImageGeneratorAgent()
    workflow = agent.get_workflow("test")
    assert workflow["5"]["inputs"]["width"] == 512
    assert workflow["5"]["inputs"]["height"] == 512


def test_get_workflow_k_sampler_config():
    agent = ImageGeneratorAgent()
    workflow = agent.get_workflow("test")
    assert workflow["3"]["inputs"]["steps"] == 20
    assert workflow["3"]["inputs"]["cfg"] == 8
