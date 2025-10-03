from typing import List, Set


class SortVowelsInString:
    """
    Leetcode #2785
    Link: https://leetcode.com/problems/sort-vowels-in-a-string
    """

    def sort_vowels(self, s: str) -> str:
        """
        >>> sut = SortVowelsInString()
        >>> s = "LQRamBOHfq"
        >>> expected = "LQROmBaHfq"
        >>> actual = sut.sort_vowels(s)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        >>> s = "lEetcOde"
        >>> expected = "lEOtcede"
        >>> actual = sut.sort_vowels(s)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        >>> s = "lYmpH"
        >>> expected = "lYmpH"
        >>> actual = sut.sort_vowels(s)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        """
        symbols = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        positions: List[int] = []
        vowels: List[str] = []

        for i, c in enumerate(s):
            if c in symbols:
                positions.append(i)
                vowels.append(c)

        if vowels:
            vowels.sort()
            t: str = ""
            k: int = 0
            for i, c in enumerate(s):
                if k < len(positions) and i == positions[k]:
                    t += vowels[k]
                    k += 1
                else:
                    t += c

            return t

        return s

    def sort_vowels_opt(self, s: str) -> str:
        """
        >>> sut = SortVowelsInString()
        >>> s = "LQRamBOHfq"
        >>> expected = "LQROmBaHfq"
        >>> actual = sut.sort_vowels_opt(s)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        >>> s = "lEetcOde"
        >>> expected = "lEOtcede"
        >>> actual = sut.sort_vowels_opt(s)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        >>> s = "lYmpH"
        >>> expected = "lYmpH"
        >>> actual = sut.sort_vowels_opt(s)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        """
        out: List[str] = []
        vowels: List[str] = []
        positions: List[int] = []

        for i, c in enumerate(s):
            if c in "AEIOUaeiou":
                vowels.append(c)
                positions.append(i)
                out.append("")
            else:
                out.append(c)

        vowels.sort()
        for i in range(len(vowels)):
            out[positions[i]] = vowels[i]

        return "".join(out)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
