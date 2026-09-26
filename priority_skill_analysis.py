import re


def normalize_skill(skill):

    return skill.lower().strip()


def analyze_priority_skills(
    priority_results,
    resume_skills
):

    normalized_resume_skills = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    required_skills = []
    preferred_skills = []

    # ---------------------------------------------
    # Separate skills according to detected priority
    # ---------------------------------------------

    for result in priority_results:

        skill = result["skill"]
        priority = result["priority"]

        normalized_skill = normalize_skill(
            skill
        )

        if priority == "required":

            if normalized_skill not in required_skills:

                required_skills.append(
                    normalized_skill
                )

        elif priority == "preferred":

            if normalized_skill not in preferred_skills:

                preferred_skills.append(
                    normalized_skill
                )


    # ---------------------------------------------
    # Required skill matching
    # ---------------------------------------------

    required_matched = []
    required_missing = []

    for skill in required_skills:

        if skill in normalized_resume_skills:

            required_matched.append(skill)

        else:

            required_missing.append(skill)


    # ---------------------------------------------
    # Preferred skill matching
    # ---------------------------------------------

    preferred_matched = []
    preferred_missing = []

    for skill in preferred_skills:

        if skill in normalized_resume_skills:

            preferred_matched.append(skill)

        else:

            preferred_missing.append(skill)


    # ---------------------------------------------
    # Coverage calculation
    # ---------------------------------------------

    if len(required_skills) > 0:

        required_coverage = (
            len(required_matched)
            / len(required_skills)
        ) * 100

    else:

        required_coverage = 0.0


    if len(preferred_skills) > 0:

        preferred_coverage = (
            len(preferred_matched)
            / len(preferred_skills)
        ) * 100

    else:

        preferred_coverage = 0.0


    # ---------------------------------------------
    # Final result
    # ---------------------------------------------

    return {

        "required": {

            "all": required_skills,

            "matched": required_matched,

            "missing": required_missing,

            "coverage": required_coverage

        },

        "preferred": {

            "all": preferred_skills,

            "matched": preferred_matched,

            "missing": preferred_missing,

            "coverage": preferred_coverage

        }

    }