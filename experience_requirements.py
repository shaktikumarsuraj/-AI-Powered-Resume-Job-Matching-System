import re


def extract_experience_requirements(
    job_description
):

    requirements = []

    text = job_description.lower()

    pattern = (
        r"(?:"
        r"(\d+)\+?\s*years?\s+of\s+experience\s+(?:with|in)\s+"
        r"([^\n.]+)"
        r"|"
        r"at least\s+(\d+)\s+years?\s+(?:of\s+)?experience\s+(?:with|in)\s+"
        r"([^\n.]+)"
        r"|"
        r"(\d+)\+?\s*years?\s+experience\s+(?:with|in)\s+"
        r"([^\n.]+)"
        r")"
    )

    matches = re.finditer(
        pattern,
        text
    )

    for match in matches:

        groups = match.groups()

        years = None
        skill = None

        for index in range(
            0,
            len(groups),
            2
        ):

            if groups[index] is not None:

                years = int(
                    groups[index]
                )

                skill = groups[
                    index + 1
                ].strip()

                break

        if years is None or skill is None:
            continue

        # Remove trailing punctuation
        skill = re.sub(
            r"[.,;:]+$",
            "",
            skill
        ).strip()

        # Remove accidental trailing whitespace
        skill = re.sub(
            r"\s+",
            " ",
            skill
        )

        skill = re.sub(
            r"\s+(?:is\s+)?(?:required|mandatory|essential)\s*$",
            "",
            skill,
            flags=re.IGNORECASE
        ).strip()

        requirement = {
            "skill": skill,
            "years": years,
            "type": "years"
        }

        if requirement not in requirements:

            requirements.append(
                requirement
            )

    return requirements