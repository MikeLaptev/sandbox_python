# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    amount, i, number = int(input()), 0, 0
    while i < amount:
        for j in range(number):
            if i >= amount:
                break
            i += 1
            print(number, end=" ")
        number += 1
