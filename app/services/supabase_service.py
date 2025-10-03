from config.config import supabase

def create_manual_notes(user_id: str, title: str, language: str | None, drive_file_id: str | None, markdown_text: str) -> bool | None:
    try:
        master_data = supabase.table("notes").insert({
            "user_id": user_id,
            "title": title,
            "language": language,
            "drive_file_id": drive_file_id
        }).execute()
        note_id = master_data.data[0]['note_id']
        data = supabase.table("note_contents").insert({
            "note_id": note_id,
            "md_text": markdown_text,
        }).execute()
        return data is not None
    except Exception as e:
        print(f"Error creating manual note: {e}")
        return None

def get_manual_notes(user_id: str):
    try:
        data = supabase.table("notes").select("*, note_contents(*)").eq("user_id", user_id).execute()
        if data is None:
            return []
        return data
    except Exception as e:
        print(f"Error fetching manual notes: {e}")
        return None

def update_manual_note(note_id: int, title: str | None, language: str | None, drive_file_id: str | None, markdown_text: str | None):
    try:
        if title or language or drive_file_id:
            supabase.table("notes").update({
                "title": title,
                "language": language,
                "drive_file_id": drive_file_id
            }).eq("note_id", note_id).execute()
        if markdown_text:
            supabase.table("note_contents").update({
                "md_text": markdown_text,
            }).eq("note_id", note_id).execute()
        return True
    except Exception as e:
        print(f"Error updating manual note: {e}")
        return None
    
def save_transcript(user_id: str, filename: str, transcript: str):
    try:
        master_request = {
            "user_id": user_id,
            "title": filename,
        }
        master_response = supabase.table("notes").insert(master_request).execute()
        note_id = master_response.data[0]['note_id']
        content_request = {
            "note_id": note_id,
            "raw_text": transcript
        }
        content_response = supabase.table("note_contents").insert(content_request).execute()
        return content_response
    except Exception as e:
        print(f"Error saving transcript: {e}")
        return None
    
def add_summary(note_id: int, summary_text: str):
    try:
        data = supabase.table("summaries").insert({
            "note_id": note_id,
            "summary_text": summary_text
        }).execute()
        return data is not None
    except Exception as e:
        print(f"Error adding summary: {e}")
        return None
    
def add_tags(note_id: int, tags: list[str]):
    try:
        for tag in tags:
            tag_requests = {"tag": tag}
            master_data = supabase.table("tags").insert(tag_requests).execute()
            tag_id = master_data.data[0]['tag_id']
            note_tag_request = {"note_id": note_id,"tag_id": tag_id}
            data = supabase.table("note_tags").insert(note_tag_request).execute()

        return data is not None
    except Exception as e:
        print(f"Error adding tags: {e}")
        return None