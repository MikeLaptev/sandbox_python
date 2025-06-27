# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    an_year = int(eval(input()))
    if 1900 <= an_year <= 3000:
        if an_year % 4 == 0 and (an_year % 100 != 0 or an_year % 400 == 0):
            print("Високосный")
        else:
            print("Обычный")
    else:
        print("Вне диапозона")
