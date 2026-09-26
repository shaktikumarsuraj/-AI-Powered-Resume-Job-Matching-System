from matching_insights import (
    generate_matching_insights
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
            "JAARVIS — AI Voice Assistant"
        ],

        "c++": [
            "Student Database Management System"
        ]
    },


    "experience_evidence": {

        "python": "experience",

        "generative ai": "experience"
    },


    "experience_duration": {

        "python": {

            "skill": "python",

            "required_years": 2,

            "resume_months": 0,

            "status": "not met"
        }
    },


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


insights = generate_matching_insights(
    analysis
)


print("\nMATCHING INSIGHTS")
print("-" * 60)


for insight in insights:

    print(
        f"• {insight}"
    )