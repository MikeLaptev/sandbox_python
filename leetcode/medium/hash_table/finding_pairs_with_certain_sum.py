from collections import Counter
from typing import List


class FindSumPairs:
    """
    Leetcode #1865
    Link: https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
    """

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.counter1 = Counter(nums1)
        self.nums2 = nums2
        self.counter2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.counter2[self.nums2[index]] -= 1
        if self.counter2[self.nums2[index]] == 0:
            del self.counter2[self.nums2[index]]
        self.nums2[index] += val
        self.counter2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        r = 0
        for elem, cnt in self.counter1.items():
            if tot - elem in self.counter2:
                r += cnt * self.counter2[tot - elem]
        return r


if __name__ == '__main__':
    # scenario 1
    find_sum_pairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
    # return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
    actual = find_sum_pairs.count(7)
    assert 8 == find_sum_pairs.count(7), f"expected 8, got {actual}"
    find_sum_pairs.add(3, 2)  # now nums2 = [1,4,5,4,5,4]
    # return 2; pairs (5,2), (5,4) make 3 + 5
    actual = find_sum_pairs.count(8)
    assert 2 == actual, f"expected 2, got {actual}"
    # return 1; pair (5,0) makes 3 + 1
    actual = find_sum_pairs.count(4)
    assert 1 == actual, f"expected 1, got {actual}"
    find_sum_pairs.add(0, 1)  # now nums2 = [2,4,5,4,5,4]
    find_sum_pairs.add(1, 1)  # now nums2 = [2,5,5,4,5,4]
    # return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
    actual = find_sum_pairs.count(7)
    assert 11 == find_sum_pairs.count(7), f"expected 11, got {actual}"
