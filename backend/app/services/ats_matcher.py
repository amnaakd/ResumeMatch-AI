def calculate_match(resume_skills: list, job_skills: list):
    """
    Compare resume skills with job skills and calculate ATS match score.
    """

    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    matched = sorted(resume_set & job_set)
    missing = sorted(job_set - resume_set)

    score = 0

    if job_set:
        score = round((len(matched) / len(job_set)) * 100, 2)

    return {
        "ats_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "resume_skill_count": len(resume_set),
        "job_skill_count": len(job_set)
    }