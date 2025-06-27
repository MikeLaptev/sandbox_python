from typing import List


class DivideStringIntoGroupsOfSizeK:
    """
    Leetcode #2138
    Link: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/
    """

    def divide_string(self, s: str, k: int, fill: str) -> List[str]:
        """
        >>> sut = DivideStringIntoGroupsOfSizeK()
        >>> expected = ["ctoyjrwt","ngqwtnnn"]
        >>> actual = sut.divide_string("ctoyjrwtngqwt", 8, "n")
        >>> assert actual == expected, f"expected {expected}; got {actual}"
        >>> expected = ["abc","def","ghi"]
        >>> actual = sut.divide_string("abcdefghi", 3, "x")
        >>> assert actual == expected, f"expected {expected}; got {actual}"
        >>> expected = ["abc","def","ghi","jxx"]
        >>> actual = sut.divide_string("abcdefghij", 3, "x")
        >>> assert actual == expected, f"expected {expected}; got {actual}"
        """
        result = list()
        p = 0
        t = len(s) - len(s) % k
        for q in range(k, t + 1, k):
            result.append(s[p:q])
            p = q

        if t != len(s):
            result.append(s[t : len(s)] + fill * (k - len(s) % k))

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
