class InvalidLearningProgressError(ValueError):
    pass


def calculate_progress(completed_topics, total_topics):
    if total_topics <= 0:
        raise InvalidLearningProgressError(
            "Total topics must be greater than zero."
        )

    if completed_topics < 0:
        raise InvalidLearningProgressError(
            "Completed topics must not be negative."
        )

    if completed_topics > total_topics:
        raise InvalidLearningProgressError(
            "Completed topics must not be greater than total topics."
        )

    return (completed_topics / total_topics) * 100


test_cases = [
    (8, 10),
    (0, 10),
    (12, 10),
    (2, 0),
]

for completed_topics, total_topics in test_cases:
    try:
        progress = calculate_progress(completed_topics, total_topics)
        print(f"Progress: {progress}%")
    except InvalidLearningProgressError as error:
        print(f"Error: {error}")