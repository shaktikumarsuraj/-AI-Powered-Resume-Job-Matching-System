def compare_experience_requirement(
    required_years,
    resume_months
):

    required_months = required_years * 12

    if resume_months >= required_months:
        status = "met"
    else:
        status = "not met"

    return {
        "required_months": required_months,
        "resume_months": resume_months,
        "status": status
    }


def compare_all_experience_requirements(
    requirements,
    resume_months
):

    results = []

    for requirement in requirements:

        result = compare_experience_requirement(
            requirement["years"],
            resume_months
        )

        result["skill"] = requirement["skill"]
        result["required_years"] = requirement["years"]

        results.append(result)

    return results