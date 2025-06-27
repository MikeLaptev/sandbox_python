from stepic.discrete_math.gauss_method import gauss_method

__author__ = "mlaptev"


def difference_between_vectors(minuend_vector, subtrahend_vector):
    """
    >>> difference_between_vectors([2, 3, 4], [1, 1, 1])
    [1, 2, 3]
    """
    return [
        minuend_vector[i] - subtrahend_vector[i] for i in range(len(minuend_vector))
    ]


def multiply_vector_by_value(vector, value):
    """
    >>> multiply_vector_by_value([1, 2, 3], 5)
    [5, 10, 15]
    """
    return [vector[i] * value for i in range(len(vector))]


def scalar_multiplication(first_vector, second_vector):
    """
    >>> scalar_multiplication([2, 3, 4], [3, 4, 6])
    42
    """
    return sum([first_vector[i] * second_vector[i] for i in range(len(first_vector))])


def process_initial_data(list_of_vectors, result_vector):
    """
    >>> processed_matrix, processed_vector = process_initial_data([[2, 3, 4]], [3, 4, 6])
    >>> processed_matrix
    [[29]]
    >>> processed_vector
    [42]
    """
    processed_matrix = list()
    processed_vector = list()
    for equation_id in range(len(list_of_vectors)):
        # calculate value for processed vector
        processed_vector.append(
            scalar_multiplication(result_vector, list_of_vectors[equation_id])
        )
        # calculate value for equation
        processed_matrix.append(
            [
                scalar_multiplication(
                    list_of_vectors[equation_id], list_of_vectors[another_equation_id]
                )
                for another_equation_id in range(len(list_of_vectors))
            ]
        )

    return processed_matrix, processed_vector


def ordinary_least_squares(list_of_vectors, result_vector):
    """
    >>> ordinary_least_squares([[2, 3, 4]], [3, 4, 6])
    [1.4482758620689655]
    >>> ordinary_least_squares([[1, 1, 1], [-1, 0, 1]], [4, 5, 9])
    [6.0, 2.5]
    """
    processed_matrix, processed_vector = process_initial_data(
        list_of_vectors, result_vector
    )
    gauss_method(processed_matrix, processed_vector)
    return processed_vector


def calculate_minimum_of_discrepancy(list_of_vectors, result_vector):
    """
    >>> calculate_minimum_of_discrepancy([[1, 1, 1], [-1, 0, 1]], [4, 5, 9])
    1.5
    """
    discrepancy_vector = ordinary_least_squares(list_of_vectors, result_vector)
    difference = result_vector[:]
    for position in range(len(list_of_vectors)):
        difference = difference_between_vectors(
            difference,
            multiply_vector_by_value(
                list_of_vectors[position], discrepancy_vector[position]
            ),
        )
    return scalar_multiplication(difference, difference)


if __name__ == "__main__":
    # data initialization
    data = list([int(x) for x in input().split()])
    amount_of_equations = data[0]
    amount_of_variables = data[1]
    list_of_vectors = [list() for dummy_i in range(amount_of_variables)]
    result_vector = list()
    for equation_id in range(amount_of_equations):
        equation = list([float(x) for x in input().split()])
        for position in range(amount_of_variables):
            list_of_vectors[position].append(equation[position])
        result_vector.append(equation[-1])

    discrepancy_vector = ordinary_least_squares(list_of_vectors, result_vector)
    print((" ".join([str(discrepancy) for discrepancy in discrepancy_vector])))
