import re


def find_relevant_sections(
    job_skills,
    resume_sections
):

    relevant_sections = {}

    for skill in job_skills:

        skill = skill.lower()

        matching_sections = []

        for section, content in resume_sections.items():

            content = content.lower()

            pattern = (
                r"(?<!\w)"
                + re.escape(skill)
                + r"(?!\w)"
            )

            if re.search(pattern, content):

                if section in [
                    "projects",
                    "experience",
                    "work experience"
                ]:
                    matching_sections.append(section)

        if matching_sections:
            relevant_sections[skill] = matching_sections

    return relevant_sections


def extract_project_blocks(projects_text):

    project_blocks = []

    title_matches = re.finditer(
        r"(?:^|●\s*)([^|●]+?)\s*\|",
        projects_text
    )

    matches = list(title_matches)

    for index, match in enumerate(matches):

        project_name = match.group(1).strip()

        project_name = re.sub(
            r"^[●○•]\s*",
            "",
            project_name
        )

        project_name = re.sub(
            r"\s+",
            " ",
            project_name
        )

        start = match.start()

        if index + 1 < len(matches):
            end = matches[index + 1].start()
        else:
            end = len(projects_text)

        block = projects_text[
            start:end
        ].strip()

        project_blocks.append(
            {
                "name": project_name,
                "content": block
            }
        )

    return project_blocks


def extract_project_evidence(
    job_skills,
    resume_sections
):

    project_evidence = {}

    projects_text = resume_sections.get(
        "projects",
        ""
    )

    if not projects_text:
        return project_evidence

    project_blocks = extract_project_blocks(
        projects_text
    )

    for skill in job_skills:

        skill = skill.lower()

        pattern = (
            r"(?<!\w)"
            + re.escape(skill)
            + r"(?!\w)"
        )

        for project in project_blocks:

            if re.search(
                pattern,
                project["content"].lower()
            ):

                if skill not in project_evidence:
                    project_evidence[skill] = []

                project_evidence[skill].append(
                    project["name"]
                )

    return project_evidence
