from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings
from app.db.base import BaseModel

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(cls=BaseModel)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()