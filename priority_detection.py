import re


REQUIRED_PATTERNS = [
    r"\brequired\b",
    r"\bmust have\b",
    r"\bmust possess\b",
    r"\bmandatory\b",
    r"\bessential\b",
    r"\bminimum requirement\b",
    r"\bneed to have\b",
    r"\bshould have\b",
    r"\bstrong knowledge of\b",
    r"\bstrong experience with\b",
    r"\bproficiency in\b",
    r"\bproficient in\b",
    r"\bexpertise in\b",
    r"\bsolid knowledge of\b"
]


PREFERRED_PATTERNS = [
    r"\bpreferred\b",
    r"\bpreferably\b",
    r"\bnice to have\b",
    r"\bgood to have\b",
    r"\bwould be a plus\b",
    r"\ba plus\b",
    r"\bplus\b",
    r"\bbonus\b",
    r"\bdesirable\b",
    r"\bdesired\b",
    r"\boptional\b",
    r"\badvantage\b",
    r"\bwould be beneficial\b"
]


def detect_priority(text):

    text = text.lower().strip()

    for pattern in REQUIRED_PATTERNS:

        if re.search(
            pattern,
            text
        ):
            return "required"

    for pattern in PREFERRED_PATTERNS:

        if re.search(
            pattern,
            text
        ):
            return "preferred"

    return "unspecified"


def clean_extracted_skill(skill):

    skill = skill.strip()

    # Remove priority phrases from the beginning
    prefixes = [
        r"^strong\s+knowledge\s+of\s+",
        r"^solid\s+knowledge\s+of\s+",
        r"^strong\s+experience\s+with\s+",
        r"^experience\s+with\s+",
        r"^knowledge\s+of\s+",
        r"^proficiency\s+in\s+",
        r"^expertise\s+in\s+",
        r"^proficient\s+in\s+"
    ]

    for prefix in prefixes:

        skill = re.sub(
            prefix,
            "",
            skill,
            flags=re.IGNORECASE
        )

    # Remove trailing punctuation
    skill = re.sub(
        r"[.,;:]+$",
        "",
        skill
    )

    # Normalize multiple spaces
    skill = re.sub(
        r"\s+",
        " ",
        skill
    )

    return skill.strip()


def split_skills(skill_text):

    skill_text = clean_extracted_skill(
        skill_text
    )

    # Convert:
    # "Pandas, NumPy and Scikit-learn"
    #
    # into:
    # "Pandas, NumPy, Scikit-learn"

    skill_text = re.sub(
        r"\s+and\s+",
        ",",
        skill_text,
        flags=re.IGNORECASE
    )

    parts = skill_text.split(",")

    skills = []

    for part in parts:

        part = clean_extracted_skill(
            part
        )

        if part:

            skills.append(
                part
            )

    return skills


def extract_skill_from_sentence(
    sentence
):

    text = sentence.strip()

    # -----------------------------------------
    # Experience requirement
    # -----------------------------------------
    # Example:
    # 2 years of experience with FastAPI
    # At least 1 year of experience with SQL
    #
    # These are handled separately by
    # experience_requirements.py
    # so they must NOT become priority skills.
    # -----------------------------------------

    experience_pattern = (
        r"(?:"
        r"\d+\+?\s*years?\s+of\s+experience\s+"
        r"(?:with|in)\s+.+?"
        r"(?:\s+is\s+(?:required|mandatory|essential))?"
        r"$"
        r"|"
        r"at\s+least\s+\d+\s+years?\s+"
        r"(?:of\s+)?experience\s+"
        r"(?:with|in)\s+.+?"
        r"(?:\s+is\s+(?:required|mandatory|essential))?"
        r"$"
        r")"
    )

    if re.search(
        experience_pattern,
        text,
        re.IGNORECASE
    ):
        return []

    # -----------------------------------------
    # Python is required
    # -----------------------------------------

    match = re.search(
        r"^(.+?)\s+is\s+"
        r"(?:required|mandatory|essential)\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # SQL proficiency is mandatory
    # -----------------------------------------

    match = re.search(
        r"^(.+?)\s+proficiency\s+is\s+"
        r"(?:required|mandatory|essential)\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # proficiency in SQL is mandatory
    # -----------------------------------------

    match = re.search(
        r"proficiency\s+in\s+(.+?)\s+is\s+"
        r"(?:required|mandatory|essential)\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # Candidates must have C++
    # -----------------------------------------

    match = re.search(
        r"(?:must\s+have|must\s+possess|"
        r"need\s+to\s+have)\s+(.+?)(?:\.|$)",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # Strong knowledge of X is required
    # -----------------------------------------

    match = re.search(
        r"strong\s+knowledge\s+of\s+(.+?)"
        r"\s+is\s+required\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # Strong knowledge of X is essential
    # -----------------------------------------

    match = re.search(
        r"strong\s+knowledge\s+of\s+(.+?)"
        r"\s+is\s+essential\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # Strong knowledge of X is mandatory
    # -----------------------------------------

    match = re.search(
        r"strong\s+knowledge\s+of\s+(.+?)"
        r"\s+is\s+mandatory\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # Experience with LangChain is preferred
    # -----------------------------------------

    match = re.search(
        r"experience\s+with\s+(.+?)\s+is\s+"
        r"(?:preferred|desirable|desired)\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # Knowledge of Docker is nice to have
    # -----------------------------------------

    match = re.search(
        r"knowledge\s+of\s+(.+?)\s+is\s+"
        r"(?:nice\s+to\s+have|good\s+to\s+have)\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # Kubernetes would be a plus
    # -----------------------------------------

    match = re.search(
        r"^(.+?)\s+would\s+be\s+a\s+plus\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # Git experience is a bonus
    # -----------------------------------------

    match = re.search(
        r"(.+?)\s+experience\s+is\s+a\s+bonus\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    # -----------------------------------------
    # Knowledge of X is a plus
    # -----------------------------------------

    match = re.search(
        r"knowledge\s+of\s+(.+?)\s+is\s+a\s+plus\b",
        text,
        re.IGNORECASE
    )

    if match:

        return split_skills(
            match.group(1)
        )

    return []


def prepare_sentences(
    job_description
):

    # Remove unnecessary line breaks.
    #
    # Example:
    #
    # "strong knowledge of
    # Pandas, NumPy and Scikit-learn."
    #
    # becomes:
    #
    # "strong knowledge of Pandas, NumPy and Scikit-learn."

    text = re.sub(
        r"\s+",
        " ",
        job_description
    ).strip()

    # Split on sentence-ending punctuation.

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text
    )

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


def extract_skill_priorities(
    job_description
):

    results = []

    sentences = prepare_sentences(
        job_description
    )

    for sentence in sentences:

        priority = detect_priority(
            sentence
        )

        skills = extract_skill_from_sentence(
            sentence
        )

        if not skills:
            continue

        for skill in skills:

            results.append(
                {
                    "skill": skill,
                    "priority": priority,
                    "source": sentence
                }
            )

    return results