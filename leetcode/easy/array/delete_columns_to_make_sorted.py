from typing import List


class DeleteColumnsToMakeSorted:
    """
    Leetcode #3318
    Link: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i
    """

    def min_deletion_size(self, strs: List[str]) -> int:
        """
        >>> sut = DeleteColumnsToMakeSorted()
        >>> strs = ["cba", "daf", "ghi"]
        >>> actual = 1
        >>> expected = sut.min_deletion_size(strs)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> strs = ["a", "b"]
        >>> actual = 0
        >>> expected = sut.min_deletion_size(strs)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> strs = ["zyx", "wvu", "tsr"]
        >>> actual = 3
        >>> expected = sut.min_deletion_size(strs)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        res: int = 0
        ncol = len(strs[0])
        for col in range(ncol):
            res += self.__is_column_not_sorted(strs, col)

        return res

    def __is_column_not_sorted(self, strs: List[str], col: int) -> bool:
        for i in range(len(strs) - 1):
            if strs[i][col] > strs[i + 1][col]:
                return True

        return False

    def min_deletion_size_opt(self, strs: List[str]) -> int:
        """
        >>> sut = DeleteColumnsToMakeSorted()
        >>> strs = ["cba", "daf", "ghi"]
        >>> actual = 1
        >>> expected = sut.min_deletion_size_opt(strs)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> strs = ["a", "b"]
        >>> actual = 0
        >>> expected = sut.min_deletion_size_opt(strs)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> strs = ["zyx", "wvu", "tsr"]
        >>> actual = 3
        >>> expected = sut.min_deletion_size_opt(strs)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        return sum(col != sorted(col) for col in map(lambda x: list(x), zip(*strs)))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
