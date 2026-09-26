def build_final_matching_analysis(
    role_analysis=None,
    priority_analysis=None,
    skill_evidence=None,
    project_evidence=None,
    experience_evidence=None,
    experience_duration=None,
    tfidf_similarity=None,
    semantic_similarity=None,
    category_analysis=None
):

    analysis = {
        "role": role_analysis,
        "priority_skills": priority_analysis,
        "skill_evidence": skill_evidence,
        "project_evidence": project_evidence,
        "experience_evidence": experience_evidence,
        "experience_duration": experience_duration,
        "tfidf_similarity": tfidf_similarity,
        "semantic_similarity": semantic_similarity,
        "category_analysis": category_analysis
    }

    return analysis


def summarize_final_analysis(
    analysis
):

    summary = {}

    # ---------------------------------------------
    # ROLE
    # ---------------------------------------------

    role = analysis.get("role")

    if role:

        summary["role_match"] = role.get(
            "role_match"
        )

    else:

        summary["role_match"] = None


    # ---------------------------------------------
    # REQUIRED SKILLS
    # ---------------------------------------------

    priority = analysis.get(
        "priority_skills"
    )

    if priority:

        required = priority.get(
            "required",
            {}
        )

        summary["required_skills"] = {
            "matched": required.get(
                "matched",
                []
            ),
            "missing": required.get(
                "missing",
                []
            ),
            "coverage": required.get(
                "coverage",
                0.0
            )
        }

        preferred = priority.get(
            "preferred",
            {}
        )

        summary["preferred_skills"] = {
            "matched": preferred.get(
                "matched",
                []
            ),
            "missing": preferred.get(
                "missing",
                []
            ),
            "coverage": preferred.get(
                "coverage",
                0.0
            )
        }

    else:

        summary["required_skills"] = None
        summary["preferred_skills"] = None


    # ---------------------------------------------
    # TEXT SIMILARITY
    # ---------------------------------------------

    summary["tfidf_similarity"] = (
        analysis.get(
            "tfidf_similarity"
        )
    )

    summary["semantic_similarity"] = (
        analysis.get(
            "semantic_similarity"
        )
    )


    # ---------------------------------------------
    # EVIDENCE
    # ---------------------------------------------

    summary["skill_evidence_available"] = (
        analysis.get(
            "skill_evidence"
        ) is not None
    )

    summary["project_evidence_available"] = (
        analysis.get(
            "project_evidence"
        ) is not None
    )

    summary["experience_evidence_available"] = (
        analysis.get(
            "experience_evidence"
        ) is not None
    )

    summary["experience_duration_available"] = (
        analysis.get(
            "experience_duration"
        ) is not None
    )


    # ---------------------------------------------
    # CATEGORY ANALYSIS
    # ---------------------------------------------

    summary["category_analysis_available"] = (
        analysis.get(
            "category_analysis"
        ) is not None
    )


    return summary