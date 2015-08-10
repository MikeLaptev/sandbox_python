'''
Created on Aug, 5 2015

@author: mlaptev
'''
import math
from functools import wraps

# simple decorator
class SimpleDecorator(object):
    '''
    Class that print name of function that has been executed and list of parameters
    @note: it can be used as a simple decorator as a class
    '''

    def __init__(self, function):
        '''
        Constructor
        '''
        self.function_to_execute = function
        
    def __call__(self, *args):
        print "Function {} has been executed with parameter(s) {}".format(self.function_to_execute.__name__, *args)
        return self.function_to_execute(*args)
        

@SimpleDecorator
def increase(param):
    return param + 1

@SimpleDecorator
def square(param):
    return param * param

@SimpleDecorator
def squareroot(param):
    return math.sqrt(param)

# instance decorator
class InstanceDecorator(object):
    '''
    Class that print name of function that has been executed and list of parameters
    @note: it can be used as a simple decorator as an instance of the class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def __call__(self, f):
        @wraps(f)
        def wrapper(*args):
            print "Function {} has been executed with parameter(s) {}".format(f.__name__, *args)
            return f(*args)
        return wrapper

instance_decorator = InstanceDecorator()

@instance_decorator
def cube(param):
    return param * param * param

if __name__ == "__main__":
    a = increase(5)
    b = square(10)
    c = squareroot(100)
    d = cube(4)
    print "Results: {}, {}, {} and {}".format(a, b, c, d)