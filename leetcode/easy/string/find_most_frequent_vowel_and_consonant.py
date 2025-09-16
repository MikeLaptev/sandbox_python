from collections import Counter


class FindMostFrequentVowelAndConsonant:
    """
    Leetcode #3541
    Link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant
    """

    def max_freq_sum(self, s: str) -> int:
        """
        >>> sut = FindMostFrequentVowelAndConsonant()
        >>> actual = sut.max_freq_sum("successes")
        >>> assert 6 == actual, f"successes; got: {actual}"
        >>> actual = sut.max_freq_sum("aeiaeia")
        >>> assert 3 == actual, f"aeiaeia; got: {actual}"
        """
        vowels = {"a", "e", "i", "o", "u"}
        v = Counter(filter(lambda t: t in vowels, s)).most_common(1)
        c = Counter(filter(lambda t: t not in vowels, s)).most_common(1)

        return (v[0][1] if v else 0) + (c[0][1] if c else 0)

    def max_freq_sum_dict(self, s: str) -> int:
        """
        >>> sut = FindMostFrequentVowelAndConsonant()
        >>> actual = sut.max_freq_sum_dict("successes")
        >>> assert 6 == actual, f"successes; got: {actual}"
        >>> actual = sut.max_freq_sum_dict("aeiaeia")
        >>> assert 3 == actual, f"aeiaeia; got: {actual}"
        """
        freq_map = {}
        for c in s:
            freq_map[c] = (freq_map[c] + 1) if c in freq_map else 1

        vowel_max = 0
        consonant_max = 0
        vowels = {"a", "e", "i", "o", "u"}
        for key, value in freq_map.items():
            if key in vowels:
                if value > vowel_max:
                    vowel_max = value
            else:
                if value > consonant_max:
                    consonant_max = value

        return vowel_max + consonant_max


if __name__ == "__main__":
    import doctest

    doctest.testmod()
