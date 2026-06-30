COMMON_SKILLS = [
    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "react",
    "fastapi",
    "docker",
    "git",
    "github",
    "sql",
    "tensorflow",
    "opencv",
    "machine learning",
    "deep learning",
    "computer vision",
    "rag",
    "llm",
    "agentic ai",
]


def extract_skills(text: str):
    found = []

    for skill in COMMON_SKILLS:
        if skill in text:
            found.append(skill)

    return sorted(set(found))