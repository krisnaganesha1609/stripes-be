from fastapi import APIRouter, HTTPException, Response
from services.supabase_service import supabase
from services.export_service import ExportService

router = APIRouter()

@router.get("/export/{note_id}")
async def export_note(note_id: str, format: str = "md"):
    # ambil note dari Supabase
    note = supabase.table("notes").select("*").eq("note_id", note_id).single().execute().data
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    # format export
    if format == "md":
        content = ExportService.to_md(note)
        return Response(content, media_type="text/markdown")
    elif format == "txt":
        content = ExportService.to_txt(note)
        return Response(content, media_type="text/plain")
    elif format == "pdf":
        buffer = ExportService.to_pdf(note)
        return Response(buffer.read(), media_type="application/pdf")
    elif format == "docx":
        buffer = ExportService.to_docx(note)
        return Response(buffer.read(), media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    else:
        raise HTTPException(status_code=400, detail="Invalid format")
