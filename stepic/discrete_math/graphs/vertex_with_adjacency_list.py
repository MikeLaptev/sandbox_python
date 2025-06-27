__author__ = "mlaptev"


class Vertex(object):

    def __init__(self, _n):
        self._name = _n
        self._adjacency_list = set()
        self._color = 0

    @property
    def name(self):
        return self._name

    def add_adjacent_vertex_id(self, _v):
        self._adjacency_list.add(_v)

    def is_adjacent_vertex_id(self, _v):
        return _v in self._adjacency_list

    @property
    def adjacency_list_of_vertex_ids(self):
        return self._adjacency_list

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
