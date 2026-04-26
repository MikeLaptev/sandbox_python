from typing import List


class DecodeTheSlantedCiphertext:
    """
    Leetcode #2075
    Link: https://leetcode.com/problems/decode-the-slanted-ciphertext
    """

    def decode_ciphertext(self, encoded_text: str, rows: int) -> str:
        """
        >>> sut = DecodeTheSlantedCiphertext()
        >>> encoded_text: str = "whurqonhhaymkrxebpdagccsjvoontnejzqkmqdedwkbjsas t kga kjjchpxkkuraiyvmsx gvvfbkfx yrpydxajzmmelyxy b"
        >>> rows: int = 1
        >>> actual: str = sut.decode_ciphertext(encoded_text, rows)
        >>> expected: str = "whurqonhhaymkrxebpdagccsjvoontnejzqkmqdedwkbjsas t kga kjjchpxkkuraiyvmsx gvvfbkfx yrpydxajzmmelyxy b"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = " b  ac"
        >>> rows: int = 2
        >>> actual: str = sut.decode_ciphertext(encoded_text, rows)
        >>> expected: str = " abc"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = ""
        >>> rows: int = 5
        >>> actual: str = sut.decode_ciphertext(encoded_text, rows)
        >>> expected: str = ""
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = "iveo    eed   l t    olc"
        >>> rows: int = 4
        >>> actual: str = sut.decode_ciphertext(encoded_text, rows)
        >>> expected: str = "i love leetcod"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = "ch   ie   pr"
        >>> rows: int = 3
        >>> actual: str = sut.decode_ciphertext(encoded_text, rows)
        >>> expected: str = "cipher"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = "iveo    eed   l te   olc"
        >>> rows: int = 4
        >>> actual: str = sut.decode_ciphertext(encoded_text, rows)
        >>> expected: str = "i love leetcode"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = "coding"
        >>> rows: int = 1
        >>> actual: str = sut.decode_ciphertext(encoded_text, rows)
        >>> expected: str = "coding"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        if not encoded_text:
            return ""
        result: str = ""
        columns: int = len(encoded_text) // rows
        matrix: List[str] = [
            encoded_text[i : i + columns] for i in range(0, len(encoded_text), columns)
        ]
        while True:
            for j in range(columns):
                for i in range(rows):
                    if i + j >= columns:
                        break
                    result += matrix[i][j + i]
            break
        return result.rstrip()

    def decode_ciphertext_opt(self, encoded_text: str, rows: int) -> str:
        """
        >>> sut = DecodeTheSlantedCiphertext()
        >>> encoded_text: str = "whurqonhhaymkrxebpdagccsjvoontnejzqkmqdedwkbjsas t kga kjjchpxkkuraiyvmsx gvvfbkfx yrpydxajzmmelyxy b"
        >>> rows: int = 1
        >>> actual: str = sut.decode_ciphertext_opt(encoded_text, rows)
        >>> expected: str = "whurqonhhaymkrxebpdagccsjvoontnejzqkmqdedwkbjsas t kga kjjchpxkkuraiyvmsx gvvfbkfx yrpydxajzmmelyxy b"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = " b  ac"
        >>> rows: int = 2
        >>> actual: str = sut.decode_ciphertext_opt(encoded_text, rows)
        >>> expected: str = " abc"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = ""
        >>> rows: int = 5
        >>> actual: str = sut.decode_ciphertext_opt(encoded_text, rows)
        >>> expected: str = ""
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = "iveo    eed   l t    olc"
        >>> rows: int = 4
        >>> actual: str = sut.decode_ciphertext_opt(encoded_text, rows)
        >>> expected: str = "i love leetcod"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = "ch   ie   pr"
        >>> rows: int = 3
        >>> actual: str = sut.decode_ciphertext_opt(encoded_text, rows)
        >>> expected: str = "cipher"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = "iveo    eed   l te   olc"
        >>> rows: int = 4
        >>> actual: str = sut.decode_ciphertext_opt(encoded_text, rows)
        >>> expected: str = "i love leetcode"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> encoded_text: str = "coding"
        >>> rows: int = 1
        >>> actual: str = sut.decode_ciphertext_opt(encoded_text, rows)
        >>> expected: str = "coding"
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        if rows == 1:
            return encoded_text

        n: int = len(encoded_text)
        cols: int = n // rows
        i, j, k = 0, 0, 0
        original_text: List[str] = []

        while k < n:
            original_text.append(encoded_text[k])
            i += 1
            if i == rows:
                i = 0
                j += 1
            k = i * (cols + 1) + j

        return "".join(original_text).rstrip()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
