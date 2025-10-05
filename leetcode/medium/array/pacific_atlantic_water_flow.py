from typing import List, Set, Tuple


class PacificAtlanticWaterFlow:
    """
    Leetcode #417
    Link: https://leetcode.com/problems/pacific-atlantic-water-flow
    """

    movements: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        >>> sut = PacificAtlanticWaterFlow()
        >>> h = [[1,1],[1,1],[1,1]]
        >>> expected = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
        >>> actual = sut.pacific_atlantic(h)
        >>> assert sorted(expected) == sorted(actual), f"expected: {sorted(expected)}, got: {sorted(actual)}"
        >>> h = [[2,1],[1,2]]
        >>> expected = [[0,0],[0,1],[1,0],[1,1]]
        >>> actual = sut.pacific_atlantic(h)
        >>> assert sorted(expected) == sorted(actual), f"expected: {sorted(expected)}, got: {sorted(actual)}"
        >>> h = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        >>> expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        >>> actual = sut.pacific_atlantic(h)
        >>> assert sorted(expected) == sorted(actual), f"expected: {sorted(expected)}, got: {sorted(actual)}"
        >>> h = [[1]]
        >>> expected = [[0,0]]
        >>> actual = sut.pacific_atlantic(h)
        >>> assert sorted(expected) == sorted(actual), f"expected: {sorted(expected)}, got: {sorted(actual)}"
        >>> h = [[1, 1, 1, 1, 1], [1, 3, 3, 3, 1], [1, 3, 2, 3, 1], [1, 3, 3, 3, 1], [1, 1, 1, 1, 1]]
        >>> expected = [[one, two] for one in range(5) for two in range(5)]
        >>> expected.remove([2, 2])
        >>> actual = sut.pacific_atlantic(h)
        >>> assert sorted(expected) == sorted(actual), f"expected: {sorted(expected)}, got: {sorted(actual)}"
        """
        num_rows = len(heights)
        num_cols = len(heights[0])
        pacific_start = [(i, 0) for i in range(num_rows)] + [
            (0, i) for i in range(1, num_cols)
        ]
        atlantic_start = [(i, num_cols - 1) for i in range(num_rows)] + [
            (num_rows - 1, i) for i in range(0, num_cols - 1)
        ]

        pacific_reachable = self.bfs(heights, num_rows, num_cols, pacific_start)
        atlantic_reachable = self.bfs(heights, num_rows, num_cols, atlantic_start)

        return [[i, j] for i, j in (pacific_reachable & atlantic_reachable)]

    def bfs(
        self,
        heights: List[List[int]],
        num_rows: int,
        num_cols: int,
        start: List[Tuple[int, int]],
    ) -> Set[Tuple[int, int]]:
        q = list(start)
        processed: Set[Tuple[int, int]] = set()
        result: Set[Tuple[int, int]] = set()
        while q:
            current = q.pop()
            processed.add(current)
            result.add(current)
            for m in self.movements:
                p = (current[0] + m[0], current[1] + m[1])
                if self.in_island(p, num_rows, num_cols) and p not in processed:
                    if heights[current[0]][current[1]] <= heights[p[0]][p[1]]:
                        q.append(p)

        return result

    def in_island(self, point: Tuple[int, int], num_rows: int, num_cols: int) -> bool:
        return 0 <= point[0] < num_rows and 0 <= point[1] < num_cols


if __name__ == "__main__":
    import doctest

    doctest.testmod()
