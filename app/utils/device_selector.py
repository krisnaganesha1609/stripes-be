import os
import torch

def detect_device() -> str:
    # Prioritas manual override
    manual = os.getenv("USE_DEVICE")
    if manual in ["cuda", "cpu"]:
        return manual

    # Cek CUDA via nvidia-smi
    if torch.cuda.is_available():
        return "cuda"

    # Default fallback
    return "cpu"
