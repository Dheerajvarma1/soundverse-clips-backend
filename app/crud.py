from sqlalchemy.orm import Session
from app.models import Clip

def get_all_clips(db: Session):
    return db.query(Clip).all()

def get_clip_by_id(db: Session, clip_id: int):
    return db.query(Clip).filter(Clip.id == clip_id).first()


def increment_play_count(db: Session, clip: Clip):
    clip.play_count += 1
    db.commit()
    db.refresh(clip)
    return clip
