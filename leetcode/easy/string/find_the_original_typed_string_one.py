class FindTheOriginalTypedStringI:
    """
    Leetcode #3330
    Link: https://leetcode.com/problems/find-the-original-typed-string-i
    """

    def possible_string_count_opt(self, word: str) -> int:
        """
        >>> sut = FindTheOriginalTypedStringI()
        >>> expected = 5
        >>> word = "abbcccc"
        >>> actual = sut.possible_string_count_opt(word)
        >>> assert expected == actual, f"expected {expected}; got {actual}; word {word}"
        >>> expected = 1
        >>> word = "abcd"
        >>> actual = sut.possible_string_count_opt(word)
        >>> assert expected == actual, f"expected {expected}; got {actual}; word {word}"
        >>> expected = 4
        >>> word = "aaaa"
        >>> actual = sut.possible_string_count_opt(word)
        >>> assert expected == actual, f"expected {expected}; got {actual}; word {word}"
        """
        n = len(word)
        res = 1
        for i in range(1, n):
            cur = word[i]
            prev = word[i - 1]
            if cur == prev:
                res += 1

        return res

    def possible_string_count(self, word: str) -> int:
        """
        >>> sut = FindTheOriginalTypedStringI()
        >>> expected = 5
        >>> word = "abbcccc"
        >>> actual = sut.possible_string_count(word)
        >>> assert expected == actual, f"expected {expected}; got {actual}; word {word}"
        >>> expected = 1
        >>> word = "abcd"
        >>> actual = sut.possible_string_count(word)
        >>> assert expected == actual, f"expected {expected}; got {actual}; word {word}"
        >>> expected = 4
        >>> word = "aaaa"
        >>> actual = sut.possible_string_count(word)
        >>> assert expected == actual, f"expected {expected}; got {actual}; word {word}"
        """
        stats = list()
        for l in word:
            if stats and stats[-1][0] == l:
                stats[-1][1] += 1
            else:
                stats.append([l, 1])

        result = 1
        for s in stats:
            result += s[1] - 1

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
