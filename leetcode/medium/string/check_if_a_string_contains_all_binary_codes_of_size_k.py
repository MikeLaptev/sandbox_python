from typing import Set


class CheckIfStringContainsAllBinaryCodesOfSizeK:
    """
    Leetcode #1461
    Link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k
    """

    def has_all_codes(self, s: str, k: int) -> bool:
        """
        >>> sut = CheckIfStringContainsAllBinaryCodesOfSizeK()
        >>> assert True == sut.has_all_codes("00110110", 2)
        >>> assert True == sut.has_all_codes("0110", 1)
        >>> assert False == sut.has_all_codes("0110", 2)
        """
        expected_length: int = 2**k
        distinct: Set[str] = set()
        for i in range(len(s) - k + 1):
            distinct.add(s[i : i + k])
            if len(distinct) == expected_length:
                return True

        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
