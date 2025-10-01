import os
import subprocess

def detect_device() -> str:
    # Prioritas manual override
    manual = os.getenv("USE_DEVICE")
    if manual in ["cuda", "vulkan", "cpu"]:
        return manual

    # Cek CUDA via nvidia-smi
    try:
        subprocess.check_output(["nvidia-smi"], stderr=subprocess.DEVNULL)
        return "cuda"
    except Exception:
        pass

    # Cek Vulkan (AMD/Intel) via vulkaninfo
    try:
        subprocess.check_output(["vulkaninfo"], stderr=subprocess.DEVNULL)
        return "vulkan"
    except Exception:
        pass

    # Default fallback
    return "cpu"
