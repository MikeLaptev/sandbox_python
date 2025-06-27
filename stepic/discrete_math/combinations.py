__author__ = "mlaptev"


def append_range_to_list_elements(initial_range, initial_set):
    result_set = set()
    for s in initial_set:
        for r in initial_range:
            set_to_append = set(s)
            if r not in set_to_append:
                set_to_append.add(r)
                list_to_append = list(set_to_append)
                list_to_append.sort()
                result_set.add(tuple(list_to_append))
    return result_set


def get_required_list_of_sets(range_of_values, max_amount_of_elements):
    list_to_add = [tuple([i]) for i in range(range_of_values)]
    list_to_add.sort()
    initial_set = set(list_to_add)
    for i in range(max_amount_of_elements - 1):
        initial_set = append_range_to_list_elements(
            list(range(range_of_values)), initial_set
        )

    return initial_set


if __name__ == "__main__":
    # data initialization
    k, n = [int(x) for x in input().split()]
    if 0 < k <= n:
        result_set = get_required_list_of_sets(n, k)
        print((len(result_set)))
        for e in result_set:
            print((" ".join(map(str, e))))
