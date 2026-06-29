from fastapi import APIRouter, HTTPException
from app.db.session import SessionLocal
from app.models import Asset

router = APIRouter()


@router.get("/{asset_id}")
async def get_asset(asset_id: int):
    db = SessionLocal()
    try:
        asset = db.query(Asset).filter(Asset.id == asset_id).first()
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found")

        return {
            "id": asset.id,
            "type": asset.asset_type,
            "file_path": asset.file_path,
            "file_size": asset.file_size,
            "mime_type": asset.mime_type,
            "metadata": asset.generation_metadata,
        }
    finally:
        db.close()
