class BinaryGap:
    """
    Leetcode #868
    Link: https://leetcode.com/problems/binary-gap
    """

    def binary_gap(self, n: int) -> int:
        """
        >>> sut = BinaryGap()
        >>> assert 2 == sut.binary_gap(22), f"expected 2 but got {sut.binary_gap(22)}"
        >>> assert 0 == sut.binary_gap(8), f"expected 0 but got {sut.binary_gap(8)}"
        >>> assert 2 == sut.binary_gap(5), f"expected 2 but got {sut.binary_gap(5)}"
        >>> assert 11 == sut.binary_gap(2049), f"expected 11 but got {sut.binary_gap(2049)}"
        >>> assert 0 == sut.binary_gap(0), f"expected 0 but got {sut.binary_gap(0)}"
        """
        result: int = 0
        prev: int = -1
        count: int = 0
        while n > 0:
            t: int = n & 1
            if t == 1:
                if prev != -1:
                    result = max(result, abs(prev - count))
                prev = count
            count += 1
            n >>= 1

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
