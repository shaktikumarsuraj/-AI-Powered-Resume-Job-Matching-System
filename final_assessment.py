def build_final_assessment(
    analysis
):

    assessment = {}


    # ---------------------------------------------
    # ROLE ASSESSMENT
    # ---------------------------------------------

    role = analysis.get(
        "role"
    )

    if role is None:

        assessment["role"] = {
            "status": "unknown"
        }

    elif role.get(
        "role_match"
    ):

        assessment["role"] = {
            "status": "matched"
        }

    else:

        assessment["role"] = {
            "status": "not matched"
        }


    # ---------------------------------------------
    # REQUIRED SKILL ASSESSMENT
    # ---------------------------------------------

    priority = analysis.get(
        "priority_skills"
    )

    if priority is not None:

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

        if missing and matched:

            required_status = "partially met"

        elif missing:

            required_status = "not met"

        elif matched:

            required_status = "met"

        else:

            required_status = "unknown"


        assessment["required_skills"] = {

            "status": required_status,

            "matched": matched,

            "missing": missing,

            "coverage": required.get(
                "coverage",
                0.0
            )
        }


        # -----------------------------------------
        # PREFERRED SKILL ASSESSMENT
        # -----------------------------------------

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

            preferred_status = (
                "partially met"
            )

        elif preferred_missing:

            preferred_status = "not met"

        elif preferred_matched:

            preferred_status = "met"

        else:

            preferred_status = "unknown"


        assessment["preferred_skills"] = {

            "status": preferred_status,

            "matched": preferred_matched,

            "missing": preferred_missing,

            "coverage": preferred.get(
                "coverage",
                0.0
            )
        }

    else:

        assessment["required_skills"] = {
            "status": "unknown"
        }

        assessment["preferred_skills"] = {
            "status": "unknown"
        }


    # ---------------------------------------------
    # EXPERIENCE ASSESSMENT
    # ---------------------------------------------

    experience_duration = analysis.get(
        "experience_duration"
    )

    experience_assessment = []


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

            experience_assessment.append(
                {
                    "skill": result.get(
                        "skill"
                    ),

                    "required_years": result.get(
                        "required_years"
                    ),

                    "resume_months": result.get(
                        "resume_months"
                    ),

                    "status": result.get(
                        "status",
                        "unknown"
                    )
                }
            )

    elif isinstance(
        experience_duration,
        dict
    ):

        for skill, result in experience_duration.items():

            if not isinstance(
                result,
                dict
            ):
                continue

            experience_assessment.append(
                {
                    "skill": result.get(
                        "skill",
                        skill
                    ),

                    "required_years": result.get(
                        "required_years"
                    ),

                    "resume_months": result.get(
                        "resume_months"
                    ),

                    "status": result.get(
                        "status",
                        "unknown"
                    )
                }
            )


    assessment[
        "experience_requirements"
    ] = experience_assessment


    # ---------------------------------------------
    # EVIDENCE AVAILABILITY
    # ---------------------------------------------

    skill_evidence = analysis.get(
        "skill_evidence"
    )

    project_evidence = analysis.get(
        "project_evidence"
    )

    experience_evidence = analysis.get(
        "experience_evidence"
    )

    assessment["evidence"] = {

        "skill": bool(
            skill_evidence
        ),

        "project": bool(
            project_evidence
        ),

        "experience": bool(
            experience_evidence
        )
    }


    # ---------------------------------------------
    # SIMILARITY
    # ---------------------------------------------

    assessment["similarity"] = {

        "tfidf": analysis.get(
            "tfidf_similarity"
        ),

        "semantic": analysis.get(
            "semantic_similarity"
        )
    }


    # ---------------------------------------------
    # CATEGORY ANALYSIS
    # ---------------------------------------------

    assessment[
        "category_analysis_available"
    ] = (
        analysis.get(
            "category_analysis"
        ) is not None
    )


    return assessment