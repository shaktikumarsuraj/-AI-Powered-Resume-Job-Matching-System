import re


def calculate_skill_experience_duration(
    skill,
    experience_entries
):

    total_months = 0

    skill = skill.lower().strip()

    pattern = (
        r"(?<!\w)"
        + re.escape(skill)
        + r"(?!\w)"
    )

    for experience in experience_entries:

        content = experience[
            "content"
        ].lower()

        if re.search(
            pattern,
            content
        ):

            total_months += experience[
                "duration_months"
            ]

    return total_months


def compare_experience_requirements(
    requirements,
    experience_entries
):

    results = []

    for requirement in requirements:

        skill = requirement[
            "skill"
        ]

        required_years = requirement[
            "years"
        ]

        required_months = (
            required_years * 12
        )

        resume_months = (
            calculate_skill_experience_duration(
                skill,
                experience_entries
            )
        )

        if resume_months >= required_months:

            status = "met"

        else:

            status = "not met"

        results.append(
            {
                "skill": skill,
                "required_years": required_years,
                "required_months": required_months,
                "resume_months": resume_months,
                "status": status
            }
        )

    return results