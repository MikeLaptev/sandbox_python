class MaximumDifferenceByRemappingDigit:
    """
    Leetcode #2566
    Link: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit
    """

    def mim_max_difference(self, num: int) -> int:
        """
        >>> sut = MaximumDifferenceByRemappingDigit()
        >>> expected = 99009
        >>> actual = sut.mim_max_difference(11891)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        >>> expected = 99
        >>> actual = sut.mim_max_difference(90)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        """
        # looking for minimum
        v: str = str(num)
        r: str = ''
        if v[0] != 0:
            for d in v:
                r += '0' if d == v[0] else d
        minimum: int = int(r)

        # looking for maximum
        p: int = 0
        for i, d in enumerate(v):
            if d != '9':
                p = i
                break
        r = v[:p]
        for i in range(p, len(v)):
            r += '9' if v[i] == v[p] else v[i]
        maximum: int = int(r)

        return maximum - minimum


if __name__ == '__main__':
    import doctest

    doctest.testmod()
