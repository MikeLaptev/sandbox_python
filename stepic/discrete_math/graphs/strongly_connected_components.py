# coding=utf-8
from stepic.discrete_math.graphs.stack import Stack
from stepic.discrete_math.graphs.graph_with_adjacency_list import Graph

__author__ = 'mlaptev'

# Найти количество компонент связности неориентированного графа при помощи поиска в глубину.
#
# Формат входных данных:
# На вход подаётся описание графа.
# В первой строке указаны два натуральных числа, разделенные пробелом: число вершин v <= 1000 и число рёбер e <= 1000.
# В следующих e строках содержатся описания рёбер.
# Каждое ребро задаётся разделённой пробелом парой номеров вершин, которые это ребро соединяет.
# Считается, что вершины графа пронумерованы числами от 1 до v.
#
# Формат выходных данных:
# Одно число — количество компонент связности графа.


def calculate_connected_components(graph):
    """
    This function calculates connected components.
    Calculation based on depth-first-search algorithm
    :param graph:
    :return:
    """
    if len(graph) == 0:
        return 0
    stack = Stack()
    number_of_connected_components = 0
    all_vertexes = graph.vertexes_names
    while len(all_vertexes) != 0:
        stack.push(all_vertexes[0])
        while len(stack) != 0:
            current_vertex = stack.pop()
            if current_vertex in all_vertexes:
                all_vertexes.remove(current_vertex)
            for adjacent_vertex in graph.adjacency_list_of_names_for_vertex(current_vertex):
                if adjacent_vertex in all_vertexes:
                    stack.push(adjacent_vertex)
        number_of_connected_components += 1
    return number_of_connected_components

if __name__ == "__main__":
    # data initialization
    v, e = map(lambda x: int(x), input().split())
    edges = list()
    for _ in range(e):
        edges.append(map(lambda x: int(x), input().split()))
    graph = Graph(range(1, v + 1))
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    print(calculate_connected_components(graph))
