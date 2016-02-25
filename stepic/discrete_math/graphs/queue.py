__author__ = 'mlaptev'


class Queue(object):

    def __init__(self):
        """
        Initialization of an internal Queue structure
        :return:
        """
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self) != 0:
            return self.queue.pop(0)
        return None

    @property
    def first(self):
        if len(self) != 0:
            return self.queue[0]
        return None
