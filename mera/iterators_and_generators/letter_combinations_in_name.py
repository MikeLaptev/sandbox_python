'''
Created on Aug, 11 2015

@author: mlaptev
'''

# implementation without external modules
def name_letters_combination(name):
    for i in range(len(name)):
        yield tuple(name[j] for j in range(len(name)) if j != i)
        
# implementation with external modules
import itertools
def name_letters_combination_with_another_module_usage(name):
    return itertools.combinations(name, len(name) - 1)

if __name__ == '__main__':
    print ">>> First Solution <<<"
    for combination in name_letters_combination('Mike'):
        print combination
    print 
    print ">>> Second Solution <<<"
    for combination in name_letters_combination_with_another_module_usage('Mike'):
        print combination