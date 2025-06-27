"""
Created on Aug 3, 2015

@author: Mikhail

@summary: Create callable instance of the class
"""


class callable_class:
    def __init__(self):
        self.function_to_call = lambda: "Call from the class {}".format(
            self.__class__.__name__
        )

    def __call__(self):
        return self.function_to_call()


if __name__ == "__main__":
    try_callable_class = callable_class()
    print((try_callable_class()))
