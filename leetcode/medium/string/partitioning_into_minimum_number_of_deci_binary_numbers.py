class PartitioningIntoMinimumNumberOfDeciBinaryNumbers:
    """
    Leetcode #1689
    Link: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers
    """

    def min_partitions(self, n: str) -> int:
        """
        >>> sut = PartitioningIntoMinimumNumberOfDeciBinaryNumbers()
        >>> assert 9 == sut.min_partitions('27346209830709182346')
        >>> assert 8 == sut.min_partitions('82734')
        """
        result: int = 0

        for digit in n:
            result = max(result, int(digit))

        return result

    def min_partitions_opt(self, n: str) -> int:
        """
        >>> sut = PartitioningIntoMinimumNumberOfDeciBinaryNumbers()
        >>> assert 9 == sut.min_partitions_opt('27346209830709182346')
        >>> assert 8 == sut.min_partitions_opt('82734')
        """
        for d in "987654321":
            if d in n:
                return int(d)
        return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
