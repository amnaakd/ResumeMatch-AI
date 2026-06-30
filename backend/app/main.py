from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.job import router as job_router
from app.api.match import router as match_router
app = FastAPI(
    title="ResumeMatch AI",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to ResumeMatch AI 🚀"}


@app.get("/health")
def health():
    return {"status": "healthy"}


app.include_router(upload_router)
app.include_router(job_router)
app.include_router(match_router)