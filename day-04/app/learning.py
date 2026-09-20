def calculate_progress(completed_topics, total_topics):
    if total_topics <= 0:
        raise ValueError("Total topics must be greater than zero.")

    return (completed_topics / total_topics) * 100


def remaining_topics(completed_topics, total_topics):
    if completed_topics > total_topics:
        raise ValueError("Completed topics cannot exceed total topics.")

    return total_topics - completed_topics

def add_learning_topic(topics,*topic):
    return [*topics,*topic]
