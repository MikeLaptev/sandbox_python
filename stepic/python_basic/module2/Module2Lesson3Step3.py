# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    a, b, c, d = [int(input()) for _ in range(4)]
    # print top row
    print(" \t", end="")
    for x in range(c, d + 1):
        print(x, end="\t")
    print()
    for y in range(a, b + 1):
        print(y, end="\t")
        for x in range(c, d + 1):
            print(x * y, end="\t")
        print()
