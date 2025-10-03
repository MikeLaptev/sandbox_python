from typing import List


class Triangle:
    """
    Leetcode #120
    Link: https://leetcode.com/problems/triangle/
    """

    def minimum_total(self, triangle: List[List[int]]) -> int:
        """
        >>> sut = Triangle()
        >>> t = [[2],[3,4],[6,5,7],[4,1,8,3]]
        >>> expected = 11
        >>> actual = sut.minimum_total(t)
        >>> assert expected == actual, f"mismatch for {t}; expected - {expected}; got - {actual}"
        >>> t = [[-10]]
        >>> expected = -10
        >>> actual = sut.minimum_total(t)
        >>> assert expected == actual, f"mismatch for {t}; expected - {expected}; got - {actual}"
        >>> t = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 1], [2, 3, 4, 5, 6], [7, 8, 9, 1, 2, 3]]
        >>> expected = 17
        >>> actual = sut.minimum_total(t)
        >>> assert expected == actual, f"mismatch for {t}; expected - {expected}; got - {actual}"
        """
        return min(self.minimum_total_lvl(triangle, 1, list(triangle[0])))

    def minimum_total_lvl(
        self, triangle: List[List[int]], level: int, current: List[int]
    ) -> List[int]:
        """
        consider:
               1
              2 3
             4 5 6
            7 8 9 1
           2 3 4 5 6
          7 8 9 1 2 3

        """
        if level == len(triangle):
            return current

        # updating current
        r = []
        for i, e in enumerate(triangle[level]):
            if i == 0:
                r.append(e + current[i])
            elif i == len(triangle[level]) - 1:
                r.append(e + current[i - 1])
            else:
                r.append(e + min(current[i - 1], current[i]))

        return self.minimum_total_lvl(triangle, level + 1, r)

    def minimum_total_opt(self, triangle: List[List[int]]) -> int:
        """
        >>> sut = Triangle()
        >>> t = [[2],[3,4],[6,5,7],[4,1,8,3]]
        >>> expected = 11
        >>> actual = sut.minimum_total_opt(t)
        >>> assert expected == actual, f"mismatch for {t}; expected - {expected}; got - {actual}"
        >>> t = [[-10]]
        >>> expected = -10
        >>> actual = sut.minimum_total_opt(t)
        >>> assert expected == actual, f"mismatch for {t}; expected - {expected}; got - {actual}"
        >>> t = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 1], [2, 3, 4, 5, 6], [7, 8, 9, 1, 2, 3]]
        >>> expected = 17
        >>> actual = sut.minimum_total_opt(t)
        >>> assert expected == actual, f"mismatch for {t}; expected - {expected}; got - {actual}"
        """
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
