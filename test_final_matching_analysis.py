from final_matching_analysis import (
    build_final_matching_analysis,
    summarize_final_analysis
)


# -------------------------------------------------
# ROLE ANALYSIS
# -------------------------------------------------

role_analysis = {

    "detected_role": "software engineer",

    "normalized_role": "software_developer",

    "role_match": True
}


# -------------------------------------------------
# PRIORITY-AWARE SKILL ANALYSIS
# -------------------------------------------------

priority_analysis = {

    "required": {

        "all": [
            "python",
            "c++",
            "sql"
        ],

        "matched": [
            "python",
            "c++"
        ],

        "missing": [
            "sql"
        ],

        "coverage": 66.67
    },

    "preferred": {

        "all": [
            "langchain",
            "docker",
            "kubernetes",
            "git"
        ],

        "matched": [
            "langchain",
            "git"
        ],

        "missing": [
            "docker",
            "kubernetes"
        ],

        "coverage": 50.00
    }
}


# -------------------------------------------------
# OTHER COMPONENT RESULTS
# -------------------------------------------------

skill_evidence = {
    "python": "strong",
    "c++": "strong",
    "sql": "none"
}


project_evidence = {
    "python": [
        "JAARVIS — AI Voice Assistant"
    ],
    "c++": [
        "Student Database Management System"
    ]
}


experience_evidence = {
    "python": "experience",
    "generative ai": "experience"
}


experience_duration = {
    "python": {
        "required_years": 2,
        "resume_months": 0,
        "status": "not met"
    }
}


category_analysis = {
    "programming_languages": {
        "matched": [
            "python",
            "c++"
        ],
        "missing": []
    },

    "databases": {
        "matched": [],
        "missing": [
            "sql"
        ]
    }
}


# -------------------------------------------------
# SIMILARITY RESULTS
# -------------------------------------------------

tfidf_similarity = 0.2657

semantic_similarity = 0.4122


# -------------------------------------------------
# BUILD FINAL ANALYSIS
# -------------------------------------------------

analysis = build_final_matching_analysis(

    role_analysis=role_analysis,

    priority_analysis=priority_analysis,

    skill_evidence=skill_evidence,

    project_evidence=project_evidence,

    experience_evidence=experience_evidence,

    experience_duration=experience_duration,

    tfidf_similarity=tfidf_similarity,

    semantic_similarity=semantic_similarity,

    category_analysis=category_analysis
)


# -------------------------------------------------
# BUILD SUMMARY
# -------------------------------------------------

summary = summarize_final_analysis(
    analysis
)


# -------------------------------------------------
# DISPLAY
# -------------------------------------------------

print("\nFINAL MATCHING ANALYSIS")
print("=" * 60)


print("\nROLE")
print("-" * 60)

print(
    "Role Match:",
    summary["role_match"]
)


print("\nREQUIRED SKILLS")
print("-" * 60)

required = summary[
    "required_skills"
]

print(
    "Matched:",
    ", ".join(
        required["matched"]
    )
)

print(
    "Missing:",
    ", ".join(
        required["missing"]
    )
)

print(
    f"Coverage: "
    f"{required['coverage']:.2f} %"
)


print("\nPREFERRED SKILLS")
print("-" * 60)

preferred = summary[
    "preferred_skills"
]

print(
    "Matched:",
    ", ".join(
        preferred["matched"]
    )
)

print(
    "Missing:",
    ", ".join(
        preferred["missing"]
    )
)

print(
    f"Coverage: "
    f"{preferred['coverage']:.2f} %"
)


print("\nTEXT SIMILARITY")
print("-" * 60)

print(
    f"TF-IDF Similarity: "
    f"{summary['tfidf_similarity'] * 100:.2f} %"
)

print(
    f"Semantic Similarity: "
    f"{summary['semantic_similarity'] * 100:.2f} %"
)


print("\nEVIDENCE")
print("-" * 60)

print(
    "Skill Evidence:",
    summary["skill_evidence_available"]
)

print(
    "Project Evidence:",
    summary["project_evidence_available"]
)

print(
    "Experience Evidence:",
    summary["experience_evidence_available"]
)

print(
    "Experience Duration:",
    summary["experience_duration_available"]
)

print(
    "Category Analysis:",
    summary["category_analysis_available"]
)