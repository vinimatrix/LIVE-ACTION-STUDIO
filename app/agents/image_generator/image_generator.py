from typing import Dict, Any
from pathlib import Path
import uuid
from app.core.config import settings


class ImageGeneratorAgent:
    def __init__(self):
        self.settings = settings
        self.output_dir = Path("./generated_images")
        self.output_dir.mkdir(exist_ok=True)

    def generate_image(self, prompt: str, scene_id: int = None) -> Dict[str, Any]:
        file_name = f"scene_{scene_id or 'unknown'}_{uuid.uuid4().hex[:8]}.png"
        file_path = self.output_dir / file_name

        with open(file_path, "w") as f:
            f.write(f"Simulated image data for prompt: {prompt}")

        return {
            "file_path": str(file_path),
            "file_size": file_path.stat().st_size,
            "mime_type": "image/png",
            "prompt_used": prompt,
            "generation_params": {
                "model": "SDXL",
                "steps": 30,
                "cfg_scale": 7.5
            }
        }
