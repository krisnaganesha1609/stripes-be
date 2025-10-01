from pydantic import BaseModel
from typing import List, Optional

class TranscriptSegment(BaseModel):
    start: float         # waktu mulai segmen
    end: float           # waktu selesai segmen
    text: str            # teks hasil transkrip

class TranscriptionResponse(BaseModel):
    file_id: str         # ID unik file di Supabase
    filename: str
    transcript: str      # full teks
    segments: Optional[List[TranscriptSegment]] = None  # optional detail
    summary: Optional[str] = None  # optional ringkasan
    tags: Optional[List[str]] = None  # optional tags
