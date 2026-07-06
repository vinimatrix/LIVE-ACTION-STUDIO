from typing import Dict, Any
from pathlib import Path
import uuid
import json
import urllib.request
import urllib.error
import time
from app.core.config import settings


class ImageGeneratorAgent:
    def __init__(self):
        self.settings = settings
        self.output_dir = Path("./generated_images")
        self.output_dir.mkdir(exist_ok=True)
        self.comfyui_url = getattr(self.settings, 'COMFYUI_URL', "http://127.0.0.1:8188")
        
    def get_workflow(self, prompt: str):
        # A basic SD 1.5 workflow mapping for simplicity.
        return {
            "3": {"class_type": "KSampler", "inputs": {"cfg": 8, "denoise": 1, "latent_image": ["5", 0], "model": ["4", 0], "negative": ["7", 0], "positive": ["6", 0], "sampler_name": "euler", "scheduler": "normal", "seed": 12345, "steps": 20}},
            "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "v1-5-pruned-emaonly.safetensors"}},
            "5": {"class_type": "EmptyLatentImage", "inputs": {"batch_size": 1, "height": 512, "width": 512}},
            "6": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["4", 1], "text": prompt}},
            "7": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["4", 1], "text": "bad quality, blurry"}},
            "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
            "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": "ai_studio", "images": ["8", 0]}}
        }

    def generate_image(self, prompt: str, scene_id: int = None) -> Dict[str, Any]:
        file_name = f"scene_{scene_id or 'unknown'}.png"
        file_path = self.output_dir / file_name

        workflow = self.get_workflow(prompt)
        data = json.dumps({"prompt": workflow}).encode('utf-8')
        req = urllib.request.Request(f"{self.comfyui_url}/prompt", data=data)
        
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                result = json.loads(response.read())
                prompt_id = result['prompt_id']
                
            # Poll for completion
            while True:
                time.sleep(2)
                hist_req = urllib.request.Request(f"{self.comfyui_url}/history/{prompt_id}")
                with urllib.request.urlopen(hist_req, timeout=5) as hist_res:
                    history = json.loads(hist_res.read())
                    if prompt_id in history:
                        outputs = history[prompt_id]['outputs']
                        for node_id, output_data in outputs.items():
                            if 'images' in output_data:
                                img_info = output_data['images'][0]
                                filename = img_info['filename']
                                subfolder = img_info.get('subfolder', '')
                                
                                # Download the image
                                img_url = f"{self.comfyui_url}/view?filename={filename}&subfolder={subfolder}"
                                urllib.request.urlretrieve(img_url, file_path)
                                break
                        break

            generation_params = {"model": "SD", "steps": 20, "cfg_scale": 8}
            
        except urllib.error.URLError as e:
            # Fallback to simulated mapping if ComfyUI isn't running
            print(f"ComfyUI no está disponible o hubo un error: {e}. Generando imagen simulada.")
            if not file_path.exists():
                from PIL import Image, ImageDraw
                img = Image.new('RGB', (1024, 1024), color=(20, 24, 38))
                draw = ImageDraw.Draw(img)
                draw.text((50, 450), f"IMAGE GENERATOR FALLBACK\nScene ID: {scene_id or 'unknown'}\nPrompt: {prompt[:80]}...", fill=(200, 200, 255))
                img.save(file_path, "PNG")
            else:
                print(f"Usando imagen pre-existente: {file_path}")
            generation_params = {"model": "Fallback", "steps": 30, "cfg_scale": 7.5}

        return {
            "file_path": str(file_path),
            "file_size": file_path.stat().st_size if file_path.exists() else 0,
            "mime_type": "image/png",
            "prompt_used": prompt,
            "generation_params": generation_params
        }
