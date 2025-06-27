__author__ = "mlaptev"

if __name__ == "__main__":
    # challenge 1
    sum_list_1 = list(range(2, 18))
    occurrence_list_1 = [1, 6, 6, 6, 3, 4, 6, 3, 0, 2, 4, 6, 3, 1, 2, 3]
    print(
        (
            sum(
                map(
                    lambda x, y: x * y / sum(occurrence_list_1),
                    occurrence_list_1,
                    sum_list_1,
                )
            )
        )
    )
