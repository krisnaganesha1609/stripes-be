# -------------------
# GPU Stage (NVIDIA CUDA)
# -------------------
FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04 AS gpu

RUN apt-get update && apt-get install -y \
    python3 python3-pip git ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# -------------------
# CPU Stage (Default)
# -------------------
FROM python:3.11-slim AS cpu

RUN apt-get update && apt-get install -y \
    python3 python3-pip git ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# -------------------
# Final Select
# -------------------
# Default → CPU
# You can override with:
#   docker build --target gpu -t smartnote .
#   docker build --target vulkan -t smartnote .
#   docker build --target cpu -t smartnote .
FROM cpu

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]