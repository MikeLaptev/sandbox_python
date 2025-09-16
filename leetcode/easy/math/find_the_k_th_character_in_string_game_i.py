class FindTheKthCharacterInStringGameI:
    """
    Leetcode #3304
    Link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i
    """

    def kth_character(self, k: int) -> str:
        """
        >>> sut = FindTheKthCharacterInStringGameI()
        >>> assert 'b' == sut.kth_character(5)
        >>> assert 'c' == sut.kth_character(10)
        """
        base = "a"
        while len(base) < k:
            t: str = ""
            for i, c in enumerate(base):
                t += chr(ord(c) + 1) if c < "z" else "a"
            base += t

        return base[k - 1]

    def kth_character_opt(self, k: int) -> str:
        """
        >>> sut = FindTheKthCharacterInStringGameI()
        >>> assert 'b' == sut.kth_character_opt(5)
        >>> assert 'c' == sut.kth_character_opt(10)
        """
        return chr(ord("a") + (k - 1).bit_count())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
