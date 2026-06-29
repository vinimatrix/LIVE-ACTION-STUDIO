from fastapi import FastAPI
from app.api.v1 import api_router

app = FastAPI(
    title="AI Live Action Studio",
    description="MVP for converting manga pages to live-action video clips",
    version="0.1.0"
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "AI Live Action Studio MVP"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}