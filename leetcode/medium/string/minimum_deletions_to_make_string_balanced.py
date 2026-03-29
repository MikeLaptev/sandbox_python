class MinimumDeletionsToMakeStringBalanced:
    """
    Leetcode #1653
    Link: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced
    """

    def minimum_deletions(self, s: str) -> int:
        """
        >>> sut = MinimumDeletionsToMakeStringBalanced()
        >>> assert 2 == sut.minimum_deletions('aababbab'), f"expected 2, but got {sut.minimum_deletions('aababbab')}"
        >>> assert 2 == sut.minimum_deletions('bbaaaaabb'), f"expected 2, but got {sut.minimum_deletions('baaaaabb')}"
        >>> assert 0 == sut.minimum_deletions('aaaa'), f"expected 0, but got {sut.minimum_deletions('aaaa')}"
        >>> assert 0 == sut.minimum_deletions('bbbb'), f"expected 0, but got {sut.minimum_deletions('bbbb')}"
        """
        r: int = 0
        count_of_b: int = 0
        for c in s:
            if c == "b":
                count_of_b += 1
            else:
                if count_of_b > 0:
                    count_of_b -= 1
                    r += 1

        return r


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
