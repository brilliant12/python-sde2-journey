def learning_plan(topics):
    for index, topic in enumerate(topics, start=1):
        yield f"Day {index}: Learn {topic}"


topics = [
    "Python Iterators",
    "Generators",
    "Decorators",
    "Context Managers",
]

for item in learning_plan(topics):
    print(item)


def even_numbers(limit):
    for num in range(0,limit+1,2):
            yield num


for number in even_numbers(10):
    print(number)