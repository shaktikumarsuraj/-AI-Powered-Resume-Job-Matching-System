from experience_requirements import extract_experience_requirements


job_description = """
We are looking for an AI/ML Engineer with 2+ years of experience with Python.
The candidate should have at least 1 year of experience in machine learning.
Experience with LangChain is preferred.
"""

requirements = extract_experience_requirements(
    job_description
)

print("\nEXPERIENCE REQUIREMENTS")
print("-" * 50)

for requirement in requirements:
    print(requirement)