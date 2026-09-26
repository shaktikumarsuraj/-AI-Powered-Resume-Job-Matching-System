import json
import os
import re


def get_job_description():

    print("\nEnter Job Description:")
    print("Type END on a new line when finished.\n")

    lines = []

    while True:

        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    return " ".join(lines)


def load_roles():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "roles.json")

    with open(file_path, "r") as file:
        role_data = json.load(file)

    return role_data


def extract_job_role(job_description):

    text = job_description.lower().strip()

    role_patterns = [
        r"looking for a\s+([^.]+)",
        r"looking for an\s+([^.]+)",
        r"hiring a\s+([^.]+)",
        r"hiring an\s+([^.]+)",
        r"seeking a\s+([^.]+)",
        r"seeking an\s+([^.]+)",
        r"position of\s+([^.]+)",
        r"role of\s+([^.]+)",
        r"need a\s+([^.]+)",
        r"need an\s+([^.]+)",
        r"want a\s+([^.]+)",
        r"want an\s+([^.]+)"
    ]

    for pattern in role_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            role = match.group(1).strip()

            role = re.sub(
                r"\s+",
                " ",
                role
            )

            return role

    return "not detected"


def normalize_job_role(role):
    role = role.lower().strip()

    role_data = load_roles()

    for normalized_role, aliases in role_data.items():

        if role in aliases:
            return normalized_role

    return role


def get_structured_job_description():
    print("\n========== STRUCTURED JOB INPUT ==========\n")

    job_role = input("Enter the job role:\n> ").strip()

    required_input = input(
        "Enter required skills (comma separated):\n> "
    ).strip()

    preferred_input = input(
        "Enter preferred skills (comma separated):\n> "
    ).strip()
    print("\nJob Description:")
    print("Type END on a new line when finished.\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    job_description = " ".join(lines)

    required_skills = [
        skill.strip().lower()
        for skill in required_input.split(",")
        if skill.strip()
    ]

    preferred_skills = [
        skill.strip().lower()
        for skill in preferred_input.split(",")
        if skill.strip()
    ]

    return (
        job_role,
        required_skills,
        preferred_skills,
        job_description
    )