'''
Created on Aug, 5 2015

@author: mlaptev
'''
import math

class InstanceDecorator(object):
    '''
    Class that print name of function that has been executed and list of parameters
    '''

    def __init__(self, function):
        '''
        Constructor
        '''
        self.function_to_execute = function
        
    def __call__(self, *args):
        print "Function {} has been executed with parameter(s) {}".format(self.function_to_execute.__name__, *args)
        return self.function_to_execute(*args)
        
@InstanceDecorator
def increase(param):
    return param + 1

@InstanceDecorator
def square(param):
    return param * param

@InstanceDecorator
def squareroot(param):
    return math.sqrt(param)

if __name__ == "__main__":
    a = increase(5)
    b = square(10)
    c = squareroot(100)
    print "Results: {}, {} and {}".format(a, b, c)