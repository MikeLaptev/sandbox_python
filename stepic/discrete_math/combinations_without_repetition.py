__author__ = 'mlaptev'


def append_range_to_list_elements(initial_range, initial_set):
    result_set = set()
    for s in initial_set:
        for r in initial_range:
            list_to_append = list()
            list_to_append.extend(s)
            if r not in list_to_append:
                list_to_append.append(r)
                result_set.add(tuple(list_to_append))
    return result_set


def get_required_list_of_sets(range_of_values, max_amount_of_elements):
    list_to_add = [tuple([i]) for i in range(range_of_values)]
    initial_set = set(list_to_add)
    for i in range(max_amount_of_elements - 1):
        initial_set = append_range_to_list_elements(range(range_of_values), initial_set)

    return initial_set

if __name__ == "__main__":
    # data initialization
    n, k = map(lambda x: int(x), input().split())
    if 0 < k <= n:
        result_set = [" ".join(map(str, e)) for e in get_required_list_of_sets(n, k)]
        for e in sorted(result_set):
            print(e)
