# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    initial_string = input().lower()
    print(100*(initial_string.count('g') + initial_string.count('c'))/len(initial_string))
