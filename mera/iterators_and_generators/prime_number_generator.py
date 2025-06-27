"""
Created on Aug 11, 2015

@author: mlaptev
"""

import math


def prime_numbers_generation():
    prime_numbers = dict()
    first_prime_number = 2
    number_to_check = 1
    index = 1
    first_odd_number = 3
    while True:
        is_prime = True
        number_to_check = (
            (number_to_check + number_to_check % 2 + 1)
            if index > 1
            else first_prime_number
        )
        divisor = first_odd_number
        divisor_index = 2
        while divisor <= math.sqrt(number_to_check):
            if number_to_check % divisor == 0:
                is_prime = False
                break
            divisor_index += 1
            divisor = prime_numbers[divisor_index]
        if is_prime:
            # if found just add it to the list
            prime_numbers[index] = number_to_check
            yield number_to_check
            # increase value of the index
            index += 1


if __name__ == "__main__":
    for i in prime_numbers_generation():
        print(i)
        if i > 200:
            break
