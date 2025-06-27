# coding=utf-8
__author__ = "mlaptev"


def f(x):
    """
    >>> f(4.5)
    7.25
    >>> f(-4.5)
    -5.25
    >>> f(1)
    -0.5
    """
    if x <= -2:
        return 1 - (x + 2) ** 2
    if x > 2:
        return 1 + (x - 2) ** 2
    return -x / 2


if __name__ == "__main__":
    import doctest

    print((doctest.testmod()))
