class ReverseBits:

    def reverse_bits(self, n: int) -> int:
        """
        >>> sut = ReverseBits()
        >>> assert 964176192 == sut.reverse_bits(43261596), f"expected 964176192; got {sut.reverse_bits(43261596)}"
        >>> assert 1073741822 == sut.reverse_bits(2147483644), f"expected 1073741822; got {sut.reverse_bits(2147483644)}"
        """
        res: int = 0
        for i in range(32):
            b: int = n & 1
            n >>= 1
            res <<= 1
            res |= b

        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
