# Submission title: Length of Last Word
# Submission url  : https://leetcode.com/problems/length-of-last-word/description/
# Submission url  : https://leetcode.com/submissions/detail/989425807/
# Submission json : {"id":989425807,"status_display":"Accepted","lang":"python3","question_id":58,"title_slug":"length-of-last-word","code":"class Solution:\n    # we need to iterate over the string searching for words\n    # add a whitespace to the end to avoid the situation when the last symbol is non-whitespace \n    # possible combinations:\n    # 1. a whitespace after a symbol: end of the word\n    # 2. a whitespace after a whitespace: ignore\n    # 3. a symbol after a symbol: ignore\n    def lengthOfLastWord(self, s: str) -> int:\n        s += \" \"\n        result, word_length = 0, 0\n\n        for i, symbol in enumerate(s):\n            if symbol != \" \":\n                word_length += 1\n                continue\n            \n            if word_length > 0:\n                result = word_length\n                word_length = 0\n        \n        return result","title":"Length of Last Word","url":"/submissions/detail/989425807/","lang_name":"Python3","time":"7 months","timestamp":1688831837,"status":10,"runtime":"50 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    # we need to iterate over the string searching for words
    # add a whitespace to the end to avoid the situation when the last symbol is non-whitespace
    # possible combinations:
    # 1. a whitespace after a symbol: end of the word
    # 2. a whitespace after a whitespace: ignore
    # 3. a symbol after a symbol: ignore
    def lengthOfLastWord(self, s: str) -> int:
        s += " "
        result, word_length = 0, 0

        for i, symbol in enumerate(s):
            if symbol != " ":
                word_length += 1
                continue

            if word_length > 0:
                result = word_length
                word_length = 0

        return result
