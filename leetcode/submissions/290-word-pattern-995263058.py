# Submission for Word Pattern
# Submission url: https://leetcode.com/submissions/detail/995263058/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        words_length, pattern_length = len(words), len(pattern)

        if words_length != pattern_length:
            return Falser

        symbol_to_word = {}
        word_to_symbol = {}

        for i, symbol in enumerate(pattern):
            word = words[i]
            symbol_in, word_in = symbol in symbol_to_word, word in word_to_symbol

            if symbol_in and word_in:
                continue

            if not symbol_in and not word_in:
                symbol_to_word[symbol] = word
                word_to_symbol[word] = symbol
                continue

            return False

        return True
