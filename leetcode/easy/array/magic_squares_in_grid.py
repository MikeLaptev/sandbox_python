from typing import List, Set


class MagicSquaresInGrid:
    """
    Leetcode #840
    Link: https://leetcode.com/problems/magic-squares-in-grid
    """

    __expected: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def num_magic_squares_inside(self, grid: List[List[int]]) -> int:
        """
        >>> sut = MagicSquaresInGrid()
        >>> expected = 1
        >>> actual = sut.num_magic_squares_inside([[4,3,8,4],[9,5,1,9],[2,7,6,2]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 0
        >>> actual = sut.num_magic_squares_inside([[8]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 0
        >>> actual = sut.num_magic_squares_inside([[11, 11, 11], [11, 11, 11], [11, 11, 11]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        res: int = 0
        # safe-guard
        if len(grid) < 2 or len(grid[0]) < 2:
            return res

        for i in range(len(grid) - 2):
            for j in range(len(grid[i]) - 2):
                if self.is_magic_square(grid, i, j):
                    res += 1

        return res

    def is_magic_square(self, grid: List[List[int]], r: int, c: int) -> bool:
        if grid[r + 1][c + 1] != 5:
            return False

        n: Set[int] = set()
        for i in range(3):
            for j in range(3):
                n.add(grid[r + i][c + j])
        if n != self.__expected:
            return False

        e: int = grid[r][c] + grid[r + 1][c] + grid[r + 2][c]

        # rows
        for i in range(3):
            if grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i] != e:
                return False

        # columns
        for i in range(3):
            if grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2] != e:
                return False

        # diagonals
        if (
            grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != e
            or grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2] != e
        ):
            return False

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
