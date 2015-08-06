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

if __name__ == "__main__":
    import doctest
    print doctest.testmod()