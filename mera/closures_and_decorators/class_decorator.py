'''
Created on Aug, 5 2015

@author: mlaptev
'''

class CallCount(object):
    '''
    This class provides functionality that can be used like a decorator 
    that calculates how many times decorated method has been called
    '''
    global_counter = 0

    def __init__(self, function):
        '''
        Constructor
        '''
        self.function_to_execute = function
        
    def __call__(self, *args):
        self.increase_counter()
        self.function_to_execute(*args)
        
    @classmethod
    def increase_counter(cls):
        cls.global_counter += 1
        
@CallCount
def hello(name):
    print "Hello, {}".format(name)
    
if __name__ == "__main__":
    for i in range(10):
        hello("Student #{}".format(i + 1))
        
    print "Function has been called {} times".format(CallCount.global_counter)