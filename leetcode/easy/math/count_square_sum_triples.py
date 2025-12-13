from bisect import bisect_left
from typing import List, Set


class CountSquareSumTriples:
    """
    Leetcode #1925
    Link: https://leetcode.com/problems/count-square-sum-triples
    """

    def count_triples(self, n: int) -> int:
        """
        >>> sut = CountSquareSumTriples()
        >>> actual = sut.count_triples(5)
        >>> assert 2 == actual, f"expected 2, got {actual}"
        >>> actual = sut.count_triples(10)
        >>> assert 4 == actual, f"expected 4, got {actual}"
        """
        r: int = 0
        squares: List[int] = [i * i for i in range(1, n + 1)]

        for i in range(0, len(squares)):
            for j in range(i, len(squares)):
                k = bisect_left(squares, squares[i] + squares[j])
                if k != len(squares) and squares[k] == squares[i] + squares[j]:
                    r += 2

        return r

    def count_triples_opt(self, n: int) -> int:
        """
        >>> sut = CountSquareSumTriples()
        >>> actual = sut.count_triples_opt(5)
        >>> assert 2 == actual, f"expected 2, got {actual}"
        >>> actual = sut.count_triples_opt(10)
        >>> assert 4 == actual, f"expected 4, got {actual}"
        """
        r: int = 0
        squares: Set[int] = set([i**2 for i in range(1, n + 1)])

        for x in range(1, n + 1):
            x_squared = x**2
            for y in range(x + 1, n + 1):
                if x_squared + y**2 in squares:
                    r += 2

        return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
