# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    # process first number
    first_number = int(input())
    maximum, middle, minimum = first_number, first_number, first_number
    # process second number
    second_number = int(input())
    if second_number >= maximum:
        maximum = second_number
    else:
        minimum = second_number
    # process third number
    third_number = int(input())
    if third_number >= maximum:
        maximum, middle = third_number, maximum
    elif third_number >= minimum:
        middle = third_number
    else:
        minimum, middle = third_number, minimum
    print(maximum)
    print(minimum)
    print(middle)
