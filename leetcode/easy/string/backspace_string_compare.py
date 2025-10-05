class BackspaceStringCompare:
    """
    Leetcode #844
    Link: https://leetcode.com/problems/backspace-string-compare/
    """

    def backspace_compare(self, s: str, t: str) -> bool:
        """
        >>> sut = BackspaceStringCompare()
        >>> s = "xywrrmp"
        >>> t = "xywrrmu#p"
        >>> assert True == sut.backspace_compare(s, t), f"expected true for {s} and {t}"
        >>> s = "ab#c"
        >>> t = "ad#c"
        >>> assert True == sut.backspace_compare(s, t), f"expected true for {s} and {t}"
        >>> s = "ab##"
        >>> t = "c#d#"
        >>> assert True == sut.backspace_compare(s, t), f"expected true for {s} and {t}"
        >>> s = "a#c"
        >>> t = "b"
        >>> assert False == sut.backspace_compare(s, t), f"expected true for {s} and {t}"
        """

        i = len(s) - 1
        j = len(t) - 1
        while True:
            position_in_s = self.position_of_next_visible(s, i)
            position_in_t = self.position_of_next_visible(t, j)
            if (
                position_in_s != -1
                and position_in_t == -1
                or position_in_s == -1
                and position_in_t != -1
            ):
                return False
            if position_in_s == -1 and position_in_t == -1:
                return True
            if s[position_in_s] != t[position_in_t]:
                return False

            j = position_in_t - 1
            i = position_in_s - 1

        return True

    def position_of_next_visible(self, q: str, p: int) -> int:
        skip_q = 0
        for i in range(p, -1, -1):
            if skip_q == 0 and q[i] != "#":
                return i
            elif q[i] == "#":
                skip_q += 1
            else:  # symbol
                skip_q -= 1
        return -1

    def backspace_compare_stack(self, s: str, t: str) -> bool:
        """
        >>> sut = BackspaceStringCompare()
        >>> s = "xywrrmp"
        >>> t = "xywrrmu#p"
        >>> assert True == sut.backspace_compare_stack(s, t), f"expected true for {s} and {t}"
        >>> s = "ab#c"
        >>> t = "ad#c"
        >>> assert True == sut.backspace_compare_stack(s, t), f"expected true for {s} and {t}"
        >>> s = "ab##"
        >>> t = "c#d#"
        >>> assert True == sut.backspace_compare_stack(s, t), f"expected true for {s} and {t}"
        >>> s = "a#c"
        >>> t = "b"
        >>> assert False == sut.backspace_compare_stack(s, t), f"expected true for {s} and {t}"
        """
        st1 = []
        st2 = []
        for i in range(len(s)):
            if s[i] == "#" and st1:
                st1.pop()
            elif s[i] != "#":
                st1.append(s[i])
        for i in range(len(t)):
            if t[i] == "#" and st2:
                st2.pop()
            elif t[i] != "#":
                st2.append(t[i])
        return st2 == st1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
