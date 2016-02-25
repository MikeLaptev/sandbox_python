# coding=utf-8
from stepic.discrete_math.graphs.graph_with_adjacency_list import Graph

__author__ = 'Mikhail'

"""
Найдите эйлеров цикл в графе.

Формат входных данных:
В первой строке указаны два числа разделенных пробелом: v (число вершин) и e (число ребер).
В следующих e строках указаны пары вершин, соединенных ребром.
Выполняются ограничения: 2 <= v <= 1000, 0<= e <= 1000.

Формат выходных данных:
Одно слово: NONE, если в графе нет эйлерова цикла, или список вершин в порядке обхода эйлерова цикла, если он есть.


Sample Input 1:
4 2
1 2
3 2
Sample Output 1:
NONE

Sample Input 2:
3 3
1 2
2 3
3 1
Sample Output 2:
1 2 3
"""

# TODO: implementation

if __name__ == "__main__":
    # data initialization
    v, e = map(lambda x: int(x), input().split())
    edges = list()
    for _ in range(e):
        edges.append(map(lambda x: int(x), input().split()))
    graph = Graph(range(1, v + 1))
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
