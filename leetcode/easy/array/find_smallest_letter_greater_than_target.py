from bisect import bisect
from typing import List


class FindSmallestLetterGreaterThanTarget:
    """
    Leetcode #744
    Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target
    """

    def next_greatest_letter(self, letters: List[str], target: str) -> str:
        p: int = bisect.bisect_right(letters, target)
        if p == len(letters):
            return letters[0]
        return letters[p]
