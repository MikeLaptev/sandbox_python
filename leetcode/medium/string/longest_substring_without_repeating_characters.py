from typing import Dict


class LongestSubstringWithoutRepeatingCharacters:

    def length_of_longest_substring(self, s: str) -> int:
        """
        >>> sut = LongestSubstringWithoutRepeatingCharacters()
        >>> s = "abcabcbb"
        >>> expected = 3
        >>> actual = sut.length_of_longest_substring(s)
        >>> assert expected == actual, f"expected {expected}; got {actual} for {s}"
        >>> s = "bbbbb"
        >>> expected = 1
        >>> actual = sut.length_of_longest_substring(s)
        >>> assert expected == actual, f"expected {expected}; got {actual} for {s}"
        >>> s = "pwwkew"
        >>> expected = 3
        >>> actual = sut.length_of_longest_substring(s)
        >>> assert expected == actual, f"expected {expected}; got {actual} for {s}"
        """
        if not s:
            return 0

        unique: Dict[str, int] = {}
        longest = 0  # length of the longest
        f = 0  # position from which we started
        for i, c in enumerate(s):
            if c in unique:
                p = unique[c]
                for j in range(f, p + 1):
                    del unique[s[j]]
                f = p + 1
            unique[c] = i
            longest = max(longest, len(unique))
        return longest


if __name__ == "__main__":
    import doctest

    doctest.testmod()
