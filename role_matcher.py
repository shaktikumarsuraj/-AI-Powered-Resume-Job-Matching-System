import json
import os


def load_roles():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "roles.json")

    with open(file_path, "r") as file:
        return json.load(file)


def calculate_role_match(resume_text, normalized_role):
    resume_text = resume_text.lower()

    role_data = load_roles()

    aliases = role_data.get(normalized_role, [])

    for alias in aliases:
        if alias in resume_text:
            return True

    return False

