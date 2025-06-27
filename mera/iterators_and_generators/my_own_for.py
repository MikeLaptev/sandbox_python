"""
Created on Aug, 11 2015

@author: mlaptev
"""


def my_own_for(iterable_collection):
    iterator_for = iter(iterable_collection)
    while True:
        try:
            print((next(iterator_for)))
        except StopIteration:
            print("End of collection")
            break


if __name__ == "__main__":
    my_own_for([2, 5, 7, 9])
