# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    words = set()
    unknown_words = set()
    # read all known words
    amount_of_words = int(eval(input()))
    for _ in range(amount_of_words):
        words.add(eval(input()))
    # read the text
    amount_of_text_lines = int(eval(input()))
    for _ in range(amount_of_text_lines):
        for word in input().split():
            if word not in words:
                unknown_words.add(word)

    # print results
    for unknown_word in unknown_words:
        print(unknown_word)
