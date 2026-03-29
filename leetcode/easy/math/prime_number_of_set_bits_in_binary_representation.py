import math


class PrimeNumberOfSetBitsInBinaryRepresentation:
    """
    Leetcode #726
    Link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation
    """

    def count_prime_set_bits(self, left: int, right: int) -> int:
        """
        >>> sut = PrimeNumberOfSetBitsInBinaryRepresentation()
        >>> assert 5 == sut.count_prime_set_bits(10, 15), f"expected 5, got {sut.count_prime_set_bits(10, 15)}"
        >>> assert 4 == sut.count_prime_set_bits(6, 10), f"expected 4, got {sut.count_prime_set_bits(6, 10)}"
        """
        result: int = 0

        for i in range(left, right + 1):
            c: int = i.bit_count()
            if self._is_prime(c):
                result += 1

        return result

    def _is_prime(self, n: int) -> bool:
        l: int = math.floor(math.sqrt(n))
        if n > 1:
            for i in range(2, l + 1):
                if (n % i) == 0:
                    return False
            else:
                return True

        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
