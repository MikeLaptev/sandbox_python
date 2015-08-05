'''
Created on Aug, 5 2015.

@author: mlaptev
'''

def power_of_n(N):
    """
    >>> square = power_of_n(2)
    >>> square(3)
    9
    >>> cube = power_of_n(3)
    >>> cube(4)
    64
    """
    def action(X):
        return X**N
    return action

if __name__ == "__main__":
    import doctest
    print doctest.testmod()
