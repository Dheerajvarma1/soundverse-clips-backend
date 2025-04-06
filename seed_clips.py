# seed_clips.py

from app.database import SessionLocal
from app.models import Clip

# Use royalty-free MP3s from Pixabay
clips_data = [
    {
        "title": "Flashing Lights",
        "description": "A relaxing lo-fi beat for background vibes.",
        "genre": "lofi",
        "duration": "430s",
        "audio_url": "https://soundverseai.com/Kanyewest.mp3",
        "play_count": 69420,
    },
    {
        "title": "Fein",
        "description": "Cinematic background music.",
        "genre": "orchestral",
        "duration": "228s",
        "audio_url": "https://soundverseai.com/travis.mp3",
        "play_count": 11220,
    },
    {
        "title": "Electronic Pulse",
        "description": "Futuristic electronic synth loop.",
        "genre": "electronic",
        "duration": "530s",
        "audio_url": "https://soundverseai.com/liluzi.mp3",
        "play_count": 12210,
    },
    {
        "title": "I Ain't Mad at Cha",
        "description": "I Ain't Mad at Cha is a song by American rapper 2Pac",
        "genre": "ambient",
        "duration": "272s",
        "audio_url": "https://soundverseai.com/2pac.mp3",
        "play_count": 21032,
    },
    {
        "title": "Rap God",
        "description": "Rap God is a song by American rapper Eminem.",
        "genre": "retro",
        "duration": "366s",
        "audio_url": "https://soundverseai.com/eminem.mp3",
        "play_count": 41210,
    }
]

def seed_clips():
    db = SessionLocal()
    for clip in clips_data:
        db_clip = Clip(**clip)
        db.add(db_clip)
    db.commit()
    db.close()
    print("✅ Clips inserted successfully!")

if __name__ == "__main__":
    seed_clips()
