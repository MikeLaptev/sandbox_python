from os import linesep
from stepic.discrete_math.graphs.vertex_with_adjacency_list import Vertex

__author__ = 'mlaptev'


class Graph(object):

    def __init__(self, _vs):
        self._vertexes = dict([(_v, Vertex(_v)) for _v in list(_vs)])

    def __len__(self):
        return len(self._vertexes)

    @property
    def vertexes_names(self):
        return self._vertexes.keys()

    @property
    def vertexes(self):
        return self._vertexes.values()

    def add_edge(self, start_vertex, finish_vertex):
        if (start_vertex in self._vertexes) and (finish_vertex in self._vertexes):
            self._vertexes.get(start_vertex).add_adjacent_vertex_id(finish_vertex)
            self._vertexes.get(finish_vertex).add_adjacent_vertex_id(start_vertex)
            return True
        return False

    def adjacency_list_of_names_for_vertex(self, vertex):
        vertex_object = self._vertexes.get(vertex, None)
        if vertex_object is not None:
            return vertex_object.adjacency_list_of_vertex_ids
        return None

    def adjacency_list_for_vertex(self, vertex):
        vertex_object = self._vertexes.get(vertex.name, None)
        if vertex_object is not None:
            return [self._vertexes.get(_id) for _id in vertex_object.adjacency_list_of_vertex_ids]
        return None

    def __str__(self):
        output_string = ""
        output_string += "The graphs contains {} vertexes {}".format(len(self._vertexes), linesep)
        output_string += "Edges are: {}".format(linesep)
        for vertex_name, vertex_object in self._vertexes.items():
            output_string += "From {} to {}{}".format(vertex_object.name, list(vertex_object.adjacency_list_of_vertex_ids), linesep)
        return output_string
