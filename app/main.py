from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from app.api import transcription, export
from app.ws import websocket

app = FastAPI(
    title="Stripes Backend",
    description="Hybrid AI transcription service for Stripes App",
    version="1.0.0",
    contact={
        "name": "Stripes Team",
        "email": "argozt@googlegroups.com"
    }
)

# Allow frontend (Flutter) to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # kalau production, ganti dengan domain Flutter app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(transcription.router, prefix="/api", tags=["Transcription"])
app.include_router(export.router, prefix="/api", tags=["Export"])
app.include_router(websocket.router, prefix="/ws", tags=["Realtime Transcribe"])

# Health Check
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Stripes API is running 🚀"}

