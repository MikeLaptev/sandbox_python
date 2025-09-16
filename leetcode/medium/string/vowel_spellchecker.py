from typing import List, Dict, Tuple, Set


class VowelSpellchecker:
    """
    Leetcode #966
    Link: https://leetcode.com/problems/vowel-spellchecker
    """

    __VOWELS = {"a", "e", "i", "o", "u"}

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        >>> sut = VowelSpellchecker()
        >>> # example one
        >>> wordlist = ["KiTe","kite","hare","Hare"]
        >>> queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
        >>> expected = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
        >>> actual = sut.spellchecker(wordlist, queries)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        >>> # example two
        >>> wordlist = ["yellow", "Yellow"]
        >>> queries = ["YellOw", "Yellow", "yellow", "yeellow", "yllw"]
        >>> expected = ["yellow", "Yellow", "yellow", "", ""]
        >>> actual = sut.spellchecker(wordlist, queries)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        """
        exact: Set[str] = {*wordlist}
        lower_2_exact: Dict[str, List[str]]
        pattern_2_exact: Dict[str, List[str]]
        lower_2_exact, pattern_2_exact = self._preprocess_words(wordlist)

        results = []

        for q in queries:
            if q in exact:
                results.append(q)
                continue

            t = q.lower()
            if t in lower_2_exact:
                results.append(lower_2_exact[t][0])
                continue

            t = self._devowel(q)
            if t in pattern_2_exact:
                results.append(pattern_2_exact[t][0])
                continue

            results.append("")

        return results

    def _preprocess_words(
        self, wordlist: List[str]
    ) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
        lower_2_exact = {}
        pattern_2_exact = {}

        for w in wordlist:
            l = w.lower()
            if l not in lower_2_exact:
                lower_2_exact[l] = []
            lower_2_exact[l].append(w)

            d = self._devowel(w)
            if d not in pattern_2_exact:
                pattern_2_exact[d] = []
            pattern_2_exact[self._devowel(w)].append(w)

        return lower_2_exact, pattern_2_exact

    def _devowel(self, w: str) -> str:
        """
        >>> sut = VowelSpellchecker()
        >>> actual = sut._devowel('yollow')
        >>> assert 'y*ll*w' == actual, f'yollow; got {actual}'
        >>> assert 'y**ll*w' == sut._devowel('yeellow'), 'yeellow'
        >>> assert 'yllw' == sut._devowel('yllw'), 'yllw'
        """
        return "".join(
            c if c not in VowelSpellchecker.__VOWELS else "*" for c in w.lower()
        )

    def spellchecker_opt(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        An optimized version

        >>> sut = VowelSpellchecker()
        >>> # example one
        >>> wordlist = ["KiTe","kite","hare","Hare"]
        >>> queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
        >>> expected = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
        >>> actual = sut.spellchecker_opt(wordlist, queries)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        >>> # example two
        >>> wordlist = ["yellow", "Yellow"]
        >>> queries = ["YellOw", "Yellow", "yellow", "yeellow", "yllw"]
        >>> expected = ["yellow", "Yellow", "yellow", "", ""]
        >>> actual = sut.spellchecker_opt(wordlist, queries)
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        """

        def case_hash(s):
            return s.lower()

        def vowel_hash(s):
            return (
                s.replace("e", "a")
                .replace("i", "a")
                .replace("o", "a")
                .replace("u", "a")
            )

        exact = {*wordlist}
        case = {}
        vowl = {}

        for w in wordlist:
            c = case_hash(w)
            if c not in case:
                case[c] = w

            v = vowel_hash(c)
            if v not in vowl:
                vowl[v] = w

        def correct(w):
            if w in exact:
                return w

            c = case_hash(w)
            if c in case:
                return case[c]

            v = vowel_hash(c)
            if v in vowl:
                return vowl[v]

            return ""

        return [correct(q) for q in queries]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
