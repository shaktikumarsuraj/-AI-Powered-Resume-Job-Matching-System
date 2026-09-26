from experience_requirements import extract_experience_requirements
from experience_matcher import compare_all_experience_requirements


job_description = """
We are looking for an AI/ML Engineer with 2+ years of experience with Python.
The candidate should have at least 1 year of experience in machine learning.
Experience with LangChain is preferred.
"""


requirements = extract_experience_requirements(
    job_description
)


resume_months = 18


results = compare_all_experience_requirements(
    requirements,
    resume_months
)


print("\nEXPERIENCE REQUIREMENT MATCHING")
print("-" * 50)

for result in results:

    print(
        f"{result['skill']}: "
        f"Required = {result['required_years']} years, "
        f"Resume = {result['resume_months']} months, "
        f"Status = {result['status']}"
    )