# coding=utf-8
__author__ = 'mlaptev'


def update_dictionary(d, key, value):
    """
    >>> d = {}
    >>> update_dictionary(d, 1, -1)
    >>> d
    {2: [-1]}
    >>> update_dictionary(d, 2, -2)
    >>> d
    {2: [-1, -2]}
    >>> update_dictionary(d, 1, -3)
    >>> d
    {2: [-1, -2, -3]}
    """
    if key in d:
        d[key].append(value)
    elif key*2 in d:
        d[key*2].append(value)
    else:
        d[key*2] = [value]

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
