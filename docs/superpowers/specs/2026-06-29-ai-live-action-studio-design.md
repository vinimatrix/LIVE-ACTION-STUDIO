# AI Live Action Studio - Design Specification

**Date:** 2026-06-29  
**Project:** AI Live Action Studio  
**MVP Scope:** Transform a single manga page into a short video clip (4-10 seconds)

## Architecture Overview

Based on user preferences, we will implement a **hybrid modular architecture** with a central orchestrator (Director agent) coordinating pluggable agent modules for specialized tasks.

### Core Architecture Principles
- **Modularity:** Each agent operates as an independent module with well-defined interfaces
- **Orchestration:** Director agent manages workflow orchestration and state management
- **Extensibility:** New agents can be added without modifying existing core logic
- **Technology Stack:** Python/FastAPI backend with Ollama for LLMs or hugging face u other or nanobanna of flow, ComfyUI/SDXL or other tools like flux or runway, for image generation, FFmpeg for video assembly

## System Components

### 1. Director Agent (Orchestrator)
**Responsibilities:**
- Divide manga chapter into scenes/pages
- Organize scenes into a coherent narrative flow
- Control narrative pacing and rhythm
- Maintain continuity across scenes
- Validate final output quality
- Manage workflow state and agent coordination

**Interfaces:**
- Input: Raw manga pages (images/text)
- Output: Structured scene breakdown with timing, camera directions, and agent task assignments
- Communication: Message queue for task distribution to other agents

### 2. Screenwriter Agent
**Responsibilities:**
- Convert manga pages into cinematic scripts
- Generate actions, dialogues, emotions, and movements
- Expand narrative beyond literal panel content
- Maintain character voice and tone consistency
- Create smooth transitions between scenes
- Create storyboards or animatics to show the flow of the video

**Interfaces:**
- Input: Scene breakdown from Director
- Output: Detailed screenplay with dialogues, actions, camera notes

### 3. Character Manager Agent
**Responsibilities:**
- Maintain persistent character database
- Ensure visual consistency across all appearances
- Manage character expressions, poses, costumes, and accessories
- Track character relationships and development
- Reuse existing character assets when possible

**Interfaces:**
- Input: Character requirements from Screenplay
- Output: Character asset references and specifications
- Storage: Character database with visual references

### 4. Environment Manager Agent
**Responsibilities:**
- Build and manage the story universe
- Handle locations (cities, interiors, forests, castles, etc.)
- Control environmental factors (weather, lighting, time of day)
- Ensure location consistency across scenes
- Reuse existing environment assets

**Interfaces:**
- Input: Location requirements from Screenplay
- Output: Environment asset references and specifications
- Storage: Location database with visual references

### 5. Cinematography Agent
**Responsibilities:**
- Determine camera movements (tracking, dolly, crane, handheld, steadycam, drone)
- Select appropriate lenses and shot types
- Control depth of field and focus techniques
- Design visual composition and framing
- Plan visual pacing and rhythm

**Interfaces:**
- Input: Scene requirements from Screenplay
- Output: Camera specifications and shot lists
- Storage: Cinematography reference library

### 6. Prompt Builder Agent
**Responsibilities:**
- Generate prompts for image, video, voice, and effects generation
- Automatically inherit character, environment, lighting, and style attributes
- Ensure continuity and consistency across generated assets
- Optimize prompts for specific AI models (Flux, SDXL, Kling, etc.)

**Interfaces:**
- Input: Character specs, environment specs, cinematography plans, screenplay
- Output: Optimized prompts for each generation agent
- Storage: Prompt templates and optimization rules

### 7. Image Generation Agent
**Responsibilities:**
- Generate key frames and visual assets
- Compatible with ComfyUI, Flux, SDXL, and similar tools
- Ensure visual consistency with established character/environment references
- Apply consistent artistic style and lighting
- Generate variations for different camera angles/expressions

**Interfaces:**
- Input: Optimized prompts from Prompt Builder
- Output: Generated image assets
- Storage: Image asset library with metadata

### 8. Video Generation Agent
**Responsibilities:**
- Generate short video clips (4-8 seconds) from images and prompts
- Compatible with Kling, Veo, Runway, Wan, Hunyuan, etc.
- Create smooth motion between keyframes
- Apply cinematographic movements specified by Cinematography Agent
- Generate VFX elements when needed

**Interfaces:**
- Input: Image assets, prompts, cinematography specs
- Output: Video clip segments
- Storage: Video asset library

### 9. Voice Generation Agent
**Responsibilities:**
- Generate character voices, breaths, laughs, whispers, shouts
- Maintain consistent voice profiles for each character
- Generate emotional variations appropriate to scene context
- Synchronize lip movements with generated video

**Interfaces:**
- Input: Dialogue from Screenplay, character voice profiles
- Output: Audio assets (dialogue, effects)
- Storage: Voice asset library

### 10. Music Generation Agent
**Responsibilities:**
- Compose opening themes, suspense tracks, battle music, drama scores, credits
- Generate adaptive music that responds to scene intensity
- Maintain thematic consistency throughout the piece
- Create dynamic transitions between musical themes

**Interfaces:**
- Input: Scene emotional tone, pacing requirements
- Output: Music tracks and stems
- Storage: Music asset library

### 11. FX (Effects) Generation Agent
**Responsibilities:**
- Generate visual effects: explosions, magic, smoke, particles, fire, electricity, shadows, portals
- Ensure VFX integrates seamlessly with live-action elements
- Apply consistent style and physics rules
- Optimize for real-time rendering where possible

**Interfaces:**
- Input: VFX requirements from screenplay/scenes
- Output: Effect assets and composite layers
- Storage: Effects asset library

### 12. Editor Agent (Automatic Editor)
**Responsibilities:**
- Assemble final video from all components
- Synchronize video, voice, effects, music
- Add subtitles and captions
- Apply color grading and final polishing
- Render final output in desired format
- Ensure broadcast-quality output

**Interfaces:**
- Input: All generated assets (video, audio, effects, music, subtitles)
- Output: Final video file
- Storage: Final output repository

## Data Flow

1. **Input:** Manga page (image + text via OCR)
2. **Director:** Breaks page into scenes, assigns timing and camera directions
3. **Screenwriter:** Converts scenes to screenplay with dialogues/actions
4. **Character Manager:** Provides character references and specifications
5. **Environment Manager:** Provides environment/location references
6. **Cinematography Agent:** Determines camera movements and shot types
7. **Prompt Builder:** Creates optimized prompts for all generation agents
8. **Image Generation:** Creates key frames and visual assets
9. **Video Generation:** Creates motion clips from images
10. **Voice Generation:** Creates character voices and audio
11. **Music Generation:** Creates background score
12. **FX Generation:** Creates special effects
13. **Editor:** Assembles all components into final video
14. **Output:** Completed video clip

## Technology Stack Details

### Backend
- **Language:** Python 3.11+
- **Framework:** FastAPI for REST APIs and WebSocket communication
- **Task Queue:** Celery with Redis broker for asynchronous task processing
- **Workflow Orchestration:** Custom Director agent with state persistence

### AI/ML Components
- **LLM:** Ollama with Llama 3 or Nemotron models for text generation
- **Image Generation:** ComfyUI workflows with SDXL and Flux models
- **Video Generation:** Integration with Kling, Veo, or similar video APIs
- **Voice Generation:** Custom voice models trained on character voices
- **Music Generation:** AI music generation models (Stable Audio, MusicLM alternatives)
- **FX Generation:** Specialized models for particle effects, simulations

### Data Storage
- **Primary Database:** PostgreSQL for structured data (characters, locations, scripts)
- **Asset Storage:** MinIO (S3-compatible) for media assets (images, video, audio)
- **Cache:** Redis for temporary processing data and session states
- **File System:** Local storage for temporary processing files

### Infrastructure
- **Containerization:** Docker for service isolation
- **Orchestration:** Docker Compose for development, Kubernetes for production
- **Monitoring:** Prometheus + Grafana for metrics
- **Logging:** ELK stack (Elasticsearch, Logstash, Kibana)

## API Design

### Core Endpoints
- `POST /process-manga` - Main entry point for manga processing
- `GET /status/{job_id}` - Check processing status
- `GET /result/{job_id}` - Retrieve completed video
- `POST /agents/{agent_type}/task` - Direct agent task submission
- `GET /assets/{asset_type}` - Retrieve stored assets

### Agent Communication
- Internal message queue (Redis/RabbitMQ) for agent-to-agent communication
- Each agent subscribes to relevant task queues
- Results published to result queues for aggregation

## Data Models

### Character Model
```python
{
  "id": "uuid",
  "name": "string",
  "visual_references": ["image_urls"],
  "personality_traits": ["strings"],
  "expressions": ["expression_names"],
  "outfits": [{"name": "string", "reference": "image_url"}],
  "weapons": [{"name": "string", "reference": "image_url"}],
  "abilities": [{"name": "string", "description": "string"}],
  "voice_profile": "voice_model_reference"
}
```

### Scene Model
```python
{
  "id": "uuid",
  "manga_page_reference": "image_url",
  "description": "text",
  "dialogue": [{"character": "string", "text": "string", "emotion": "string"}],
  "actions": ["action_descriptions"],
  "camera_instructions": {
    "shot_type": "string",
    "movement": "string",
    "duration": "float",
    "focus": "string"
  },
  "characters_present": ["character_ids"],
  "location": "location_id",
  "time_of_day": "string",
  "weather": "string"
}
```

### Asset Model
```python
{
  "id": "uuid",
  "type": "image|video|audio|effect|music",
  "content": "binary_data_or_url",
  "metadata": {
    "created_by": "agent_type",
    "prompt_used": "string",
    "generation_params": "json",
    "related_entities": ["character_ids", "location_ids"]
  },
  "timestamp": "datetime"
}
```

## Quality Assurance & Testing

### Unit Testing
- Each agent unit tested with mock inputs/outputs
- Prompt validation and optimization testing
- Asset generation quality checks

### Integration Testing
- End-to-end pipeline testing with sample manga pages
- Cross-agent data flow validation
- Output quality assessment

### Continuity Validation
- Automated character consistency checking
- Location/environment consistency verification
- Temporal coherence checking

## Error Handling & Resilience

### Error Categories
1. **Input Validation Errors** - Invalid manga format, missing data
2. **Processing Errors** - Agent failures, timeout, resource exhaustion
3. **Output Quality Issues** - Failed quality checks, consistency violations
4. **System Errors** - Database failures, storage issues, network problems

### Handling Strategies
- Retry mechanisms with exponential backoff
- Fallback to alternative models/approaches
- Manual review queues for problematic outputs
- Comprehensive logging and alerting
- Graceful degradation when non-critical components fail

## Security Considerations

### Data Protection
- Secure storage of user-uploaded content
- Encryption at rest for sensitive assets
- Access controls for asset repositories
- Audit trails for all operations

### Model Security
- Input sanitization for AI model prompts
- Output filtering to prevent inappropriate content
- Rate limiting to prevent abuse
- Model version tracking and validation

## Deployment Architecture

### Development Environment
- Docker Compose for local development
- Pre-configured development containers
- Hot-reload capabilities for iterative development
- Local AI model caching for faster iteration

### Production Environment
- Kubernetes orchestration
- Auto-scaling based on queue depth
- GPU node allocation for ML workloads
- CDN for asset delivery
- Blue-green deployment strategy

## Success Criteria (MVP)

### Functional Requirements
- [ ] Process single manga page input (image + extracted text)
- [ ] Generate 4-8 second video clip with synchronized audio
- [ ] Maintain character consistency throughout the clip
- [ ] Apply appropriate cinematography based on scene content
- [ ] Generate appropriate background music and sound effects
- [ ] Deliver output in standard video format (MP4)

### Quality Requirements
- [ ] Output resembles professional live-action production (not AI-looking)
- [ ] Lip-sync accuracy within acceptable thresholds
- [ ] Visual consistency with source material style
- [ ] Audio-visual synchronization within 100ms tolerance
- [ ] Stable frame rate (24fps or 30fps)

### Performance Requirements
- [ ] Processing time under 10 minutes for 8-second clip
- [ ] Memory usage under 16GB peak
- [ ] Storage efficiency (reuse assets where possible)
- [ ] Scalable to multiple concurrent jobs

## Future Extensions

### Phase 2: Multi-Page Processing
- Process full manga chapters into complete episodes
- Improved narrative arc management
- Enhanced character arc tracking
- Episode-level continuity maintenance

### Phase 3: Advanced Features
- User-directed scene modifications
- Multiple artistic style options
- Interactive character customization
- Real-time preview capabilities
- Multi-language support (dubbing/subtitles)

### Phase 4: Production Pipeline
- Integration with professional video editing tools
- Collaborative workflow features
- Asset version control and management
- Automated quality control and rating systems
- Distribution and publishing integrations

---
*This design document represents the agreed-upon architecture for the AI Live Action Studio MVP. Implementation will proceed via the writing-plans skill to create detailed implementation tasks.*