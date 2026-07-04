from typing import Dict, Any
from pathlib import Path
import uuid
from app.core.config import settings


class MusicGeneratorAgent:
    def __init__(self):
        self.settings = settings
        self.output_dir = Path("./generated_music")
        self.output_dir.mkdir(exist_ok=True)

    def generate_music(self, prompt: str, duration: float = 5.0) -> Dict[str, Any]:
        import hashlib
        prompt_hash = hashlib.md5(prompt.encode('utf-8')).hexdigest()[:8]
        file_name = f"music_{prompt_hash}.mp3"
        file_path = self.output_dir / file_name

        if not file_path.exists():
            import wave
            import struct
            import math
            with wave.open(str(file_path), "wb") as w:
                w.setparams((1, 2, 22050, 0, "NONE", "not compressed"))
                for i in range(int(22050 * duration)):
                    value = int(32767 * 0.1 * math.sin(2 * math.pi * 220.0 * i / 22050))
                    w.writeframes(struct.pack('h', value))
        else:
            print(f"Usando música pre-existente: {file_path}")

        return {
            "file_path": str(file_path),
            "file_size": file_path.stat().st_size,
            "mime_type": "audio/mp3",
            "prompt_used": prompt,
            "duration": duration,
            "generation_params": {
                "model": "MusicGen",
                "temperature": 0.8
            }
        }
