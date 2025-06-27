# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    min_amount = int(eval(input()))
    max_amount = int(eval(input()))
    current_amount = int(eval(input()))
    if min_amount <= current_amount <= max_amount:
        print("Это нормально")
    elif current_amount < min_amount:
        print("Недосып")
    else:
        print("Пересып")
