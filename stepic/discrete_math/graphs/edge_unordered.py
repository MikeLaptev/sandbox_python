from stepic.discrete_math.graphs.vertex_with_adjacency_list import Vertex

__author__ = "mlaptev"


class Edge(object):

    def __init__(self, first_vertex, second_vertex):
        """
        Constructor
        :param first_vertex: object of type :Vertex:
        :param second_vertex: object of type :Vertex:
        :return:
        """
        # initialize first vertex
        if isinstance(first_vertex, Vertex):
            self._vertex_one = first_vertex
        else:
            self._vertex_one = Vertex(first_vertex)
        # initialize second vertex
        if isinstance(second_vertex, Vertex):
            self._vertex_two = second_vertex
        else:
            self._vertex_two = Vertex(second_vertex)

    @property
    def vertex_one(self):
        return self._vertex_one

    @vertex_one.setter
    def vertex_one(self, new_vertex):
        self._vertex_one = new_vertex

    @property
    def vertex_two(self):
        return self._vertex_two

    @vertex_two.setter
    def vertex_two(self, new_vertex):
        self._vertex_two = new_vertex

    @property
    def is_the_same_color(self):
        return self._vertex_one.color == self._vertex_two.color
