# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    initial_list = [int(i) for i in input().split()]
    if len(initial_list) == 1:
        print(initial_list[0])
    else:
        for combination in [
            initial_list[i - 1] + initial_list[(i + 1) % len(initial_list)]
            for i in range(len(initial_list))
        ]:
            print(combination, end=" ")
