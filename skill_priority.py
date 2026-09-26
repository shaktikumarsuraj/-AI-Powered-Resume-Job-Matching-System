import re


REQUIRED_KEYWORDS = [
    "required knowledge of",
    "required",
    "must have",
    "must know",
    "mandatory",
    "strong knowledge of",
    "proficiency in",
    "proficient in",
    "expertise in",
    "essential"
]


PREFERRED_KEYWORDS = [
    "optional knowledge of",
    "preferred",
    "nice to have",
    "good to have",
    "bonus",
    "plus",
    "familiarity with",
    "optional"
]


def find_priority_markers(text):
    markers = []

    all_keywords = [
        (keyword, "required")
        for keyword in REQUIRED_KEYWORDS
    ] + [
        (keyword, "preferred")
        for keyword in PREFERRED_KEYWORDS
    ]

    for keyword, priority in all_keywords:
        for match in re.finditer(
            re.escape(keyword),
            text
        ):
            markers.append(
                (match.start(), match.end(), priority)
            )

    markers.sort(key=lambda x: x[0])

    return markers


def classify_skill_priority(job_description, job_skills):

    text = job_description.lower()

    markers = find_priority_markers(text)

    required_skills = []
    preferred_skills = []
    unclassified_skills = []

    for skill in job_skills:

        skill_match = re.search(
            r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)",
            text
        )

        if not skill_match:
            unclassified_skills.append(skill)
            continue

        skill_position = skill_match.start()

        previous_markers = [
            marker
            for marker in markers
            if marker[0] < skill_position
        ]

        if not previous_markers:
            unclassified_skills.append(skill)
            continue

        nearest_marker = previous_markers[-1]

        priority = nearest_marker[2]

        if priority == "required":
            required_skills.append(skill)

        elif priority == "preferred":
            preferred_skills.append(skill)

        else:
            unclassified_skills.append(skill)

    return (
        required_skills,
        preferred_skills,
        unclassified_skills
    )