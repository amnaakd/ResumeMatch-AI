from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from app.services.resume_parser import extract_text_from_pdf
from app.services.text_preprocessor import clean_text
from app.services.skill_extractor import extract_skills
from app.services.ats_matcher import calculate_match
from app.utils.file_validator import validate_file

router = APIRouter(
    prefix="/api/match",
    tags=["ATS Matching"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/")
async def match_resume(
    resume: UploadFile = File(...),
    job: UploadFile = File(...)
):
    # Validate both uploaded files
    validate_file(resume)
    validate_file(job)

    resume_path = UPLOAD_DIR / resume.filename
    job_path = UPLOAD_DIR / job.filename

    with resume_path.open("wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    with job_path.open("wb") as buffer:
        shutil.copyfileobj(job.file, buffer)

    resume_text = extract_text_from_pdf(str(resume_path))
    job_text = extract_text_from_pdf(str(job_path))

    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    resume_skills = extract_skills(resume_clean)
    job_skills = extract_skills(job_clean)

    result = calculate_match(resume_skills, job_skills)

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        **result
    }