import bisect
from typing import List


class SuccessfulPairsOfSpellsAndPotions:
    """
    Leetcode #2300
    Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions
    """

    def successful_pairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        """
        >>> sut = SuccessfulPairsOfSpellsAndPotions()
        >>> sp = [5, 1, 3]
        >>> po = [1, 2, 3, 4, 5]
        >>> su = 7
        >>> expected = [4, 0, 3]
        >>> actual = sut.successful_pairs(sp, po, su)
        >>> assert expected == actual, f"expected {expected}, got {actual} for spells {sp}"
        >>> sp = [3, 1, 2]
        >>> po = [8, 5, 8]
        >>> su = 16
        >>> expected = [2, 0, 2]
        >>> actual = sut.successful_pairs(sp, po, su)
        >>> assert expected == actual, f"expected {expected}, got {actual} for spells {sp}"
        """
        p = len(potions)
        potions.sort()
        result = [p - bisect.bisect_left(potions, success / s) for s in spells]

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
