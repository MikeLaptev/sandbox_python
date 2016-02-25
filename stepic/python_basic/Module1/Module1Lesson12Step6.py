# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    number_of_programmers = int(input())
    last_number = number_of_programmers % 10
    pre_last_number = (number_of_programmers//10) % 10
    if pre_last_number == 1 or (pre_last_number == 0 and last_number == 0):
        print(str(number_of_programmers) + " программистов")
    elif pre_last_number != 0 and last_number == 1:
        print(str(number_of_programmers) + " программист")
    elif last_number in [2, 3, 4]:
        print(str(number_of_programmers) + " программиста")
    else:
        print(str(number_of_programmers) + " программистов")
