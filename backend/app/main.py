from fastapi import FastAPI

app = FastAPI(
    title="ResumeMatch AI API",
    description="AI-powered resume analysis backend",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to ResumeMatch AI"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}