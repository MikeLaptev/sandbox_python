# coding=UTF-8
"""
Created on Aug, 5 2015

@author: mlaptev
"""


def escape_unicode(fn):
    def wrapped():
        print(("String to convert '{}'".format(fn())))
        return "".join([i if ord(i) < 128 else "\\" + str(hex(ord(i))) for i in fn()])

    return wrapped


@escape_unicode
def some_non_latin_string():
    return "This is just a строка!"


if __name__ == "__main__":
    print((some_non_latin_string()))
