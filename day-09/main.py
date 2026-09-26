from functools import wraps
from time import perf_counter


def measure_execution_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()

        result = function(*args, **kwargs)

        end_time = perf_counter()
        duration = end_time - start_time

        print(f"{function.__name__} took {duration:.6f} seconds")

        return result

    return wrapper


@measure_execution_time
def calculate_total(*prices):
    return sum(prices)


print(calculate_total(199, 499, 999))