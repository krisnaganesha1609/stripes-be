import tempfile
import whisper
from typing import Dict, Any, Optional
from utils.device_selector import detect_device

# Load model global supaya nggak re-load setiap request
# Gunakan small untuk realtime, large untuk batch final
device = detect_device()
model_realtime = whisper.load_model("small", device=device)  
model_batch = whisper.load_model("large", device=device)


def transcribe_realtime(audio_bytes: bytes, language: Optional[str] = None) -> Dict[str, Any]:
    """
    Transkripsi audio kecil (chunk) untuk realtime websocket.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp.flush()
        result = model_realtime.transcribe(tmp.name, language=language)
    return result  # {"text": "...", "segments": [...]}

def transcribe_batch(audio_path: str, language: Optional[str] = None) -> Dict[str, Any]:
    """
    Transkripsi file audio penuh (upload batch final).
    """
    result = model_batch.transcribe(audio_path, language=language)
    return result  # {"text": "...", "segments": [...]}
