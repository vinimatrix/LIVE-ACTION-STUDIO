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

- Python 3.14 with FastAPI
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

## API Endpoints

- POST `/api/v1/manga/process` - Start processing a manga page
- GET `/api/v1/manga/status/{job_id}` - Get job status
- GET `/api/v1/manga/result/{job_id}` - Get job result (when completed)
- GET `/api/v1/jobs/` - List recent jobs
- GET `/api/v1/assets/{asset_id}` - Get specific asset

## Features

- [x] Project structure and basic API
- [x] Database models for characters, environments, scenes, assets, jobs
- [x] Director agent for workflow orchestration
- [x] Screenwriter agent for screenplay generation
- [x] Character manager for consistency
- [x] Environment manager for location handling
- [x] Prompt builder for AI generation prompts
- [x] Image generation agent (simulated)
- [x] Video generation agent (simulated)
- [x] Voice generation agent (simulated)
- [x] Music generation agent (simulated)
- [x] FX generation agent (simulated)
- [x] Editor agent for final assembly (simulated)
- [x] API endpoints for job management
- [ ] Frontend interface (optional)
- [ ] Real AI model integrations (future work)
- [ ] Advanced editing features (color grading, transitions, etc.)
- [ ] User authentication and authorization
- [ ] WebSocket for real-time job updates
- [ ] Support for full manga chapters
- [ ] Multi-language support (dubbing/subtitles)

## License

MIT

## Contributing

See CONTRIBUTING.md
