from typing import List, Tuple
from itertools import combinations


class BinaryWatch:
    """
    Leetcode #401
    Link: https://leetcode.com/problems/binary-watch
    """

    def read_binary_watch(self, turned_on: int) -> List[str]:
        """
        >>> s = BinaryWatch()
        >>> assert ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"] == sorted(s.read_binary_watch(1)), f"got: sorted({s.read_binary_watch(1)})"
        >>> assert [] == s.read_binary_watch(9), f"got: {s.read_binary_watch(9)}"
        """
        result: List[str] = []
        leds: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for combination in combinations(leds, turned_on):
            h, m = self.get_time(list(combination))
            if 0 <= h <= 11 and 0 <= m <= 59:
                result.append(f"{h}" + ":" + f"{m:02}")

        return result

    def get_time(self, combination: List[int]) -> Tuple[int, int]:
        h: int = 0
        m: int = 0
        for i in combination:
            if i <= 3:
                h += 1 << i
            else:
                m += 1 << (i - 4)
        return h, m


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
