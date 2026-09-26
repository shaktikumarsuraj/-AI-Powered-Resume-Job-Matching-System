import re


SECTION_NAMES = [
    "education",
    "experience",
    "work experience",
    "skills",
    "technical skills",
    "projects",
    "achievements",
    "certifications",
    "certificates",
    "positions of responsibility",
    "interests",
    "languages" , 
    "achievements & awards",
    "awards & achievements"
]


def detect_section_heading(line):
    clean_line = line.strip().lower()

    if not clean_line:
        return None

    # Normal heading match
    for section in SECTION_NAMES:
        if clean_line == section:
            return section

    # Handle PDF extraction errors such as:
    # "A w ards & Achievements"
    normalized_line = re.sub(r"\s+", "", clean_line)

    for section in SECTION_NAMES:
        normalized_section = re.sub(r"\s+", "", section)

        if normalized_line == normalized_section:
            return section

    return None


def parse_resume_sections(text):

    lines = text.splitlines()

    sections = {}
    current_section = "general"

    sections[current_section] = []

    for line in lines:

        section = detect_section_heading(line)

        if section:

            current_section = section

            if current_section not in sections:
                sections[current_section] = []

        else:

            if line.strip():
                sections[current_section].append(
                    line.strip()
                )

    for section in sections:

        sections[section] = " ".join(
            sections[section]
        )

    return sections