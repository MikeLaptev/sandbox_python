'''
Created on Aug, 11 2015

@author: mlaptev
'''

def generator_of_sum_of_cubes(start, finish):
    pointer = start
    while pointer <= finish:
        yield pointer**3
        pointer += 1

if __name__ == '__main__':
    sum = 0
    prev_sum = 0
    for i in generator_of_sum_of_cubes(1, 3000000):
        sum += i
    print "Result sum is: {}".format(sum)