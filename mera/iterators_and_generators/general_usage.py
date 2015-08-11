'''
Created on Aug, 11 2015

@author: mlaptev
'''

# First: create list that contains tuple with following structure:
# 1. the element
# 2. square of the element
# 3. cube of the element

first_task_result = [(elem, elem**2, elem**3) for elem in range (1, 21)]

# Second: create list that contains cube of even numbers
second_task_result = [elem**3 for elem in range(2, 21, 2)]

# Third: create dictionary with symbols and its key in string
third_task_results = {key: ord(key) for key in "This is a test message"}

# Fourth: dictionary with number as a key and cube of the number as  a value. number should be even and should not have 10 as delimiter
fourth_tast_results = {key: key**3 for key in range(10, 1001, 2) if key % 10 != 0}

if __name__ == '__main__':
    print "First task"
    print first_task_result
    print "Second task"
    print second_task_result
    print "Third task"
    print third_task_results
    print "Fourth task"
    print fourth_tast_results
    