# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    first_number = float(input())
    second_number = float(input())
    operation = input()
    if operation in ['/', 'div', 'mod'] and second_number == 0.0:
        print("Деление на 0!")
    else:
        if operation == "+":
            print(first_number + second_number)
        elif operation == "-":
            print(first_number - second_number)
        elif operation == "/":
            print(first_number / second_number)
        elif operation == "*":
            print(first_number * second_number)
        elif operation == "mod":
            print(first_number % second_number)
        elif operation == "pow":
            print(first_number**second_number)
        elif operation == "div":
            print(int(first_number)//int(second_number))
