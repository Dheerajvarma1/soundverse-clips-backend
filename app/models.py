from sqlalchemy import Column, Integer, String
from app.database import Base  # This is the line that defines Base

class Clip(Base):
    __tablename__ = "clips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    genre = Column(String)
    duration = Column(String)
    audio_url = Column(String)
    play_count = Column(Integer, default=0)
