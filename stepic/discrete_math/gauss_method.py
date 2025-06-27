__author__ = "Mikhail"


def add_line(line_one, line_two):
    """
    >>> line_one = [1, 2, 3]
    >>> line_two = [1, 2, 3]
    >>> add_line(line_one, line_two)
    >>> line_one
    [2, 4, 6]
    >>> line_two
    [1, 2, 3]
    >>> add_line(line_two, line_one)
    >>> line_one
    [2, 4, 6]
    >>> line_two
    [3, 6, 9]
    """
    for i in range(len(line_one)):
        line_one[i] += line_two[i]


def multiply_by_value(line, value):
    """
    >>> line_one = [1, 2, 3]
    >>> value = 5
    >>> multiply_by_value(line_one, value)
    >>> line_one
    [5, 10, 15]
    """
    for i in range(len(line)):
        line[i] *= value


def gauss_method(matrix, result_vector):
    """
    >>> matrix = [[1, 2, 3, 4], [1, 1, 1, 1], [1, 1, 2, 3], [1, 1, 2, 2]]
    >>> vector = [1, 0, 0, 0]
    >>> gauss_method(matrix, vector)
    >>> matrix
    [[1.0, -0.0, -0.0, -0.0], [-0.0, 1.0, -0.0, -0.0], [-0.0, -0.0, 1.0, -0.0], [0.0, 0.0, 0.0, 1.0]]
    >>> vector
    [-1.0, 1.0, -0.0, 0.0]
    >>> matrix = [[4, 2, 1], [7, 8, 9], [9, 1, 3]]
    >>> vector = [1, 1, 2]
    >>> gauss_method(matrix, vector)
    >>> matrix
    [[1.0, -0.0, -0.0], [-0.0, 1.0, -0.0], [-0.0, 6.082091352294336e-17, 1.0]]
    >>> vector
    [0.2608695652173913, 0.043478260869565265, -0.1304347826086957]
    >>> matrix = [[1, 3, 4], [2, 1, 4]]
    >>> vector = [4, 5]
    >>> gauss_method(matrix, vector)
    >>> matrix
    [[1.0, -0.0, 1.5999999999999996], [0.0, 1.0, 0.8]]
    >>> vector
    [2.1999999999999993, 0.6000000000000001]
    >>> matrix = [[1, 3, 2], [2, 6, 4], [1, 4, 3]]
    >>> vector = [7, 8, 1]
    >>> gauss_method(matrix, vector)
    >>> matrix
    [[1.0, -0.0, -1.0], [-0.0, 1.0, 1.0], [0.0, 0.0, 0.0]]
    >>> vector
    [24.999999999999996, -6.0, 3.0]
    >>> matrix = [[1, 1, -3], [2, 1, -2], [1, 1, 1], [1, 2, -3]]
    >>> vector = [-1, 1, 3, 1]
    >>> gauss_method(matrix, vector)
    >>> matrix
    [[1.0, -0.0, -0.0], [0.0, 1.0, 0.0], [-0.0, -0.0, 1.0], [0.0, 0.0, 0.0]]
    >>> vector
    [1.0, 1.0, 1.0, -0.25]
    >>> matrix = [[3, 3, -1], [1, -2, -3], [2, 1, -2]]
    >>> vector = [1, -11, -4]
    >>> gauss_method(matrix, vector)
    >>> matrix
    [[1.0, -0.0, 0.0], [0.0, 1.0, -0.0], [-0.0, -0.0, 1.0]]
    >>> vector
    [-1.0, 2.0, 2.0]
    """
    the_smallest_matrix_size = min(len(matrix), len(matrix[0]))
    the_matrix_size = len(matrix)
    # forward
    for forward_row_id in range(the_smallest_matrix_size):
        column_id = forward_row_id
        if matrix[forward_row_id][column_id] == 0:
            # attempt to identify required row
            rows_were_switched = False
            for another_modified_row_id in range(forward_row_id + 1, the_matrix_size):
                if matrix[another_modified_row_id][column_id] != 0:
                    # switch rows in the matrix
                    for matrix_column_id in range(column_id, len(matrix[0]), 1):
                        (
                            matrix[forward_row_id][matrix_column_id],
                            matrix[another_modified_row_id][matrix_column_id],
                        ) = (
                            matrix[another_modified_row_id][matrix_column_id],
                            matrix[forward_row_id][matrix_column_id],
                        )
                    # switch elements in result vector
                    (
                        result_vector[forward_row_id],
                        result_vector[another_modified_row_id],
                    ) = (
                        result_vector[another_modified_row_id],
                        result_vector[forward_row_id],
                    )
                    rows_were_switched = True
                    break
            if not rows_were_switched:
                continue
        normalization_value = matrix[forward_row_id][column_id]
        # change value on the element on diagonal
        multiply_by_value(matrix[forward_row_id], 1.0 / normalization_value)
        result_vector[forward_row_id] *= 1.0 / normalization_value
        # modification
        for modified_row_id in range(forward_row_id + 1, the_matrix_size):
            if matrix[modified_row_id][column_id] != 0:
                direct_or_reverse_gauss_step(
                    column_id, forward_row_id, matrix, modified_row_id, result_vector
                )
    # reverse
    for reverse_row_id in range(the_smallest_matrix_size - 1, -1, -1):
        column_id = reverse_row_id
        if matrix[reverse_row_id][column_id] != 0:
            normalization_value = matrix[reverse_row_id][column_id]
            # change value on the element on diagonal
            multiply_by_value(matrix[reverse_row_id], 1.0 / normalization_value)
            result_vector[reverse_row_id] *= 1.0 / normalization_value
            # modification
            for modified_row_id in range(reverse_row_id - 1, -1, -1):
                if matrix[modified_row_id][column_id] != 0:
                    direct_or_reverse_gauss_step(
                        column_id,
                        reverse_row_id,
                        matrix,
                        modified_row_id,
                        result_vector,
                    )


def direct_or_reverse_gauss_step(
    column_id, forward_row_id, matrix, modified_row_id, result_vector
):
    """ """
    modification = -(matrix[forward_row_id][column_id]) / (
        matrix[modified_row_id][column_id]
    )
    # normalise matrix row
    multiply_by_value(matrix[modified_row_id], modification)
    # normalise result vector
    result_vector[modified_row_id] *= modification
    # change required row
    add_line(matrix[modified_row_id], matrix[forward_row_id])
    # change result vector
    result_vector[modified_row_id] += result_vector[forward_row_id]


def analyse_gauss_method_results(matrix, result_vector):
    """
    >>> matrix = [[1.0, -0.0, -0.0], [-0.0, 1.0, -0.0], [-0.0, 6.082091352294336e-17, 1.0]]
    >>> result_vector = [0.2608695652173913, 0.043478260869565265, -0.1304347826086957]
    >>> analyse_gauss_method_results(matrix, result_vector)
    YES
    0.260869565217 0.0434782608696 -0.130434782609
    >>> processed_matrix = [[1.0, -0.0, -1.0], [-0.0, 1.0, 1.0], [0.0, 0.0, 0.0]]
    >>> result_vector = [24.999999999999996, -6.0, 3.0]
    >>> analyse_gauss_method_results(processed_matrix, result_vector)
    NO
    >>> processed_matrix = [[1.0, -0.0, 1.5999999999999996], [0.0, 1.0, 0.8]]
    >>> result_vector = [2.1999999999999993, 0.6000000000000001]
    >>> analyse_gauss_method_results(processed_matrix, result_vector)
    INF
    >>> processed_matrix = [[1.0, -0.0, -0.0], [0.0, 1.0, 0.0], [-0.0, -0.0, 1.0], [0.0, 0.0, 0.0]]
    >>> result_vector = [1.0, 1.0, 1.0, -0.25]
    >>> analyse_gauss_method_results(processed_matrix, result_vector)
    NO
    """
    # check on situation when the system has no answer
    for row_id, row in enumerate(matrix):
        if (
            all([abs(row_element) < 1.0e-8 for row_element in matrix[row_id]])
            and abs(result_vector[row_id]) > 1.0e-8
        ):
            print("NO")
            return
    # system has infinite number of answers
    if len(matrix) < len(matrix[0]):
        print("INF")
        return
    # system has only one answer
    print("YES")
    print((" ".join([str(res) for res in result_vector])))


if __name__ == "__main__":
    # data initialization
    data = list([int(x) for x in input().split()])
    amount_of_equations = data[0]
    amount_of_variables = data[1]
    initial_matrix = list()
    initial_vector = list()
    for equation_id in range(amount_of_equations):
        equation = list([float(x) for x in input().split()])
        initial_matrix.append(equation[:-1])
        initial_vector.append(equation[-1])

    gauss_method(initial_matrix, initial_vector)
    analyse_gauss_method_results(initial_matrix, initial_vector)
