from priority_detection import (
    extract_skill_priorities
)

from priority_skill_analysis import (
    analyze_priority_skills
)


# -------------------------------------------------
# JOB DESCRIPTION
# -------------------------------------------------

job_description = """
Python is required.

Candidates must have C++.

SQL proficiency is mandatory.

Experience with LangChain is preferred.

Knowledge of Docker is nice to have.

Kubernetes would be a plus.

Git experience is a bonus.
"""


# -------------------------------------------------
# RESUME SKILLS
#
# Assume these skills were already extracted
# by our existing resume skill extraction system.
# -------------------------------------------------

resume_skills = [
    "Python",
    "C++",
    "LangChain",
    "Git"
]


# -------------------------------------------------
# STEP 1
# DETECT SKILL PRIORITIES FROM JD
# -------------------------------------------------

priority_results = extract_skill_priorities(
    job_description
)


# -------------------------------------------------
# STEP 2
# ANALYZE REQUIRED / PREFERRED SKILLS
# -------------------------------------------------

analysis = analyze_priority_skills(
    priority_results,
    resume_skills
)


# -------------------------------------------------
# REQUIRED SKILLS
# -------------------------------------------------

print("\nREQUIRED SKILLS")
print("-" * 60)

print(
    "All:",
    ", ".join(
        analysis["required"]["all"]
    )
)

print(
    "Matched:",
    ", ".join(
        analysis["required"]["matched"]
    )
    if analysis["required"]["matched"]
    else "None"
)

print(
    "Missing:",
    ", ".join(
        analysis["required"]["missing"]
    )
    if analysis["required"]["missing"]
    else "None"
)

print(
    f"Coverage: "
    f"{analysis['required']['coverage']:.2f} %"
)


# -------------------------------------------------
# PREFERRED SKILLS
# -------------------------------------------------

print("\nPREFERRED SKILLS")
print("-" * 60)

print(
    "All:",
    ", ".join(
        analysis["preferred"]["all"]
    )
)

print(
    "Matched:",
    ", ".join(
        analysis["preferred"]["matched"]
    )
    if analysis["preferred"]["matched"]
    else "None"
)

print(
    "Missing:",
    ", ".join(
        analysis["preferred"]["missing"]
    )
    if analysis["preferred"]["missing"]
    else "None"
)

print(
    f"Coverage: "
    f"{analysis['preferred']['coverage']:.2f} %"
)