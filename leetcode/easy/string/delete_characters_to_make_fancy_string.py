class DeleteCharactersToMakeFancyString:
    """
    Leetcode #1957
    Link: https://leetcode.com/problems/delete-characters-to-make-fancy-string
    """

    def make_fancy_string(self, s: str) -> str:
        """
        >>> sut = DeleteCharactersToMakeFancyString()
        >>> assert "aabaa" == sut.make_fancy_string("aaabaaaa")
        """
        i = 0
        while i < len(s) - 2:
            if s[i] == s[i + 1] == s[i + 2]:
                s = s[:i] + s[i + 1:]
            else:
                i += 1
        return s

    def make_fancy_string_opt(self, s: str) -> str:
        """
        >>> sut = DeleteCharactersToMakeFancyString()
        >>> assert "aabaa" == sut.make_fancy_string_opt("aaabaaaa")
        """
        res = s[0]
        last = s[0]
        repeat = 1
        for ch in s[1:]:
            if ch == last:
                if repeat >= 2:
                    continue
                repeat += 1
            else:
                last = ch
                repeat = 1
            res += ch
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
