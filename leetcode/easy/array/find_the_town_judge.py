from typing import List


class FindTheTownJudge:
    """
    Leetcode #997
    Link: https://leetcode.com/problems/find-the-town-judge/
    """

    def find_judge(self, n: int, trust: List[List[int]]) -> int:
        """
        >>> sut = FindTheTownJudge()
        >>> expected = 3
        >>> actual = sut.find_judge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])
        >>> assert actual == expected, f"expected {expected}; got {actual}"
        >>> expected = 2
        >>> actual = sut.find_judge(2, [[1,2]])
        >>> assert actual == expected, f"expected {expected}; got {actual}"
        >>> expected = 3
        >>> actual = sut.find_judge(3, [[1,3],[2,3]])
        >>> assert actual == expected, f"expected {expected}; got {actual}"
        >>> expected = -1
        >>> actual = sut.find_judge(3, [[1,3],[2,3],[3,1]])
        >>> assert actual == expected, f"expected {expected}; got {actual}"
        """
        trusted = [0] * n
        for t in trust:
            trusted[t[0] - 1] = trusted[t[0] - 1] - 1
            trusted[t[1] - 1] = trusted[t[1] - 1] + 1

        for i, t in enumerate(trusted):
            if t == n - 1:
                return i + 1

        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
