class MaximumDifferenceBetweenEvenAndOddFrequencyI:
    """
    Leetcode #3442
    Link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i
    """

    def max_difference(self, s: str) -> int:
        """
        >>> sut = MaximumDifferenceBetweenEvenAndOddFrequencyI()
        >>> actual = sut.max_difference("aaaaabbc")
        >>> assert actual == 3
        """
        counters = dict()
        for c in s:
            counters[c] = (counters[c] if c in counters else 0) + 1

        odd = None
        even = None
        for k, v in list(counters.items()):
            if (v & 1) == 1:
                odd = v if not odd else max(odd, v)
            else:
                even = v if not even else min(even, v)

        return (odd if odd else 0) - (even if even else 0)

    def max_difference_opt(self, s: str) -> int:
        """
        >>> sut = MaximumDifferenceBetweenEvenAndOddFrequencyI()
        >>> actual = sut.max_difference_opt("aaaaabbc")
        >>> assert actual == 3
        """
        from collections import Counter

        freq = Counter(s)
        odd = 0
        even = len(s)
        for cnt in list(freq.values()):
            if (cnt & 1) == 1:
                odd = max(odd, cnt)
            elif cnt != 0:
                even = min(even, cnt)
        return odd - even


if __name__ == "__main__":
    import doctest

    doctest.testmod()
