class CheckIfStringsCanBeMadeEqualWithOperationsI:
    """
    Leetcode #2839
    Link: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/
    """

    def can_be_equal(self, s1: str, s2: str) -> bool:
        """
        >>> sut = CheckIfStringsCanBeMadeEqualWithOperationsI()
        >>> assert False == sut.can_be_equal('jjgg', 'gjgj')
        >>> assert True == sut.can_be_equal('abcd', 'cdab')
        >>> assert False == sut.can_be_equal('abcd', 'dacb')
        """
        odd_s1: list = []
        even_s1: list = []

        for index, char in enumerate(s1):
            if index & 1 == 0:
                even_s1.append(char)
            else:
                odd_s1.append(char)

        odd_s2: list = []
        even_s2: list = []
        for index, char in enumerate(s2):
            if index & 1 == 0:
                even_s2.append(char)
            else:
                odd_s2.append(char)

        if sorted(odd_s1) != sorted(odd_s2) or sorted(even_s1) != sorted(even_s2):
            return False

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
