class VowelsGameInString:
    """
    Leetcode #3227
    Link: https://leetcode.com/problems/vowels-game-in-a-string/description
    """

    def does_alice_win(self, s: str) -> bool:
        """
        >>> sut = VowelsGameInString()
        >>> assert True == sut.does_alice_win("leetcode")
        >>> assert False == sut.does_alice_win("bbcd")
        """
        count = sum([1 for c in s if c in {"a", "e", "i", "o", "u"}])
        if count == 0:
            return False
        return True

    def does_alice_win_2(self, s: str) -> bool:
        """
        >>> sut = VowelsGameInString()
        >>> assert True == sut.does_alice_win_2("leetcode")
        >>> assert False == sut.does_alice_win_2("bbcd")
        """
        return bool(set(s) & set("aeiou"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
