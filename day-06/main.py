from developer import Developer


profile = {
    "name": "Arjun Gupta",
    "experience_years": 4,
    "target_role": "Python Backend SDE-2",
    "skills": ["PHP", "Laravel", "Python"],
}

developer = Developer.from_profile(profile)
developer.add_skill("FastAPI")
developer.add_skill("Python")

print(developer.summary())
print(f"SDE-2 candidate: {developer.is_sde2_candidate()}")
print(f"Skills: {developer.skills}")