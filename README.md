# 📒 Stripes - AI-Powered Student Note Assistant

Stripes is a mobile application designed to help students capture, organize, and manage lecture notes more effectively. With the power of AI speech-to-text transcription, automatic summarization, and intelligent tagging, Stripes enables students to focus on learning instead of manual note-taking.

The project includes a Python FastAPI backend (with Whisper for accurate transcription and NLP models for summarization & tagging) and a Flutter frontend for seamless mobile experience.

## Features

- 🎙️ Real-time Speech-to-Text
  Transcribe lectures in Indonesian & English using OpenAI Whisper.

- ✨ AI Summarization
  Automatically generate lecture summaries with bullet points, key definitions, and conclusions.

- 🏷️ Highlight & Auto-Tagging
  Extract keywords & auto-tag notes into relevant topics like Algorithms, Economics, Law.

## Installation & Setup

### 1. Git Clone

```bash
  git clone https://github.com/krisnaganesha1609/stripes-be.git
  cd stripes-be
```

### 2. Setup Environment

See next section for the info

### 3. Install Dependencies

```bash
  pip install -r requirements.txt
```

### 4. Run Locally

```bash
  uvicorn main:app --reload
```

### 5. OpenAPI Docs

Visit at `http://localhost:8000/docs`

## Environment Variables

Copy and paste the `.env.example` as `.env` and fill the variables. (INTERNAL ONLY)

`SUPABASE_URL`

`SUPABASE_KEY`

## Docker Deploy

This project has 3 docker flavor. Try:

### CPU (default)

```bash
  docker build -t stripes .
  docker run -p 8000:8000 stripes
```

### NVIDIA GPU

```bash
  docker build --target gpu -t stripes .
  docker run --gpus all -p 8000:8000 stripes
```

### Vulkan (AMD/Intel GPU)

```bash
  docker build --target vulkan -t stripes .
  docker run --device /dev/dri -p 8000:8000 stripes
```

## 👨‍💻 Contributors

- [I Gede Krisna Ganesha Widhiarta – Lead Backend & AI Engineer](https://github.com/krisnaganesha1609)

- [I Putu Justine Budi Wijaya – Backend Developer Support](https://github.com/riarumoda)

- [Ziyad Fathir Al Biaroza – UI/UX Designer & Documentation](https://github.com/Zeeroza)

- [Made Ayu Canakya Wiguna Giri – Documentation & QA](https://github.com/canakyawgn)

- [Mauliani Rahma Fazwat – Documentation & Support Developer](https://github.com/mlianirhm)
