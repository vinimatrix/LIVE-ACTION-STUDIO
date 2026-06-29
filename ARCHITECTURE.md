# AI Live Action Studio Architecture

## Overview

The AI Live Action Studio follows a hybrid modular architecture with a central Director agent orchestrating specialized agent modules.

## Core Components

1. **Director Agent** - Workflow orchestration and scene breakdown
2. **Screenwriter Agent** - Converts scenes to cinematic screenplays
3. **Character Manager** - Ensures character consistency and provides references
4. **Environment Manager** - Manages locations and environmental factors
5. **Cinematography Agent** - Plans camera movements and shot types
6. **Prompt Builder** - Creates optimized prompts for AI generation models
7. **Generation Agents** - Create images, video, voice, music, and effects
8. **Editor Agent** - Assembles final video with synchronization and color grading

## Data Flow

1. Manga input -> Director (scene breakdown)
2. Director -> Screenwriter (screenplay generation)
3. Screenwriter -> Character/Environment Managers (consistency)
4. All -> Prompt Builder (prompt creation)
5. Prompt Builder -> Generation Agents (asset creation)
6. Generation Agents -> Editor (final assembly)
7. Editor -> Final output

## Communication

- Internal task queue (Celery with Redis) for agent-to-agent communication
- REST API for external interactions
- Database (PostgreSQL) for persistent state
- Object storage (MinIO) for media assets

## Technology Stack

- Backend: Python 3.14, FastAPI
- Task Queue: Celery + Redis
- Database: PostgreSQL (SQLite for testing)
- Storage: MinIO (S3-compatible)
- AI Models: Ollama (LLMs), ComfyUI/SDXL (images), Kling/Veo (video), TTS (voice), MusicGen (music)
- Video Processing: FFmpeg
- Frontend: React (optional)

## Extensibility

New agents can be added by:
1. Creating a new agent module in `app/agents/`
2. Implementing the agent interface
3. Registering Celery tasks
4. Updating the workflow in the Director agent as needed
