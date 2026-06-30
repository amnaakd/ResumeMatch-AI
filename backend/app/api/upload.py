from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from app.services.resume_parser import extract_text_from_pdf
from app.utils.file_validator import validate_file

router = APIRouter(
    prefix="/api/upload",
    tags=["Upload"],
)

# Create uploads folder if it doesn't exist
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/resume")
async def upload_resume(file: UploadFile = File(...)):
    # ✅ Validate the uploaded file first
    validate_file(file)

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(str(file_path))

    return {
        "filename": file.filename,
        "saved_to": str(file_path),
        "text": resume_text
    }