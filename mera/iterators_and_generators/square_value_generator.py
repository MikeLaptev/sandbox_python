'''
Created on Aug 11, 2015.

@author: mlaptev
'''

def square_value_generator(max_value):
    start_value = 0
    while start_value < max_value:
        start_value += 1
        yield (start_value, start_value**2)
           
if __name__ == '__main__':
    for i in square_value_generator(10):
        print i