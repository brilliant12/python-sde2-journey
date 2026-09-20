from app.developer import create_developer_profile, is_sde2_candidate,format_developer_summary
from app.learning import calculate_progress, remaining_topics,add_learning_topic


developer = create_developer_profile(
    name="Arjun Gupta",
    experience_years=4,
    target_role="Python Backend SDE-2",
)

progress = calculate_progress(completed_topics=4, total_topics=40)
topics_left = remaining_topics(completed_topics=4, total_topics=40)

print(developer)
print(f"Learning progress: {progress:.1f}%")
print(f"Topics remaining: {topics_left}")

if is_sde2_candidate(developer["experience_years"]):
    print("You have suitable experience for the SDE-2 transition path.")

print(f"Learning progress: {progress:.1f}%")

topics = ["Python", "Collections", "Functions"]
updated_topics = add_learning_topic(topics, "Modules")
print(updated_topics,topics)

profile=format_developer_summary(developer);
print(profile)