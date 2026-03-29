class CheckIfAllAAppearsBeforeAllB:

    def check_string(self, s: str) -> bool:
        """
        >>> sut = CheckIfAllAAppearsBeforeAllB()
        >>> assert True == sut.check_string('aaabbb'), f"expected True, but got {sut.check_string('aaabbb')}"
        >>> assert True == sut.check_string('aaa'), f"expected True, but got {sut.check_string('aaa')}"
        >>> assert True == sut.check_string('bbbb'), f"expected True, but got {sut.check_string('bbbb')}"
        >>> assert False == sut.check_string('ababab'), f"expected False, but got {sut.check_string('ababab')}"
        """
        count_of_b: int = 0
        for c in s:
            if c == "b":
                count_of_b += 1
            else:
                if count_of_b > 0:
                    return False

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
