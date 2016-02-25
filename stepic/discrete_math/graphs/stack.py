__author__ = 'mlaptev'


class Stack(object):

    def __init__(self):
        """
        Initialization of an internal Stack structure
        :return:
        """
        self.stack = list()

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self) != 0:
            return self.stack.pop()
        return None

    @property
    def first(self):
        if len(self) != 0:
            return self.stack[-1]
        return None
