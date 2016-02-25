# coding=utf-8
__author__ = 'mlaptev'


def modify_list(l):
    """
    >>> lst = [1, 2, 3, 4, 5, 6]
    >>> modify_list(lst)
    >>> lst
    [1, 2, 3]
    >>> modify_list(lst)
    >>> lst
    [1]
    >>> lst = [10, 5, 8, 3]
    >>> modify_list(lst)
    >>> lst
    [5, 4]
    """
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            l[i] //= 2
        else:
            del l[i]

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
