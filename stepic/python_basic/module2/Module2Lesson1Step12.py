# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    amount_of_biologists = int(input())
    amount_of_programmers = int(input())
    first, second = amount_of_biologists, amount_of_programmers
    if first < second:
        first, second = second, first
    # calculate gcd
    while second != 0:
        first, second = second, (first % second)
    print(int((amount_of_programmers*amount_of_biologists)/first))
