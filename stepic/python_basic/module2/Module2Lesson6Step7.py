# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    sum = 0
    sum_of_squares = 0
    while True:
        current_num = int(eval(input()))
        sum += current_num
        sum_of_squares += current_num * current_num
        if sum == 0:
            break
    print(sum_of_squares)
