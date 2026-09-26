import re
import json
import os 


def load_skills():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "skills.json")
    with open(file_path, "r") as file:
        skill_data = json.load(file)

    skills = []

    for category in skill_data.values():
        skills.extend(category)

    return skills

def load_skill_categories():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "skills.json")

    with open(file_path, "r") as file:
        skill_data = json.load(file)

    return skill_data


def extract_skills_by_category(text):
    text = text.lower()

    skill_categories = load_skill_categories()

    found_skills = {}

    for category, skills in skill_categories.items():
        found_skills[category] = []

        for skill in skills:
            pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

            if re.search(pattern, text):
                found_skills[category].append(skill)

    return found_skills


def extract_skills(text):
    text = text.lower()
    found_skills = []

    skills = load_skills()
    skills = sorted(skills, key=len, reverse=True)

    for skill in skills:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


def compare_skills(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = resume_set & job_set
    missing_skills = job_set - resume_set

    return list(matched_skills), list(missing_skills)

def compare_skills_by_category(resume_skills, job_skills):
    result = {}

    categories = set(resume_skills) | set(job_skills)

    for category in categories:
        resume_set = set(resume_skills.get(category, []))
        job_set = set(job_skills.get(category, []))

        matched = resume_set & job_set
        missing = job_set - resume_set

        result[category] = {
            "matched": list(matched),
            "missing": list(missing)
        }

    return result


def calculate_skill_match(matched_skills, job_skills):
    if not job_skills:
        return 0

    skill_match = len(matched_skills) / len(job_skills)

    return skill_match


def calculate_priority_skill_match(
    resume_skills,
    required_skills,
    preferred_skills
):
    resume_set = set(resume_skills)

    required_set = set(required_skills)
    preferred_set = set(preferred_skills)

    matched_required = resume_set & required_set
    missing_required = required_set - resume_set

    matched_preferred = resume_set & preferred_set
    missing_preferred = preferred_set - resume_set

    if required_set:
        required_score = (
            len(matched_required) / len(required_set)
        )
    else:
        required_score = 0

    if preferred_set:
        preferred_score = (
            len(matched_preferred) / len(preferred_set)
        )
    else:
        preferred_score = 0

    return (
        list(matched_required),
        list(missing_required),
        required_score,
        list(matched_preferred),
        list(missing_preferred),
        preferred_score
    )

def extract_skills_from_sections(sections):
    section_skills = {}

    for section, content in sections.items():
        section_skills[section] = extract_skills(content)

    return section_skills

def find_skill_evidence(skill, sections):
    evidence = []

    for section, content in sections.items():
        found_skills = extract_skills(content)

        if skill.lower() in found_skills:
            evidence.append(section)

    return evidence

def calculate_evidence_strength(skill, sections):
    strength = {}

    for section in sections:

        if section == "projects":
            strength[section] = "strong"

        elif section == "experience":
            strength[section] = "strong"

        elif section == "skills":
            strength[section] = "direct"

        elif section == "education":
            strength[section] = "academic"

        elif section == "achievements" or section == "awards & achievements":
            strength[section] = "supporting"

        elif section == "general":
            strength[section] = "supporting"

        else:
            strength[section] = "supporting"

    return strength


def summarize_evidence_strength(evidence_strength):
    if not evidence_strength:
        return "none"

    strengths = set(evidence_strength.values())

    if "strong" in strengths:
        return "strong"

    if "direct" in strengths:
        return "direct"

    if "academic" in strengths:
        return "academic"

    if "supporting" in strengths:
        return "supporting"

    return "none"