# Submission title: First Unique Character in a String
# Submission url  : https://leetcode.com/problems/first-unique-character-in-a-string/description/
# Submission url  : https://leetcode.com/submissions/detail/1002662613/
# Submission json : {"id":1002662613,"status_display":"Accepted","lang":"python3","question_id":387,"title_slug":"first-unique-character-in-a-string","code":"class Solution:\n    def firstUniqChar(self, s: str) -> int:\n        counts = {}\n        repeated_index = len(s)\n        for i, letter in enumerate(s):\n            if letter in counts:\n                counts[letter] = repeated_index\n                continue\n            \n            counts[letter] = i\n        \n        result = repeated_index\n\n        for letter, index in counts.items():\n            if index == repeated_index:\n                continue\n            \n            if index < result:\n                result = index\n\n        return result if result != repeated_index else -1","title":"First Unique Character in a String","url":"/submissions/detail/1002662613/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690206578,"status":10,"runtime":"107 ms","is_pending":"Not Pending","memory":"16.6 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        repeated_index = len(s)
        for i, letter in enumerate(s):
            if letter in counts:
                counts[letter] = repeated_index
                continue

            counts[letter] = i

        result = repeated_index

        for letter, index in counts.items():
            if index == repeated_index:
                continue

            if index < result:
                result = index

        return result if result != repeated_index else -1
