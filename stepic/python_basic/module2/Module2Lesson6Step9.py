# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    input_list = [int(i) for i in input().split()]
    required_number = int(input())
    counter = 0
    for i in range(len(input_list)):
        if input_list[i] == required_number:
            print(i, end=" ")
            counter += 1
    if counter == 0:
        print("Отсутствует")
