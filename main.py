"""AI-Powered Resume–Job Matching System

Reusable matching engine plus console entry point.
"""


# =================================================
# IMPORTS
# =================================================

from read import extract_text_from_pdf

from preprocess import clean_text

from job_description import (
    get_job_description,
    extract_job_role,
    normalize_job_role,
    get_structured_job_description,
)

from matcher import calculate_similarity

from skills import (
    extract_skills,
    compare_skills,
    calculate_skill_match,
    extract_skills_by_category,
    compare_skills_by_category,
    calculate_priority_skill_match,
    extract_skills_from_sections,
    find_skill_evidence,
    calculate_evidence_strength,
    summarize_evidence_strength
)

from semantic_matcher import calculate_semantic_similarity

from role_matcher import calculate_role_match

from skill_priority import classify_skill_priority

from report import generate_report

from analysis import generate_analysis

from section_parser import (
    parse_resume_sections
)

from project_relevance import (
    find_relevant_sections,
    extract_project_evidence,
)

from experience_relevance import (
    find_experience_evidence
)


# -------------------------------------------------
# STEP 25 / EXPERIENCE REQUIREMENTS
# -------------------------------------------------

from experience_requirements import (
    extract_experience_requirements
)

from experience_duration import (
    extract_experience_section,
    extract_experience_entries
)

from experience_skill_duration import (
    compare_experience_requirements
)


# -------------------------------------------------
# STEP 26 / PRIORITY DETECTION
# -------------------------------------------------

from priority_detection import (
    extract_skill_priorities
)

from priority_skill_analysis import (
    analyze_priority_skills
)


# -------------------------------------------------
# STEP 27 / FINAL MATCHING FRAMEWORK
# -------------------------------------------------

from final_matching_analysis import (
    build_final_matching_analysis,
    summarize_final_analysis
)

from final_assessment import (
    build_final_assessment
)

from matching_insights import (
    generate_matching_insights
)


# =================================================
# MAIN REUSABLE ENGINE
# =================================================

def analyze_resume(
    resume_path,
    job_description=None,
    mode="1"
):

    file_path = resume_path


    # =================================================
    # RESUME EXTRACTION
    # =================================================

    resume_text = extract_text_from_pdf(
        file_path
    )

    clean_resume = clean_text(
        resume_text
    )


    # =================================================
    # RESUME SECTION PARSING
    # =================================================

    resume_sections = parse_resume_sections(
        resume_text
    )


    # =================================================
    # SECTION-WISE SKILLS
    # =================================================

    section_skills = extract_skills_from_sections(
        resume_sections
    )

    print("\nSECTION-WISE SKILLS")

    for section, skills in section_skills.items():

        if skills:

            print(
                f"{section}: "
                f"{', '.join(skills)}"
            )


    # =================================================
    # JOB INPUT
    # =================================================

    if mode == "1":

        if job_description is None:

            job_description = get_job_description()

        job_role = extract_job_role(
            job_description
        )

        normalized_role = normalize_job_role(
            job_role
        )

        clean_job_description = clean_text(
            job_description
        )

        required_skills = None
        preferred_skills = None


    # =================================================
    # STRUCTURED MODE
    # =================================================

    elif mode == "2":

        (
            job_role,
            structured_required_skills,
            structured_preferred_skills,
            job_description
        ) = get_structured_job_description()

        normalized_role = normalize_job_role(
            job_role
        )

        clean_job_description = clean_text(
            job_description
        )


    # =================================================
    # INVALID MODE
    # =================================================

    else:

        raise ValueError(
            "Invalid mode. "
            "Use 1 for Natural Language JD "
            "or 2 for Structured Job Input."
        )


    # =================================================
    # ROLE MATCHING
    # =================================================

    role_match = calculate_role_match(
        clean_resume,
        normalized_role
    )


    # =================================================
    # TF-IDF SIMILARITY
    # =================================================

    score = calculate_similarity(
        clean_resume,
        clean_job_description
    )


    # =================================================
    # SEMANTIC SIMILARITY
    # =================================================

    semantic_score = calculate_semantic_similarity(
        clean_resume,
        clean_job_description
    )


    # =================================================
    # SKILL EXTRACTION
    # =================================================

    resume_skills = extract_skills(
        clean_resume
    )

    job_skills = extract_skills(
        clean_job_description
    )


    # =================================================
    # PROJECT / EXPERIENCE RELEVANCE
    # =================================================

    relevant_sections = find_relevant_sections(
        job_skills,
        resume_sections
    )

    project_evidence = extract_project_evidence(
        job_skills,
        resume_sections
    )

    experience_evidence = find_experience_evidence(
        job_skills,
        resume_sections
    )


    # =================================================
    # EXPERIENCE EVIDENCE DISPLAY
    # =================================================

    print("\nEXPERIENCE EVIDENCE")

    print("-" * 50)

    if experience_evidence:

        for skill, sections in experience_evidence.items():

            if sections:

                print(
                    f"{skill}: "
                    f"{', '.join(sections)}"
                )

            else:

                print(
                    f"{skill}: "
                    f"No experience evidence found"
                )

    else:

        print(
            "No experience evidence found "
            "for the detected job skills."
        )


    # =================================================
    # RAW EXPERIENCE SECTION
    # =================================================

    print("\nRAW EXPERIENCE SECTION")

    print("-" * 50)

    print(
        resume_sections.get(
            "experience",
            "No experience section found"
        )
    )

    print(
        resume_sections.get(
            "work experience",
            ""
        )
    )


    # =================================================
    # PROJECT EVIDENCE
    # =================================================

    print("\nPROJECT EVIDENCE")

    print("-" * 50)

    for skill, projects in project_evidence.items():

        print(
            f"{skill}:"
        )

        for project in projects:

            print(
                f"  → {project}"
            )


    # =================================================
    # RAW PROJECT SECTION
    # =================================================

    print("\nRAW PROJECT SECTION")

    print("-" * 50)

    print(
        resume_sections.get(
            "projects",
            "No projects section found"
        )
    )


    # =================================================
    # PROJECT / EXPERIENCE RELEVANCE
    # =================================================

    print(
        "\nPROJECT / EXPERIENCE RELEVANCE"
    )

    for skill, sections in relevant_sections.items():

        print(
            f"{skill}: "
            f"{', '.join(sections)}"
        )


    # =================================================
    # SKILL EVIDENCE
    # =================================================

    skill_evidence = {}

    for skill in resume_skills:

        skill_evidence[skill] = (
            find_skill_evidence(
                skill,
                resume_sections
            )
        )


    # =================================================
    # EVIDENCE STRENGTH
    # =================================================

    evidence_strength = {}

    for skill, sections in skill_evidence.items():

        evidence_strength[skill] = (
            calculate_evidence_strength(
                skill,
                sections
            )
        )


    # =================================================
    # EVIDENCE SUMMARY
    # =================================================

    evidence_summary = {}

    for skill, strength_data in evidence_strength.items():

        evidence_summary[skill] = (
            summarize_evidence_strength(
                strength_data
            )
        )


    # =================================================
    # GENERAL SKILL MATCHING
    # =================================================

    matched_skills, missing_skills = compare_skills(
        resume_skills,
        job_skills
    )

    skill_score = calculate_skill_match(
        matched_skills,
        job_skills
    )


    # =================================================
    # OLD PRIORITY SYSTEM
    # =================================================

    if mode == "1":

        (
            required_skills,
            preferred_skills,
            unclassified_skills
        ) = classify_skill_priority(
            clean_job_description,
            job_skills
        )

    elif mode == "2":

        required_skills = structured_required_skills

        preferred_skills = structured_preferred_skills

        unclassified_skills = []


    # =================================================
    # EXISTING PRIORITY MATCHING
    # =================================================

    (
        matched_required,
        missing_required,
        required_score,
        matched_preferred,
        missing_preferred,
        preferred_score
    ) = calculate_priority_skill_match(
        resume_skills,
        required_skills,
        preferred_skills
    )


    # =================================================
    # STEP 26 / NEW PRIORITY DETECTION
    # =================================================

    priority_results = extract_skill_priorities(
        job_description
    )

    priority_analysis = analyze_priority_skills(
        priority_results,
        resume_skills
    )


    # =================================================
    # CATEGORY-WISE SKILLS
    # =================================================

    resume_category_skills = extract_skills_by_category(
        clean_resume
    )

    job_category_skills = extract_skills_by_category(
        clean_job_description
    )

    category_comparison = compare_skills_by_category(
        resume_category_skills,
        job_category_skills
    )


    # =================================================
    # STEP 25 / EXPERIENCE REQUIREMENTS
    # =================================================

    experience_requirements = (
        extract_experience_requirements(
            job_description
        )
    )


    # =================================================
    # STEP 25b / EXPERIENCE DURATION
    # =================================================

    experience_text = extract_experience_section(
        resume_text
    )

    experience_entries = extract_experience_entries(
        experience_text
    )


    # =================================================
    # EXPERIENCE DURATION COMPARISON
    # =================================================

    experience_duration_results = (
        compare_experience_requirements(
            experience_requirements,
            experience_entries
        )
    )


    # =================================================
    # EXISTING ANALYSIS
    # =================================================

    analysis = generate_analysis(
        role_match,
        required_score,
        preferred_score,
        semantic_score,
        skill_score,
        missing_required,
        missing_preferred,
    )


    # =================================================
    # STEP 27 / FINAL MATCHING ANALYSIS
    # =================================================

    final_analysis = build_final_matching_analysis(

        role_analysis={
            "detected_role": job_role,
            "normalized_role": normalized_role,
            "role_match": role_match
        },

        priority_analysis=priority_analysis,

        skill_evidence=skill_evidence,

        project_evidence=project_evidence,

        experience_evidence=experience_evidence,

        experience_duration=experience_duration_results,

        tfidf_similarity=score,

        semantic_similarity=semantic_score,

        category_analysis=category_comparison
    )


    # =================================================
    # FINAL ANALYSIS SUMMARY
    # =================================================

    final_summary = summarize_final_analysis(
        final_analysis
    )


    # =================================================
    # STEP 27 / FINAL ASSESSMENT
    # =================================================

    final_assessment = build_final_assessment(
        final_analysis
    )


    # =================================================
    # STEP 27 / FINAL MATCHING INSIGHTS
    # =================================================

    final_insights = generate_matching_insights(
        final_analysis
    )


    # =================================================
    # FINAL MATCHING FRAMEWORK DISPLAY
    # =================================================

    print("\nFINAL MATCHING FRAMEWORK")

    print("=" * 60)


    # =================================================
    # ROLE STATUS
    # =================================================

    print("\nROLE STATUS")

    print("-" * 60)

    print(
        "Detected Role:",
        job_role
    )

    print(
        "Normalized Role:",
        normalized_role
    )

    print(
        "Status:",
        final_assessment["role"]["status"]
    )


    # =================================================
    # REQUIRED SKILLS
    # =================================================

    print("\nREQUIRED SKILLS STATUS")

    print("-" * 60)

    required_assessment = (
        final_assessment["required_skills"]
    )

    print(
        "Status:",
        required_assessment["status"]
    )

    print(
        "Matched:",
        ", ".join(
            required_assessment.get(
                "matched",
                []
            )
        )
        if required_assessment.get("matched")
        else "None"
    )

    print(
        "Missing:",
        ", ".join(
            required_assessment.get(
                "missing",
                []
            )
        )
        if required_assessment.get("missing")
        else "None"
    )

    print(
        f"Coverage: "
        f"{required_assessment.get('coverage', 0.0):.2f} %"
    )


    # =================================================
    # PREFERRED SKILLS
    # =================================================

    print("\nPREFERRED SKILLS STATUS")

    print("-" * 60)

    preferred_assessment = (
        final_assessment["preferred_skills"]
    )

    print(
        "Status:",
        preferred_assessment["status"]
    )

    print(
        "Matched:",
        ", ".join(
            preferred_assessment.get(
                "matched",
                []
            )
        )
        if preferred_assessment.get("matched")
        else "None"
    )

    print(
        "Missing:",
        ", ".join(
            preferred_assessment.get(
                "missing",
                []
            )
        )
        if preferred_assessment.get("missing")
        else "None"
    )

    print(
        f"Coverage: "
        f"{preferred_assessment.get('coverage', 0.0):.2f} %"
    )


    # =================================================
    # EXPERIENCE REQUIREMENTS
    # =================================================

    print("\nEXPERIENCE REQUIREMENTS")

    print("-" * 60)

    if final_assessment["experience_requirements"]:

        for result in final_assessment[
            "experience_requirements"
        ]:

            print(
                f"Skill: {result['skill']}"
            )

            print(
                f"Required: "
                f"{result['required_years']} years"
            )

            print(
                f"Resume Experience: "
                f"{result['resume_months']} months"
            )

            print(
                f"Status: "
                f"{result['status']}"
            )

            print()

    else:

        print(
            "No explicit experience requirements detected."
        )


    # =================================================
    # TEXT SIMILARITY
    # =================================================

    print("\nTEXT SIMILARITY")

    print("-" * 60)

    print(
        f"TF-IDF Similarity: "
        f"{score * 100:.2f} %"
    )

    print(
        f"Semantic Similarity: "
        f"{semantic_score * 100:.2f} %"
    )


    # =================================================
    # EVIDENCE AVAILABILITY
    # =================================================

    print("\nEVIDENCE AVAILABILITY")

    print("-" * 60)

    print(
        "Skill Evidence:",
        final_assessment["evidence"]["skill"]
    )

    print(
        "Project Evidence:",
        final_assessment["evidence"]["project"]
    )

    print(
        "Experience Evidence:",
        final_assessment["evidence"]["experience"]
    )


    # =================================================
    # MATCHING INSIGHTS
    # =================================================

    print("\nMATCHING INSIGHTS")

    print("-" * 60)

    for insight in final_insights:

        print(
            f"• {insight}"
        )


    # =================================================
    # FINAL REPORT
    # =================================================

    generate_report(
        job_role,
        normalized_role,
        role_match,
        matched_skills,
        missing_skills,
        skill_score,
        score,
        semantic_score,
        category_comparison,
        matched_required,
        missing_required,
        required_score,
        matched_preferred,
        missing_preferred,
        preferred_score,
        unclassified_skills,
        final_insights,
        skill_evidence,
        evidence_strength,
        evidence_summary,
        project_evidence
    )


    # =================================================
    # RETURN ALL RESULTS
    # =================================================

    return {

        "resume_path": resume_path,

        "job_description": job_description,

        "resume_text": resume_text,

        "clean_resume": clean_resume,

        "resume_sections": resume_sections,

        "section_skills": section_skills,

        "job_role": job_role,

        "normalized_role": normalized_role,

        "role_match": role_match,

        "resume_skills": resume_skills,

        "job_skills": job_skills,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "skill_score": skill_score,

        "required_skills": required_skills,

        "preferred_skills": preferred_skills,

        "matched_required": matched_required,

        "missing_required": missing_required,

        "required_score": required_score,

        "matched_preferred": matched_preferred,

        "missing_preferred": missing_preferred,

        "preferred_score": preferred_score,

        "unclassified_skills": unclassified_skills,

        "priority_results": priority_results,

        "priority_analysis": priority_analysis,

        "skill_evidence": skill_evidence,

        "evidence_strength": evidence_strength,

        "evidence_summary": evidence_summary,

        "project_evidence": project_evidence,

        "experience_evidence": experience_evidence,

        "relevant_sections": relevant_sections,

        "category_comparison": category_comparison,

        "experience_requirements": experience_requirements,

        "experience_duration": experience_duration_results,

        "tfidf_similarity": score,

        "semantic_similarity": semantic_score,

        "final_analysis": final_analysis,

        "final_summary": final_summary,

        "final_assessment": final_assessment,

        "final_insights": final_insights
    }


# =================================================
# CONSOLE ENTRY POINT
# =================================================

def run_matching_engine():

    print(
        "\n========== RESUME-JOB MATCHING SYSTEM =========="
    )


    # -------------------------------------------------
    # RESUME PATH
    # -------------------------------------------------

    resume_path = input(
        "Enter resume PDF path: "
    ).strip()


    # -------------------------------------------------
    # JOB INPUT MODE
    # -------------------------------------------------

    print(
        "\n========== JOB INPUT MODE =========="
    )

    print(
        "1. Natural Language JD"
    )

    print(
        "2. Structured Job Input"
    )


    mode = input(
        "\nChoose mode (1/2): "
    ).strip()


    # -------------------------------------------------
    # RUN ENGINE
    # -------------------------------------------------

    if mode == "1":

        results = analyze_resume(
            resume_path,
            mode="1"
        )

    elif mode == "2":

        results = analyze_resume(
            resume_path,
            mode="2"
        )

    else:

        print(
            "Invalid choice."
        )

        return None


    return results


# =================================================
# PROGRAM ENTRY
# =================================================

if __name__ == "__main__":

    run_matching_engine()