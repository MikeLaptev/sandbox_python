__author__ = 'Mikhail'


"""
Total amount of perfect matching for full graphs with 2*n vertexes could be calculated by the following formula:
(multiplication by k from 0 till n of (n-k)*(2*(n-k)-1))/(n!)
"""


def full_graph_with_2_n_vertexes(n):
    """
    >>> full_graph_with_2_n_vertexes(10)
    654729075L
    """
    result = 1
    for i in range(1, n+1):
        result *= (i*(2*i-1))
    for i in range(1, n+1):
        result /= i
    return result
