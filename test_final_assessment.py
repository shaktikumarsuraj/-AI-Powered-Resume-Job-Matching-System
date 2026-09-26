from final_assessment import (
    build_final_assessment
)


analysis = {

    "role": {

        "detected_role": "software engineer",

        "normalized_role": "software_developer",

        "role_match": True
    },


    "priority_skills": {

        "required": {

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
    },


    "skill_evidence": {

        "python": "strong",

        "c++": "strong"
    },


    "project_evidence": {

        "python": [
            "JAARVIS"
        ]
    },


    "experience_evidence": {

        "python": "experience"
    },


    "experience_duration": [

        {
            "skill": "python",

            "required_years": 2,

            "required_months": 24,

            "resume_months": 0,

            "duration_unknown": False,

            "status": "not met"
        },

        {
            "skill": "generative ai",

            "required_years": 1,

            "required_months": 12,

            "resume_months": 0,

            "duration_unknown": False,

            "status": "not met"
        }
    ],


    "tfidf_similarity": 0.2657,

    "semantic_similarity": 0.4122,


    "category_analysis": {

        "programming_languages": {

            "matched": [
                "python",
                "c++"
            ],

            "missing": []
        }
    }
}


assessment = build_final_assessment(
    analysis
)


print("\nFINAL ASSESSMENT")
print("=" * 60)


print("\nROLE")
print("-" * 60)

print(
    "Status:",
    assessment["role"]["status"]
)


print("\nREQUIRED SKILLS")
print("-" * 60)

required = assessment[
    "required_skills"
]

print(
    "Status:",
    required["status"]
)

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

preferred = assessment[
    "preferred_skills"
]

print(
    "Status:",
    preferred["status"]
)

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


print("\nEXPERIENCE REQUIREMENTS")
print("-" * 60)

for result in assessment[
    "experience_requirements"
]:

    print(
        f"{result['skill']}: "
        f"{result['status']}"
    )


print("\nEVIDENCE")
print("-" * 60)

print(
    "Skill:",
    assessment["evidence"]["skill"]
)

print(
    "Project:",
    assessment["evidence"]["project"]
)

print(
    "Experience:",
    assessment["evidence"]["experience"]
)


print("\nSIMILARITY")
print("-" * 60)

print(
    f"TF-IDF: "
    f"{assessment['similarity']['tfidf'] * 100:.2f} %"
)

print(
    f"Semantic: "
    f"{assessment['similarity']['semantic'] * 100:.2f} %"
)