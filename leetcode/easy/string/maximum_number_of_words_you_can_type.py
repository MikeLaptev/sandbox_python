class MaximumNumberOfWordsYouCanType:
    """
    Leetcode #1935
    Link: https://leetcode.com/problems/maximum-number-of-words-you-can-type
    """

    def can_be_typed_words(self, text: str, broken_letters: str) -> int:
        letters = {*broken_letters}
        return len(list(filter(lambda w: (not {*w} & letters), text.split())))
