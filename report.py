def generate_report(
    job_role,
    normalized_role,
    role_match,
    matched_skills,
    missing_skills,
    skill_score,
    similarity_score,
    semantic_score,
    category_comparison,
    matched_required,
    missing_required,
    required_score,
    matched_preferred,
    missing_preferred,
    preferred_score,
    unclassified_skills,
    analysis,
    skill_evidence,
    evidence_strength,
    evidence_summary,
    project_evidence
):

    print("\n")
    print("=" * 60)
    print("          RESUME - JOB MATCHING REPORT")
    print("=" * 60)

    # =================================================
    # ROLE
    # =================================================

    print("\nROLE")
    print("-" * 60)

    print("Detected Role   :", job_role)
    print("Normalized Role :", normalized_role)
    print(
        "Role Match      :",
        "Yes" if role_match else "No"
    )


    # =================================================
    # REQUIRED / PREFERRED SKILLS
    # =================================================

    required_matched = []
    required_missing = []

    preferred_matched = []
    preferred_missing = []

    for insight in analysis:
        pass

    # -------------------------------------------------
    # NOTE:
    # `analysis` now contains final_insights.
    # Therefore the authoritative skill information
    # remains the FINAL MATCHING FRAMEWORK printed
    # by main.py.
    # -------------------------------------------------

    print("\nSKILL MATCHING")
    print("-" * 60)

    if matched_skills:
        print(
            "Matched Skills  :",
            ", ".join(matched_skills)
        )
    else:
        print("Matched Skills  : None")

    if missing_skills:
        print(
            "Missing Skills  :",
            ", ".join(missing_skills)
        )
    else:
        print("Missing Skills  : None")

    print(
        "Overall Coverage:",
        f"{skill_score * 100:.2f} %"
    )


    # =================================================
    # SKILL EVIDENCE
    # =================================================

    print("\nSKILL EVIDENCE")
    print("-" * 60)

    if matched_skills:

        for skill in matched_skills:

            sections = skill_evidence.get(
                skill,
                []
            )

            summary = evidence_summary.get(
                skill,
                "none"
            )

            print(f"\n{skill}")

            print(
                "  Overall Evidence:",
                summary
            )

            project_names = project_evidence.get(
                skill,
                []
            )

            if project_names:

                print("  Project Evidence:")

                for project in project_names:

                    print(
                        f"    → {project}"
                    )

            if sections:

                for section in sections:

                    strength = (
                        evidence_strength
                        .get(skill, {})
                        .get(
                            section,
                            "supporting"
                        )
                    )

                    print(
                        f"  {section}: "
                        f"{strength}"
                    )

            else:

                print(
                    "  No section evidence found"
                )

    else:

        print(
            "No matched skills available."
        )


    # =================================================
    # CATEGORY ANALYSIS
    # =================================================

    print("\nCATEGORY ANALYSIS")
    print("-" * 60)

    category_found = False

    for category, result in category_comparison.items():

        if (
            result.get("matched")
            or result.get("missing")
        ):

            category_found = True

            print(f"\n{category}")

            if result.get("matched"):

                print(
                    "  Matched:",
                    ", ".join(
                        result["matched"]
                    )
                )

            if result.get("missing"):

                print(
                    "  Missing:",
                    ", ".join(
                        result["missing"]
                    )
                )

    if not category_found:

        print("No category-level matches found.")


    # =================================================
    # TEXT SIMILARITY
    # =================================================

    print("\nTEXT SIMILARITY")
    print("-" * 60)

    print(
        "TF-IDF Similarity     :",
        f"{similarity_score * 100:.2f} %"
    )

    print(
        "Semantic Similarity   :",
        f"{semantic_score * 100:.2f} %"
    )


    # =================================================
    # MATCHING INSIGHTS
    # =================================================

    print("\nMATCHING INSIGHTS")
    print("-" * 60)

    if analysis:

        for insight in analysis:

            print(
                f"• {insight}"
            )

    else:

        print("No additional insights available.")


    # =================================================
    # END
    # =================================================

    print("\n" + "=" * 60)