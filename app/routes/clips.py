from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from app.database import SessionLocal
from app.crud import get_all_clips, get_clip_by_id, increment_play_count

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/clips")
def read_clips(db: Session = Depends(get_db)):
    return get_all_clips(db)

@router.get("/clips/{clip_id}/stream")
def stream_clip(clip_id: int, db: Session = Depends(get_db)):
    clip = get_clip_by_id(db, clip_id)
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    increment_play_count(db, clip)
    return RedirectResponse(url=clip.audio_url)

@router.get("/clips/{clip_id}/stats")
def get_clip_stats(clip_id: int, db: Session = Depends(get_db)):
    clip = get_clip_by_id(db, clip_id)
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    return {
        "id": clip.id,
        "title": clip.title,
        "description": clip.description,
        "genre": clip.genre,
        "duration": clip.duration,
        "audio_url": clip.audio_url,
        "play_count": clip.play_count
    }
