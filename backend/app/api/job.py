from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from app.services.resume_parser import extract_text_from_pdf
from app.services.text_preprocessor import clean_text
from app.services.skill_extractor import extract_skills
from app.utils.file_validator import validate_file

router = APIRouter(
    prefix="/api/job",
    tags=["Job Description"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/")
async def upload_job(file: UploadFile = File(...)):
    # ✅ Validate uploaded file
    validate_file(file)

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(str(file_path))

    cleaned = clean_text(text)

    skills = extract_skills(cleaned)

    return {
        "filename": file.filename,
        "skills": skills,
        "characters": len(cleaned)
    }