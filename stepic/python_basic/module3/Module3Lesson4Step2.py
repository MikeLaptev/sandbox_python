# coding=utf-8
__author__ = 'mlaptev'


def unpack_dataset(input_file_name, output_file_name):
    current_symbol = ""
    amount = ""
    is_ready_for_output = False
    with open(input_file_name) as input_file:
        with open(output_file_name, "w+") as output_file:
            input_string = input_file.read()
            for symbol in input_string:
                if symbol.isalpha():
                    if is_ready_for_output:
                        for _ in range(int(amount)):
                            output_file.write(current_symbol)
                    current_symbol = symbol
                    amount = ""
                if symbol.isdigit():
                    is_ready_for_output = True
                    amount += symbol
            for _ in range(int(amount)):
                output_file.write(current_symbol)

if __name__ == "__main__":
    unpack_dataset("dataset_3363_2.txt", "reply_3363_2.txt")
