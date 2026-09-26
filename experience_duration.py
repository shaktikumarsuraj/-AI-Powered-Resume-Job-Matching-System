import re
from datetime import datetime


# ==================================================
# MONTH MAPPING
# ==================================================

MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12
}


# ==================================================
# MONTH REGEX PATTERN
# ==================================================

MONTH_PATTERN = (
    r"(jan(?:uary)?|"
    r"feb(?:ruary)?|"
    r"mar(?:ch)?|"
    r"apr(?:il)?|"
    r"may|"
    r"jun(?:e)?|"
    r"jul(?:y)?|"
    r"aug(?:ust)?|"
    r"sep(?:tember)?|"
    r"oct(?:ober)?|"
    r"nov(?:ember)?|"
    r"dec(?:ember)?)"
)


# ==================================================
# CALCULATE DURATION
# ==================================================

def calculate_duration(
    start_month,
    start_year,
    end_month,
    end_year
):

    start_date = datetime(
        start_year,
        start_month,
        1
    )

    end_date = datetime(
        end_year,
        end_month,
        1
    )

    months = (
        (end_date.year - start_date.year) * 12
        + (end_date.month - start_date.month)
    )

    return max(months, 0)


# ==================================================
# EXTRACT EXPERIENCE SECTION
# ==================================================

def extract_experience_section(text):

    """
    Extract the actual EXPERIENCE section
    from the resume.
    """

    text = text.replace(
        "\r",
        "\n"
    )

    text = text.replace(
        "\xa0",
        " "
    )

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    # ----------------------------------------------
    # Find EXPERIENCE heading
    # ----------------------------------------------

    start_index = None

    for index, line in enumerate(lines):

        clean_line = re.sub(
            r"^[•●○▪■\-\s]+",
            "",
            line
        )

        clean_line = (
            clean_line
            .strip()
            .lower()
        )

        if clean_line == "experience":

            start_index = index + 1
            break

    if start_index is None:

        return ""


    # ----------------------------------------------
    # Possible next section headings
    # ----------------------------------------------

    section_headings = {
        "education",
        "technical skills",
        "skills",
        "projects",
        "achievements",
        "achievements & certification",
        "achievements & activities",
        "achievements & awards",
        "certification",
        "certifications",
        "interests",
        "languages"
    }


    # ----------------------------------------------
    # Find end of EXPERIENCE section
    # ----------------------------------------------

    end_index = len(lines)

    for index in range(
        start_index,
        len(lines)
    ):

        clean_line = re.sub(
            r"^[•●○▪■\-\s]+",
            "",
            lines[index]
        )

        clean_line = (
            clean_line
            .strip()
            .lower()
        )

        if clean_line in section_headings:

            end_index = index
            break


    # ----------------------------------------------
    # Return section
    # ----------------------------------------------

    experience_lines = lines[
        start_index:end_index
    ]

    return "\n".join(
        experience_lines
    )


# ==================================================
# EXTRACT EXPERIENCE ENTRIES
# ==================================================

def extract_experience_entries(text):

    """
    Extract individual experience entries
    from the EXPERIENCE section.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]


    # ==================================================
    # DATE PATTERN
    # ==================================================

    date_pattern = re.compile(
        rf"{MONTH_PATTERN}\s+(\d{{4}})"
        rf"\s*[–—-]\s*"
        rf"(present|{MONTH_PATTERN})"
        rf"(?:\s+(\d{{4}}))?",
        re.IGNORECASE
    )


    # ==================================================
    # ROLE PATTERN
    # ==================================================

    role_pattern = re.compile(
        r"^.+?\s+[—–-]\s+.+$"
    )


    # ==================================================
    # CREATE EXPERIENCE BLOCKS
    # ==================================================

    blocks = []

    current_block = []


    for line in lines:

        is_role = bool(
            role_pattern.match(line)
        )


        if is_role:

            if current_block:

                blocks.append(
                    current_block
                )

            current_block = [
                line
            ]

        else:

            if current_block:

                current_block.append(
                    line
                )


    # ----------------------------------------------
    # Add final block
    # ----------------------------------------------

    if current_block:

        blocks.append(
            current_block
        )


    experiences = []


    # ==================================================
    # PROCESS EACH EXPERIENCE BLOCK
    # ==================================================

    for block in blocks:

        header = block[0]


        # ==================================================
        # CASE 1 — MONTH BASED EXPERIENCE
        # ==================================================

        date_match = date_pattern.search(
            header
        )


        if date_match:

            # ------------------------------------------
            # Start date
            # ------------------------------------------

            start_month = (
                date_match
                .group(1)
                .lower()
            )

            start_year = int(
                date_match.group(2)
            )


            # ------------------------------------------
            # End date
            # ------------------------------------------

            end_value = (
                date_match
                .group(3)
                .lower()
            )


            if end_value == "present":

                current_date = datetime.now()

                end_month_number = (
                    current_date.month
                )

                end_year = (
                    current_date.year
                )

                end_label = "present"

            else:

                end_month_name = (
                    date_match
                    .group(4)
                    .lower()
                )

                end_month_number = MONTHS[
                    end_month_name
                ]


                if date_match.group(5) is None:

                    continue


                end_year = int(
                    date_match.group(5)
                )

                end_label = end_value


            # ------------------------------------------
            # Calculate duration
            # ------------------------------------------

            duration_months = calculate_duration(
                MONTHS[start_month],
                start_year,
                end_month_number,
                end_year
            )


            # ------------------------------------------
            # Extract title
            # ------------------------------------------

            title = header[
                :date_match.start()
            ].strip()


            # ------------------------------------------
            # Content
            # ------------------------------------------

            content = " ".join(
                block
            )


            # ------------------------------------------
            # Store experience
            # ------------------------------------------

            experiences.append(
                {
                    "title": title,
                    "start": f"{start_month} {start_year}",
                    "end": end_label,
                    "end_year": end_year,
                    "duration_months": duration_months,
                    "duration_unknown": False,
                    "content": content
                }
            )


        # ==================================================
        # CASE 2 — YEAR ONLY EXPERIENCE
        # ==================================================

        else:

            year_match = re.search(
                r"\b(20\d{2})\b",
                header
            )


            if year_match is None:

                continue


            year = int(
                year_match.group(1)
            )


            # ------------------------------------------
            # Extract title
            # ------------------------------------------

            title = header[
                :year_match.start()
            ].strip()


            # ------------------------------------------
            # Content
            # ------------------------------------------

            content = " ".join(
                block
            )


            # ------------------------------------------
            # Store year-only experience
            # ------------------------------------------

            experiences.append(
                {
                    "title": title,
                    "start": str(year),
                    "end": str(year),
                    "end_year": year,
                    "duration_months": None,
                    "duration_unknown": True,
                    "content": content
                }
            )


    return experiences


# ==================================================
# EXTRACT EXPERIENCE DURATIONS
# ==================================================

def extract_experience_durations(text):

    """
    Backward-compatible function.

    Returns only duration information.
    """

    experience_section = extract_experience_section(
        text
    )


    experiences = extract_experience_entries(
        experience_section
    )


    durations = []


    for experience in experiences:

        durations.append(
            {
                "start": experience["start"],
                "end": experience["end"],
                "end_year": experience["end_year"],
                "duration_months": experience[
                    "duration_months"
                ]
            }
        )


    return durations