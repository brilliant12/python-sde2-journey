from dataclasses import dataclass


@dataclass
class Developer:
    name: str
    experience_years: int
    target_role: str
    skills: list[str]

    def add_skill(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)

    def is_sde2_candidate(self) -> bool:
        return self.experience_years >= 3

    def summary(self) -> str:
        return (
            f"{self.name} has {self.experience_years} years of experience "
            f"and is targeting {self.target_role}."
        )

    @classmethod
    def from_profile(cls, profile: dict) -> "Developer":
        return cls(
            name=profile["name"],
            experience_years=profile["experience_years"],
            target_role=profile["target_role"],
            skills=list(profile["skills"]),
        )