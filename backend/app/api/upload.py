from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/api/upload",
    tags=["Upload"],
)


@router.post("/resume")
async def upload_resume(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Resume uploaded successfully!"
    }