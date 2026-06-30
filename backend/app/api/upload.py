from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

router = APIRouter(
    prefix="/api/upload",
    tags=["Upload"],
)

# Create uploads folder if it doesn't exist
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/resume")
async def upload_resume(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "saved_to": str(file_path),
        "message": "Resume saved successfully!"
    }