"""
Created on Jul 30, 2015

@author: Mikhail
"""


def check_that_number_happy(num):
    """
    >>> check_that_number_happy(512)
    Amount of zero - 9
    Amount of one - 1
    False
    """
    amount_of_zero = 0
    amount_of_one = 0
    while num > 0:
        if num - ((num >> 1) << 1) == 0:
            amount_of_zero += 1
        else:
            amount_of_one += 1
        num >>= 1

    print(("Amount of zero - {}".format(amount_of_zero)))
    print(("Amount of one - {}".format(amount_of_one)))

    return amount_of_one == amount_of_zero


if __name__ == "__main__":
    import doctest

    print((doctest.testmod()))
