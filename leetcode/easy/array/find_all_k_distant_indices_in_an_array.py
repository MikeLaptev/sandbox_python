from typing import List


class FindAllKDistantIndicesInAnArray:
    """
    Leetcode #2200
    Link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array
    """

    def find_k_distant_indices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = list()
        for i, n in enumerate(nums):
            if n == key:
                l = max((result[-1] + 1) if len(result) != 0 else 0, i - k)
                r = min(len(nums), i + k + 1)
                result += list(range(l, r, 1))

        return result
