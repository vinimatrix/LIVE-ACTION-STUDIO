# AI Live Action Studio MVP

A platform to transform manga pages into live-action video clips using AI agents.

## Architecture

Hybrid modular architecture with Director agent orchestrating specialized agents:
- Screenwriter Agent: Converts manga to cinematic screenplay
- Character Manager: Maintains character consistency
- Environment Manager: Handles locations and settings
- Cinematography Agent: Plans camera movements and shots
- Prompt Builder: Creates optimized prompts for AI generation
- Generation Agents: Create images, video, voice, music, effects
- Editor Agent: Assembles final video

## Technology Stack

- Python 3.11+ with FastAPI
- Celery + Redis for task queuing
- PostgreSQL for data storage
- MinIO for asset storage
- Ollama for LLM inference
- ComfyUI/SDXL for image generation
- FFmpeg for video processing

## Setup

```bash
# Clone repository
git clone <repository-url>
cd ai-live-action-studio

# Install dependencies
pip install -r requirements.txt

# Start services
docker-compose up -d

# Run tests
pytest
```