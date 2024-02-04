# Submission for Longest String Chain
# Submission url: https://leetcode.com/submissions/detail/1056974394/


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        length = len(words)

        @cache
        def is_pred(pred: str, word: str) -> bool:
            length_pred, length_word = len(pred), len(word)
            if length_pred == length_word:
                return pred == word
            if length_word - length_pred != 1:
                return False

            for i in range(length_pred):
                if word[i] == pred[i]:
                    continue
                return word[i + 1 :] == pred[i:]
            return True

        cur_words = set()

        def backtrack(prev_word: str) -> int:
            chain_length = 0
            for word in words:
                if word in cur_words:
                    continue
                if prev_word is None or is_pred(prev_word, word):
                    cur_words.add(word)
                    chain_length = max(chain_length, 1 + backtrack(word))
                    cur_words.remove(word)
            return chain_length

        return backtrack(None)
