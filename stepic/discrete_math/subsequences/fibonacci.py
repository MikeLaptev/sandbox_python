from timeit import timeit
from multiprocessing import Pool
from math import sqrt

__author__ = "mlaptev"


# Fibonacci
def calculate_by_position(positions):
    square_root_of_five = sqrt(5)
    return (
        ((1 + square_root_of_five) / 2) ** positions
        - ((1 - square_root_of_five) / 2) ** positions
    ) / square_root_of_five


def generate_value_fibonacci(till):
    prev_prev_value = 0.0
    prev_value = 1.0
    for i in range(till):
        if i == 0:
            yield prev_prev_value
        elif i == 1:
            yield prev_value
        else:
            yield prev_prev_value + prev_value
            prev_prev_value, prev_value = prev_value, prev_value + prev_prev_value


if __name__ == "__main__":
    # Simple launch
    for position, value in enumerate(generate_value_fibonacci(15)):
        print((calculate_by_position(position), value))

    # Multithreading
    amount_of_numbers = 100
    number_of_threads = 10
    p = Pool(number_of_threads)
    # Comparison parallel results with sequential launch
    multi_thread_result = p.map_async(
        calculate_by_position,
        list(range(amount_of_numbers)),
        amount_of_numbers / number_of_threads,
    )
    for position_of_number, number in enumerate(
        generate_value_fibonacci(amount_of_numbers)
    ):
        element_from_multithread_solution = multi_thread_result.get()[
            position_of_number
        ]
        if (element_from_multithread_solution - number) > 1e-8:
            # measurement error on 36 iteration :(
            print(
                (
                    "Number {} at {} position should be {}".format(
                        "{0:.8f}".format(element_from_multithread_solution),
                        position_of_number,
                        number,
                    )
                )
            )
            break

    # Fail with getting more than 1475 elements: map_async(...).get() will raise Overflow exception
    amount_of_numbers = 1475
    # Time measurements
    sequential_launch = timeit(
        "[a for a in generate_value_fibonacci(amount_of_numbers)]",
        setup="from __main__ import generate_value_fibonacci, amount_of_numbers",
        number=1000,
    )
    print(("Sequential launch {}".format(sequential_launch)))
    # lets use ready to make sure that calculation was finished.
    parallel_launch = timeit(
        "p.map_async(calculate_by_position, range(amount_of_numbers), amount_of_numbers/number_of_threads).ready()",
        setup="from __main__ import p, calculate_by_position, amount_of_numbers, number_of_threads",
        number=1000,
    )
    print(("Parallel launch {}".format(parallel_launch)))
