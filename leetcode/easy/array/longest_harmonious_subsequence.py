from collections import Counter
from typing import List


class LongestHarmoniousSubsequence:
    """
    Leetcode #594
    Link: https://leetcode.com/problems/longest-harmonious-subsequence
    """

    def find_lhs(self, nums: List[int]) -> int:
        result = 0
        counter = Counter()
        for n in nums:
            counter[n] += 1

        for l in counter:
            if l + 1 in counter:
                result = max(result, counter[l] + counter[l + 1])

        return result

    def find_lhs_alternative(self, nums: List[int]) -> int:
        result = 0
        stats = dict()
        for n in nums:
            stats[n] = stats.get(n, 0) + 1

        if len(stats) > 1:
            for k, v in stats.items():
                if k + 1 in stats:
                    result = max(result, v + stats[k + 1])

        return result
