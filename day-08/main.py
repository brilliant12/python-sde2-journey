def learning_topics():
    yield "Python"
    yield "FastAPI"
    yield "System Design"


for topic in learning_topics():
    print(topic)


def get_user_ids():
    for user_id in range(10_000_000):
        yield user_id

def get_user_idsq():
    return list(range(10_000_000))


# for num in get_user_ids():
#     print(num)

squared_numbers = (number * number for number in range(5))
print(next(squared_numbers))
print(next(squared_numbers))
print(next(squared_numbers))

# Creates the entire list immediately
numbers = [number * number for number in range(1_000_000)]

# Creates values lazily, one at a time
numbers1 = (number * number for number in range(1_000_000))
print(numbers1);