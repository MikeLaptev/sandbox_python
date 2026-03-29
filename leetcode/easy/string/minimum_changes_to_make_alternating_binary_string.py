class MinimumChangesToMakeAlternatingBinaryString:
    """
    Leetcode #1758
    Link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
    """

    def min_operations(self, s: str) -> int:
        """
        >>> sut = MinimumChangesToMakeAlternatingBinaryString()
        >>> actual = sut.min_operations("0100")
        >>> expected = 1
        >>> assert actual == expected, f"expected: {expected}, actual: {actual}"
        >>> actual = sut.min_operations("10")
        >>> expected = 0
        >>> assert actual == expected, f"expected: {expected}, actual: {actual}"
        >>> actual = sut.min_operations("1111")
        >>> expected = 2
        >>> assert actual == expected, f"expected: {expected}, actual: {actual}"
        """
        odd: int = 0
        even: int = 0
        for i in range(len(s)):
            if i & 1 == 0:
                if s[i] == "1":
                    odd += 1
                else:
                    even += 1
            else:
                if s[i] == "1":
                    even += 1
                else:
                    odd += 1

        return min(odd, even)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
