class CheckIfDigitsAreEqualInStringAfterOperationsI:
    """
    Leetcode #3461
    Link: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i
    """

    def has_same_digits(self, s: str) -> bool:
        """
        >>> sut = CheckIfDigitsAreEqualInStringAfterOperationsI()
        >>> assert True == sut.has_same_digits('3902')
        >>> assert False == sut.has_same_digits('34789')
        """
        if len(s) == 2:
            return s[0] == s[1]
        n: str = ""
        for i in range(0, len(s) - 1):
            n += str((ord(s[i]) + ord(s[i + 1])) % 10)
        return self.has_same_digits(n)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
