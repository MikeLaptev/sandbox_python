# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    input_strings = input().split()
    statistic = dict()
    for string in input_strings:
        string = string.lower()
        statistic[string] = statistic.get(string, 0) + 1
    for string, amount in list(statistic.items()):
        print((string, amount))
