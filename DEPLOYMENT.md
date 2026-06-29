# Deployment Guide

## Development

### Prerequisites

- Docker and Docker Compose
- Python 3.14+
- Node.js 16+ (if using frontend)

### Local Development

1. Clone the repository
2. Copy `.env.example` to `.env` and configure
3. Run `docker-compose up -d` to start services
4. Run `pip install -r requirements.txt` for Python dependencies
5. Run `npm install` in frontend directory (if applicable)
6. Run `pytest` to execute tests
7. Access API at `http://localhost:8000`
8. Access frontend at `http://localhost:3000` (if applicable)

### Environment Variables

See `app/core/config.py` for configuration options.
Key variables:
- DATABASE_URL: PostgreSQL connection string
- REDIS_URL: Redis connection string
- MINIO_ENDPOINT: MinIO server endpoint
- MINIO_ACCESS_KEY: MinIO access key
- MINIO_SECRET_KEY: MinIO secret key
- OLLAMA_BASE_URL: Ollama server URL

## Production

### Kubernetes Deployment

1. Build Docker images: `docker build -t ai-live-action-studio .`
2. Push images to container registry
3. Apply Kubernetes manifests:
   ```bash
   kubectl apply -f k8s/
   ```
4. Configure ingress for external access
5. Set up persistent volumes for database and storage
6. Configure secrets for sensitive values

### Monitoring

- Prometheus + Grafana for metrics
- ELK stack for logging
- Health checks on all services

## Scaling

- The Director agent can scale horizontally
- Individual agent types can scale based on queue depth
- GPU nodes can be allocated for ML-intensive agents (image/video generation)
- Redis and PostgreSQL can be clustered for high availability
