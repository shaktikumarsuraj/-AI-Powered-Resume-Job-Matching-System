import re


def find_experience_evidence(
    job_skills,
    resume_sections
):
    experience_evidence = {}

    experience_sections = [
        "experience",
        "work experience"
    ]

    for section in experience_sections:

        if section not in resume_sections:
            continue

        content = resume_sections[section]

        for skill in job_skills:

            pattern = (
                r"(?<!\w)"
                + re.escape(skill.lower())
                + r"(?!\w)"
            )

            if re.search(
                pattern,
                content.lower()
            ):

                if skill not in experience_evidence:
                    experience_evidence[skill] = []

                experience_evidence[skill].append(
                    section
                )

    return experience_evidence