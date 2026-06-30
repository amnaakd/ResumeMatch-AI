import re


def clean_text(text: str) -> str:
    """
    Clean extracted resume text before analysis.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    return text.strip()