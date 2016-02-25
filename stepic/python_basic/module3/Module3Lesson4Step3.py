# coding=utf-8
__author__ = 'mlaptev'


def find_more_used_word(input_file_name):
    statistic = dict()
    with open(input_file_name) as input_file:
        for line in input_file:
            words = line.split()
            for a_word in words:
                statistic[a_word.lower()] = statistic.get(a_word.lower(), 0) + 1
    word_to_return = ""
    amount_to_return = -1
    for key, value in statistic.items():
        if value > amount_to_return:
            word_to_return = key
            amount_to_return = value
        elif value == amount_to_return:
            if key < word_to_return:
                word_to_return = key
    return word_to_return, amount_to_return

if __name__ == "__main__":
    the_word, the_amount = find_more_used_word("dataset_3363_3.txt")
    print(the_word, the_amount)
