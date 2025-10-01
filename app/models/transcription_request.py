from pydantic import BaseModel

class TranscriptionRequest(BaseModel):
    user_id: str         # ID user (supabase auth user id)
    filename: str        # nama file audio
