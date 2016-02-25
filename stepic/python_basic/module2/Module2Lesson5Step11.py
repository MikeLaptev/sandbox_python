# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    input_array = sorted([int(i) for i in input().split()])
    amount = 0
    for i in range(len(input_array) - 1):
        if input_array[i] == input_array[i+1]:
            amount += 1
        elif amount > 0:
            print(input_array[i], end=' ')
            amount = 0
        else:
            amount = 0
    if amount > 0:
        print(input_array[-1], end=' ')
