def create_developer_profile(name, experience_years, target_role="Python Backend SDE-2"):
    return {
        'name':name,
        'experience_years':experience_years,
        'target_role' :target_role
    }

User=create_developer_profile("Arjun Gupta",4,"Python Backend SDE-2");

print(User)

def calculate_learning_progress(completed_topics, total_topics):
    if total_topics<=0:
        return 'Add Total Topics'

    if completed_topics>total_topics :
        return 'completed topic should bot be greater than total topics'
    if completed_topics <0 :
        return 'add a valid total completed topic count'

    return completed_topics*100/total_topics;


print(calculate_learning_progress(12,10))


def add_skills(existing_skills, *new_skills):
    return [*existing_skills, *new_skills]

skills = ["PHP", "Laravel", "Python"]

updated_skills = add_skills(skills, "FastAPI", "PostgreSQL")

print("Original:", skills)
print("Updated:", updated_skills)

profile = {
    "name": "Arjun Gupta",
    "target_role": "Python Backend SDE-2",
}

def update_profile(profile, **updates):
    return {**profile, **updates}

updated_profile = update_profile(
    profile,
    target_role="Python Full-Stack Developer",
    experience_years=4,
)

print("Original:", profile)
print("Updated:", updated_profile)
    