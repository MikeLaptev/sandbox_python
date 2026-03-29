class AddBinary:
    """
    Leetcode #67
    Link: https://leetcode.com/problems/add-binary/
    """

    def add_binary(self, a: str, b: str) -> str:
        """
        >>> sut = AddBinary()
        >>> assert '11110' == sut.add_binary('1111', '1111')
        >>> assert '100' == sut.add_binary('11', '1'), f"expected 100, got {sut.add_binary('11', '1')}"
        >>> assert '10101' == sut.add_binary('1010', '1011'), f"expected 10101, got {sut.add_binary('1010', '1011')}"
        >>> assert '10000' == sut.add_binary('10000', '0')
        >>> assert '10001' == sut.add_binary('10000', '1')
        >>> assert '10000' == sut.add_binary('1111', '1')
        """
        res: str = ""
        bit: bool = False
        for i in range(0, max(len(a), len(b))):
            l: str = "0" if i >= len(a) else a[-i - 1]
            r: str = "0" if i >= len(b) else b[-i - 1]
            if l == "1" and r == "1":
                res += "1" if bit else "0"
                bit = True
            elif l == "0" and r == "0":
                res += "1" if bit else "0"
                if bit:
                    bit = False
            else:
                res += "0" if bit else "1"
        if bit:
            res += "1"

        return res[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
