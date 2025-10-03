from fastapi import APIRouter, UploadFile, File
from services.whisper_service import transcribe_batch
from services.supabase_service import save_transcript
from services.summarization_service import summarize_text
from services.tagging_service import extract_keywords
from models import TranscriptionResponse, TranscriptSegment
import tempfile

router = APIRouter()

@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_file(user_id: str, file: UploadFile = File(...)):
    # Simpan file sementara
    audio_path = f"/tmp/{file.filename}"
    with open(audio_path, "wb") as f:
        f.write(await file.read())

    # Transkripsi pakai Whisper
    result = transcribe_batch(audio_path)

    # Simpan ke Supabase
    file_id = save_transcript(
        user_id=user_id,
        filename=file.filename,
        transcript=result["text"],
    )

    summary = summarize_text(file_id=file_id[0]['note_id'], text=result["text"])
    tags = extract_keywords(note_id=file_id[0]['note_id'], text=summary)

    return TranscriptionResponse(
        file_id=file_id,
        filename=file.filename,
        transcript=result["text"],
        summary=summary,
        tags=tags
    )
