"""
Created on Aug, 7 2015

@author: mlaptev
"""

import math


class CallCount(object):
    """
    This class provides functionality that can be used like a decorator
    that calculates how many times decorated method has been called
    """

    global_counter = {}

    def __init__(self, function):
        """
        Constructor
        """
        self.function_to_execute = function
        self.__name__ = function.__name__

    def __call__(self, *args):
        self.increase_counter(self.__name__)
        return self.function_to_execute(self, *args)

    @classmethod
    def increase_counter(cls, function_name):
        cls.global_counter[function_name] = cls.global_counter.get(function_name, 0) + 1


class ToDecorateMethods(object):
    """
    This class is example for class decorator, that calculate statistic
    """

    def increase(self, param):
        return param + 1

    def square(self, param):
        return param * param

    @CallCount
    def squareroot(self, param):
        return math.sqrt(param)

    @CallCount
    def cube(self, param):
        return param * param * param


if __name__ == "__main__":
    to_decorate_methods = ToDecorateMethods()
    for i in range(1, 5):
        for j in range(i + 1):
            if j == 1:
                print(("Call {} method".format(to_decorate_methods.increase.__name__)))
                print(("Result {}".format(to_decorate_methods.increase(4))))
            elif j == 2:
                print(("Call {} method".format(to_decorate_methods.square.__name__)))
                print(("Result {}".format(to_decorate_methods.square(4))))
            elif j == 3:
                print(
                    ("Call {} method".format(to_decorate_methods.squareroot.__name__))
                )
                print(("Result {}".format(to_decorate_methods.squareroot(4))))
            elif j == 4:
                print(("Call {} method".format(to_decorate_methods.cube.__name__)))
                print(("Result {}".format(to_decorate_methods.cube(4))))

    print("Statistic:")
    print(("Amount of decorated calls is: {}".format(CallCount.global_counter)))
