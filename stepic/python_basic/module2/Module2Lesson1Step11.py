# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    sum = 0
    current_number = int(input())
    while current_number != 0:
        sum += current_number
        current_number = int(input())
    print(sum)
