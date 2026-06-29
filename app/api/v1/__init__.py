from fastapi import APIRouter
from .endpoints import manga, jobs, assets

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(manga.router, prefix="/manga", tags=["manga"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(assets.router, prefix="/assets", tags=["assets"])
