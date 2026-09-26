import re


def normalize_skill(skill):

    return (
        skill
        .lower()
        .strip()
    )


def assign_skill_priorities(
    extracted_skills,
    priority_results
):

    final_results = []

    # ---------------------------------------------
    # Convert detected priority information
    # into an easier lookup structure
    # ---------------------------------------------

    priority_map = {}

    for result in priority_results:

        skill = normalize_skill(
            result["skill"]
        )

        priority_map[skill] = {
            "priority": result["priority"],
            "source": result["source"]
        }


    # ---------------------------------------------
    # Match existing extracted skills
    # with detected priority information
    # ---------------------------------------------

    for skill in extracted_skills:

        normalized_skill = normalize_skill(
            skill
        )

        priority = "unspecified"
        source = None

        # Direct skill match
        if normalized_skill in priority_map:

            priority = priority_map[
                normalized_skill
            ]["priority"]

            source = priority_map[
                normalized_skill
            ]["source"]

        else:

            # -------------------------------------
            # Fallback:
            # Check whether the extracted skill
            # appears inside a detected skill/source
            # -------------------------------------

            for detected_skill, data in priority_map.items():

                if (
                    normalized_skill == detected_skill
                    or
                    normalized_skill in detected_skill
                ):

                    priority = data[
                        "priority"
                    ]

                    source = data[
                        "source"
                    ]

                    break


        final_results.append(
            {
                "skill": skill,
                "priority": priority,
                "source": source
            }
        )


    return final_results