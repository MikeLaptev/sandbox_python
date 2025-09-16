import string


class ValidWord:
    """
    Leetcode #3136
    Link: https://leetcode.com/problems/valid-word/description
    """

    def is_valid(self, word: str) -> bool:
        """
        >>> sut = ValidWord()
        >>> assert True == sut.is_valid('234Adas')
        >>> assert False == sut.is_valid('b3')
        >>> assert False == sut.is_valid('a3$e')
        >>> assert True == sut.is_valid('aya')
        """
        is_len: bool = len(word) >= 3
        if not is_len:
            return False
        has_consonant: bool = False
        has_vowel: bool = False

        for c in word:
            if c in string.ascii_letters:
                if c.lower() in ["a", "e", "i", "o", "u"]:
                    has_vowel = True
                else:
                    has_consonant = True
            elif c not in string.digits:
                return False

        return has_vowel and has_consonant


if __name__ == "__main__":
    import doctest

    doctest.testmod()
