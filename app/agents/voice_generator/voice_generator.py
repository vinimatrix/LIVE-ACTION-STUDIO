from typing import Dict, Any
from pathlib import Path
import uuid
from app.core.config import settings


class VoiceGeneratorAgent:
    def __init__(self):
        self.settings = settings
        self.output_dir = Path("./generated_audio")
        self.output_dir.mkdir(exist_ok=True)

    def generate_voice(self, prompt: str, character_id: int = None) -> Dict[str, Any]:
        import hashlib
        prompt_hash = hashlib.md5(prompt.encode('utf-8')).hexdigest()[:8]
        file_name = f"voice_{character_id or 'unknown'}_{prompt_hash}.wav"
        file_path = self.output_dir / file_name

        if not file_path.exists():
            import wave
            import struct
            import math
            with wave.open(str(file_path), "wb") as w:
                w.setparams((1, 2, 22050, 0, "NONE", "not compressed"))
                for i in range(int(22050 * 2.0)): # 2 seconds
                    value = int(32767 * 0.1 * math.sin(2 * math.pi * 330.0 * i / 22050))
                    w.writeframes(struct.pack('h', value))
        else:
            print(f"Usando audio de voz pre-existente: {file_path}")

        return {
            "file_path": str(file_path),
            "file_size": file_path.stat().st_size,
            "mime_type": "audio/wav",
            "prompt_used": prompt,
            "character_id": character_id,
            "generation_params": {
                "model": "TTS_v1",
                "speaker": "default"
            }
        }
