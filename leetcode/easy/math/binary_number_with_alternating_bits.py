class BinaryNumberWithAlternatingBits:
    """
    Leetcode #401
    Link: https://leetcode.com/problems/binary-watch
    """

    def has_alternating_bits(self, n: int) -> bool:
        """
        >>> s = BinaryNumberWithAlternatingBits()
        >>> assert True == s.has_alternating_bits(5), f"expected True, got {s.has_alternating_bits(5)}"
        >>> assert False == s.has_alternating_bits(7), f"expected False, got {s.has_alternating_bits(7)}"
        >>> assert False == s.has_alternating_bits(11), f"expected False, got {s.has_alternating_bits(11)}"
        """
        b: bool = n & 1 == 1
        n >>= 1
        while n > 0:
            t: bool = n & 1 == 1
            if b == t:
                return False
            b = t
            n >>= 1

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
