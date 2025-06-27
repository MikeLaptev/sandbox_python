# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    input_string = eval(input())
    output_string = ""
    current_symbol = input_string[0]
    amount = 0
    for symbol in input_string:
        if symbol == current_symbol:
            amount += 1
        else:
            output_string += current_symbol + str(amount)
            current_symbol = symbol
            amount = 1
    output_string += current_symbol + str(amount)
    print(output_string)
