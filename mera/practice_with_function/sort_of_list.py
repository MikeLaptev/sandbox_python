'''
Created on Aug 3, 2015

@author: Mikhail

@summary: Sort list of strings by latest letter
'''

def sort_by_latest_letter(list_of_strings):
    """
    >>> sort_by_latest_letter(["abc", "cab", "bca"])
    ['bca', 'cab', 'abc']
    """
    return [sorted_element[::-1] for sorted_element in sorted([element[::-1] for element in list_of_strings])]

def sort_by_latest_letter_with_map(list_of_strings):
    """
    >>> sort_by_latest_letter_with_map(["abc", "cab", "bca"])
    ['bca', 'cab', 'abc']
    """
    return map(lambda x: x[::-1], *[sorted(map(lambda a: a[::-1], list_of_strings))])

if __name__ == "__main__":
    # acceptance testing
    import doctest
    print doctest.testmod()
    
    # performance testing
    import timeit
    first_solution = timeit.timeit(stmt='sort_by_latest_letter(["abc", "cab", "bca"])', setup="from __main__ import sort_by_latest_letter")
    second_solution = timeit.timeit(stmt='sort_by_latest_letter_with_map(["abc", "cab", "bca"])', setup="from __main__ import sort_by_latest_letter_with_map")
    print "First solution took {}, but second solution took {}".format(first_solution, second_solution)