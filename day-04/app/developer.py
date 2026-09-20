def create_developer_profile(name, experience_years, target_role):
    return {
        "name": name,
        "experience_years": experience_years,
        "target_role": target_role,
    }


def is_sde2_candidate(experience_years):
    return experience_years >= 3


def format_developer_summary(profile):
    return f"{profile.get('name')} has {profile.get('experience_years')} years of experience and targets {profile.get('target_role')}."