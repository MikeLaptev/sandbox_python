from typing import List


class FindResultantArrayAfterRemovingAnagrams:
    """
    Leetcode #2273
    Link: https://leetcode.com/problems/find-resultant-array-after-removing-anagrams
    """

    def remove_anagrams(self, words: List[str]) -> List[str]:
        """
        >>> sut = FindResultantArrayAfterRemovingAnagrams()
        >>> assert ["abba","cd"] == sut.remove_anagrams(["abba","baba","bbaa","cd","cd"])
        >>> assert ["a","b","c","d","e"] == sut.remove_anagrams(["a","b","c","d","e"])
        """
        ret: List[str] = [words[0]]
        for i in range(len(words)):
            if self.__stats(ret[-1]) != self.__stats(words[i]):
                ret.append(words[i])
        return ret

    def __stats(self, word: str) -> List[int]:
        ret: List[int] = [0] * (ord("z") - ord("a") + 1)
        for c in word:
            ret[ord(c) - ord("a")] += 1
        return ret

    def remove_anagrams_opt(self, words: List[str]) -> List[str]:
        """
        >>> sut = FindResultantArrayAfterRemovingAnagrams()
        >>> assert ["abba","cd"] == sut.remove_anagrams_opt(["abba","baba","bbaa","cd","cd"])
        >>> assert ["a","b","c","d","e"] == sut.remove_anagrams_opt(["a","b","c","d","e"])
        """
        word: str = ""
        answer: List[str] = []

        for i in words:
            if sorted(word) != sorted(i):
                answer.append(i)
            word = i

        return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
