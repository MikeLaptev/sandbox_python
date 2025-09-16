from typing import Tuple


class MaximumScoreFromRemovingSubstrings:
    """
    Leetcode #1717
    Link: https://leetcode.com/problems/maximum-score-from-removing-substrings
    """

    def maximum_gain(self, s: str, x: int, y: int) -> int:
        """
        >>> sut = MaximumScoreFromRemovingSubstrings()
        >>> actual: int = sut.maximum_gain('cdbcbbaaabab', 4, 5)
        >>> assert 19 == actual, f'expected 19; got {actual}'
        >>> actual = sut.maximum_gain('aabbaaxybbaabb', 5, 4)
        >>> assert 20 == actual, f'expected 20; got {actual}'
        >>> actual = sut.maximum_gain('cdbcbbaaabab', 4, 4)
        >>> assert 16 == actual, f'expected 16; got {actual}'
        """

        max_gain: str = "ab" if x > y else "ba"
        min_gain: str = "ab" if x <= y else "ba"

        count: int = 0
        q: str = s
        t, q = self.process(q, max_gain)
        count += t * max(x, y)

        t, q = self.process(q, min_gain)
        count += t * min(x, y)

        return count

    def process(self, s: str, gain: str) -> Tuple[int, str]:
        count = 0
        q = ""
        for i, c in enumerate(s):
            q += c
            if q.endswith(gain):
                q = q[: len(q) - len(gain)]
                count += 1
        return count, q

    def maximum_gain_opt(self, s: str, x: int, y: int) -> int:
        """
        >>> sut = MaximumScoreFromRemovingSubstrings()
        >>> actual: int = sut.maximum_gain_opt('cdbcbbaaabab', 4, 5)
        >>> assert 19 == actual, f'expected 19; got {actual}'
        >>> actual = sut.maximum_gain_opt('aabbaaxybbaabb', 5, 4)
        >>> assert 20 == actual, f'expected 20; got {actual}'
        >>> actual = sut.maximum_gain_opt('cdbcbbaaabab', 4, 4)
        >>> assert 16 == actual, f'expected 16; got {actual}'
        """
        if x > y:
            return self.process_opt(s, "a", "b", x, y)
        else:
            return self.process_opt(s, "b", "a", y, x)

    def process_opt(self, s: str, a: str, b: str, x: int, y: int) -> int:
        c1 = c2 = ans = 0
        s += "c"
        for c in s:
            if c == a:
                c1 += 1
            elif c == b:
                if c1 == 0:
                    c2 += 1
                else:
                    ans += x
                    c1 -= 1
            else:
                ans += y * min(c1, c2)
                c1 = c2 = 0
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
