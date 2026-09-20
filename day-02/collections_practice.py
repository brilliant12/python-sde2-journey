developer = {
    "name": "Arjun Gupta",
    "skills": ["PHP", "Laravel", "Python"],
    "experience_years": 4,
    "target_role": "Python Backend SDE-2",
    "preferred_locations": ("Remote", "India"),
}

developer["skills"].append("FastAPI")

backend_skills = developer["skills"].copy()
backend_skills.append("PostgreSQL")

unique_skills = {"PHP", "Laravel", "Python", "FastAPI", "PostgreSQL", "Python"}

print("Original skills:", developer["skills"])
print("Backend skills:", backend_skills)
print("Unique skills:", unique_skills)

print(developer.get("github_url", "Not added yet"))

for key, value in developer.items():
    print(f"{key}: {value}")

print(
    f'{developer["name"]} has {developer["experience_years"]} years '
    f'of experience and is targeting {developer["target_role"]}.'
)