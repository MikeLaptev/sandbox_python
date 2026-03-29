from typing import List, Dict


class SortIntegersByTheNumberOfSetBits:
    """
    Leetcode #1356
    Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
    """

    def sort_by_bits(self, numbers: List[int]) -> List[int]:
        stats: Dict[int, List[int]] = {}
        for n in numbers:
            c: int = n.bit_count()
            if c not in stats:
                stats[c] = list()
            stats[c].append(n)

        result: List[int] = []
        for i in sorted(stats):
            result += sorted(stats[i])

        return result
