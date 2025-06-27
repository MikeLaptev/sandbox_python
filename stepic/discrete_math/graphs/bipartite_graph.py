# coding=utf-8
from stepic.discrete_math.graphs.stack import Stack
from stepic.discrete_math.graphs.graph_with_adjacency_list import Graph


__author__ = "Mikhail"

"""
Проверить является ли граф двудольным.

Формат входных данных:
В первой строке указаны два числа разделенных пробелом:
v (число вершин) и e (число ребер).
В следующих e строках указаны пары вершин, соединенных ребром.

Выполняются ограничения:
0 <= v <= 1000,
0 <= e <= 1000.

Формат выходных данных:
Одно слово: YES, если граф двудолен, или NO, в противном случае.

Sample Input 1:
4 2
1 2
3 2

Sample Output 1:
YES

Sample Input 2:
3 3
1 2
2 3
3 1
Sample Output 2:
NO
"""


def is_graph_bipartite(graph):
    """
    This function check is graph bipartite or not
    Calculation based on depth-first-search algorithm
    :param graph:
    :return:
    """
    if len(graph) == 0:
        return 0
    stack = Stack()
    first_color = 0
    second_color = 1
    all_vertexes = graph.vertexes
    while len(all_vertexes) != 0:
        all_vertexes[0].color = first_color
        stack.push(all_vertexes[0])
        while len(stack) != 0:
            current_vertex = stack.pop()
            color_to_add = current_vertex.color
            # inverting
            if color_to_add == first_color:
                color_to_add = second_color
            else:
                color_to_add = first_color
            if current_vertex in all_vertexes:
                all_vertexes.remove(current_vertex)
            for adjacent_vertex in graph.adjacency_list_for_vertex(current_vertex):
                if adjacent_vertex in all_vertexes:
                    adjacent_vertex.color = color_to_add
                    stack.push(adjacent_vertex)
    for vertex in graph.vertexes:
        for adjacent_vertex in graph.adjacency_list_for_vertex(vertex):
            if vertex.color == adjacent_vertex.color:
                return False
    return True


if __name__ == "__main__":
    # data initialization
    v, e = [int(x) for x in input().split()]
    edges = list()
    for _ in range(e):
        edges.append([int(x) for x in input().split()])
    graph = Graph(list(range(1, v + 1)))
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    print(("YES" if is_graph_bipartite(graph) else "NO"))
