import torch
from transformers import pipeline
from services.supabase_service import add_summary

pipeline = pipeline("summarization", model="google/pegasus-x-large", dtype=torch.bfloat16, device=0)

def summarize_text(note_id: str, text: str, max_length: int = 512, min_length: int = 30) -> str:
    summary = pipeline(text, max_length=max_length, min_length=min_length, do_sample=False)
    summarize_text = summary[0]['summary_text']

    add_summary(note_id, summarize_text)
    return summarize_text

