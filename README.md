# ResumeMatch-AI

An AI-powered Resume ATS Analyzer that compares a resume with a job description, calculates an ATS compatibility score, identifies missing skills, and provides intelligent suggestions to improve the resume.

---

## Features

- Upload Resume (PDF/DOCX)
- Upload or Paste Job Description
- Extract Resume Text
- ATS Score Calculation
- Skill Gap Analysis
- AI-powered Resume Suggestions
- Modern Web Interface
- REST API using FastAPI

---

## Tech Stack

### Backend
- Python 3.14
- FastAPI
- Uvicorn

### Frontend
- React
- Vite

### AI & NLP
- Sentence Transformers
- spaCy
- Hugging Face Transformers

---

## Project Structure

```text
ResumeMatch-AI/
│
├── backend/
├── frontend/
├── docs/
├── assets/
└── README.md
```

---

## Development Roadmap

- [x] Project Setup
- [x] FastAPI Backend
- [ ] Resume Upload API
- [ ] Resume Text Extraction
- [ ] Job Description Upload
- [ ] ATS Scoring Engine
- [ ] Skill Extraction
- [ ] AI Suggestions
- [ ] Frontend Development
- [ ] Deployment

---

## Installation

Clone the repository:

```bash
git clone https://github.com/amnaakd/ResumeMatch-AI.git
```

Go to the backend:

```bash
cd ResumeMatch-AI/backend
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn app.main:app --reload
```

---

## Current Status

🚧 Under active development.

---

## Author

**Amna Khalid**

GitHub: https://github.com/amnaakd