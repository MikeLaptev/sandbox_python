'''
Created on Aug, 11 2015

@author: mlaptev
'''

def name_letters_combination(name):
    for i in range(len(name)):
        yield tuple(name[j] for j in range(len(name)) if j != i)

if __name__ == '__main__':
    for combination in name_letters_combination('Mike'):
        print combination