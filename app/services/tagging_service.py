from keybert import keyBERT
from services.supabase_service import add_tags

keybert = keyBERT()

def extract_keywords(note_id: str, text: str, top_n: int = 5) -> list[str]:
    keywords = keybert.extract_keywords(text, top_n=top_n)
    tags = [kw for kw, score in keywords]

    add_tags(note_id, tags)
    return tags