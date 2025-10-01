from fastapi import APIRouter, WebSocket
import tempfile
import whisper

router = APIRouter()
model = whisper.load_model("small")  # kecil biar cepat

@router.websocket("/ws/transcribe")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            audio_chunk = await websocket.receive_bytes()
            
            # Simpan sementara jadi file wav
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio_chunk)
                tmp.flush()
                result = model.transcribe(tmp.name, language=None)
            
            # Kirim balik teks sementara
            await websocket.send_text(result["text"])
    except Exception as e:
        await websocket.close()
