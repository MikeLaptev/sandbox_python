# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    start = int(input())
    finish = int(input())
    amount, total_sum = 0, 0
    for number in (i for i in range(start, finish+1) if i%3 == 0):
        amount += 1
        total_sum += number
    print(total_sum / amount)
