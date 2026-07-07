from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.v1 import api_router
import os

app = FastAPI(
    title="AI Live Action Studio",
    description="MVP for converting manga pages to live-action video clips",
    version="0.1.0"
)

static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)

app.mount("/static", StaticFiles(directory=static_dir), name="static")
app.include_router(api_router)

@app.get("/")
async def root():
    index = os.path.join(static_dir, "index.html")
    if os.path.exists(index):
        return FileResponse(index)
    return {"message": "AI Live Action Studio MVP"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}