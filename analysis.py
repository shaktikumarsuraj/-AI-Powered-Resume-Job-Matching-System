def generate_analysis(
    role_match,
    required_score,
    preferred_score,
    semantic_score,
    skill_score,
    missing_required,
    missing_preferred
):

    analysis = []

    # Required skills
    if required_score == 1:
        analysis.append(
            "All detected required skills are present in the resume."
        )

    elif required_score > 0:
        analysis.append(
            "Some required skills are present, "
            "but some required skills are missing."
        )

    else:
        analysis.append(
            "None of the detected required skills "
            "were found in the resume."
        )

    # Preferred skills
    if preferred_score == 1:
        analysis.append(
            "All detected preferred skills are present."
        )

    elif preferred_score > 0:
        analysis.append(
            "Some preferred skills are present."
        )

    elif missing_preferred:
        analysis.append(
            "None of the detected preferred skills "
            "were found in the resume."
        )

    # Role
    if role_match:
        analysis.append(
            "The resume contains a matching role or role alias."
        )

    else:
        analysis.append(
            "No matching role or role alias was found "
            "in the resume."
        )

    # Semantic similarity
    if semantic_score >= 0.75:
        analysis.append(
            "Resume and job description have high "
            "semantic similarity."
        )

    elif semantic_score >= 0.50:
        analysis.append(
            "Resume and job description have moderate "
            "semantic similarity."
        )

    else:
        analysis.append(
            "Resume and job description have relatively "
            "low semantic similarity."
        )

    return analysis