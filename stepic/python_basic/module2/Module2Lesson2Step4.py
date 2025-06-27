# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    while True:
        number = int(eval(input()))
        if number < 10:
            continue
        if number > 100:
            break
        print(number)
