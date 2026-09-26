def generate_matching_insights(
    analysis
):

    insights = []

    # -------------------------------------------------
    # ROLE
    # -------------------------------------------------

    role_match = analysis.get(
        "role"
    )

    if role_match:

        if role_match.get(
            "role_match"
        ):

            insights.append(
                "The resume contains a matching role or role alias."
            )

        else:

            insights.append(
                "No matching role or role alias was found in the resume."
            )


    # -------------------------------------------------
    # PRIORITY SKILLS
    # -------------------------------------------------

    priority = analysis.get(
        "priority_skills"
    )

    if priority:

        required = priority.get(
            "required",
            {}
        )

        matched = required.get(
            "matched",
            []
        )

        missing = required.get(
            "missing",
            []
        )

        if missing:

            insights.append(
                "Some required skills are missing."
            )

        elif matched:

            insights.append(
                "All detected required skills are present in the resume."
            )


        preferred = priority.get(
            "preferred",
            {}
        )

        preferred_matched = preferred.get(
            "matched",
            []
        )

        preferred_missing = preferred.get(
            "missing",
            []
        )

        if (
            preferred_missing
            and preferred_matched
        ):

            insights.append(
                "Some preferred skills are present, "
                "while some preferred skills are missing."
            )

        elif (
            preferred_missing
            and not preferred_matched
        ):

            insights.append(
                "None of the detected preferred skills "
                "were found in the resume."
            )

        elif preferred_matched:

            insights.append(
                "All detected preferred skills are present "
                "in the resume."
            )


    # -------------------------------------------------
    # EXPERIENCE DURATION
    # IMPORTANT:
    # compare_experience_requirements()
    # returns LIST
    # -------------------------------------------------

    experience_duration = analysis.get(
        "experience_duration"
    )

    if isinstance(
        experience_duration,
        list
    ):

        for result in experience_duration:

            if not isinstance(
                result,
                dict
            ):
                continue

            status = result.get(
                "status"
            )

            skill = result.get(
                "skill",
                "required skill"
            )

            if status == "not met":

                insights.append(
                    f"The required experience "
                    f"for {skill} is not met."
                )

            elif status == "met":

                insights.append(
                    f"The required experience "
                    f"for {skill} is met."
                )

            elif status == "unknown":

                insights.append(
                    f"The experience duration "
                    f"for {skill} could not be determined."
                )


    # -------------------------------------------------
    # PROJECT EVIDENCE
    # -------------------------------------------------

    if analysis.get(
        "project_evidence"
    ) is not None:

        insights.append(
            "Project evidence is available for "
            "the analyzed skills."
        )


    # -------------------------------------------------
    # EXPERIENCE EVIDENCE
    # -------------------------------------------------

    if analysis.get("experience_evidence"):
        insights.append(
        "Experience evidence is available for the analyzed skills."
    )
    else:
        insights.append(
        "No experience evidence was found for the analyzed skills."
    )


    # -------------------------------------------------
    # SEMANTIC SIMILARITY
    # -------------------------------------------------

    semantic_similarity = analysis.get(
        "semantic_similarity"
    )

    if semantic_similarity is not None:

        if semantic_similarity < 0.50:

            insights.append(
                "Resume and job description have "
                "relatively low semantic similarity."
            )

        elif semantic_similarity < 0.75:

            insights.append(
                "Resume and job description have "
                "moderate semantic similarity."
            )

        else:

            insights.append(
                "Resume and job description have "
                "high semantic similarity."
            )


    return insights