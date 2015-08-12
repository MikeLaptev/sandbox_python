'''
Created on Aug, 11 2015

@author: mlaptev
'''
import time

def generator_of_sum_of_cubes(start, finish):
    pointer = start
    while pointer <= finish:
        yield pointer**3
        pointer += 1

if __name__ == '__main__':
    print ">>> First Solution <<<"
    start_time = time.time()
    sum_f = 0
    for i in generator_of_sum_of_cubes(1, 3000000):
        sum_f += i
    finish_time = time.time()
    print "Result sum is: {}. Working time: {}".format(sum_f, finish_time - start_time)
    
    print ">>> Second Solution <<<"
    start_time = time.time()
    sum_s = sum(value for value in generator_of_sum_of_cubes(1, 3000000))
    finish_time = time.time()
    print "Result sum is: {}. Working time: {}".format(sum_s, finish_time - start_time)
    