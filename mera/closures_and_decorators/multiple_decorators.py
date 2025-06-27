"""
Created on Aug, 5 2015

@author: mlaptev
"""


class html_tag_decorator:

    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, function):
        def wrapped_f(*args):
            updated_value = function(*args)
            if updated_value.startswith("<") and updated_value.endswith(">"):
                # already inside HTML tags
                return "<{0}>{1}</{0}>".format(self.tag_name, updated_value)
            else:
                return "<{0}> {1} </{0}>".format(self.tag_name, updated_value)

        return wrapped_f


@html_tag_decorator("div")
@html_tag_decorator("span")
@html_tag_decorator("a")
def hello(name):
    return "Hello, {}".format(name)


if __name__ == "__main__":
    print((hello("Mike")))
