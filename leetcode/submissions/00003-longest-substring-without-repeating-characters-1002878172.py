# Submission title: Longest Substring Without Repeating Characters
# Submission url  : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Submission url  : https://leetcode.com/submissions/detail/1002878172/
# Submission json : {"id":1002878172,"status_display":"Accepted","lang":"python3","question_id":3,"title_slug":"longest-substring-without-repeating-characters","code":"class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        length = len(s)\n        if length < 2:\n            return length\n        \n        max_length = 0\n        start = 0\n        indexes = {s[0]: 0}\n        for end in range(1, length):\n            letter = s[end]\n            if letter not in indexes:\n                indexes[letter] = end\n                continue\n\n            this_length = end - start\n            if this_length > max_length:\n                max_length = this_length\n            \n            letter_index = indexes[letter]\n            \n            for remove_letter in s[start:letter_index]:\n                indexes.pop(remove_letter)\n\n            indexes[letter], start = end, letter_index + 1\n\n        return max(max_length, length - start)","title":"Longest Substring Without Repeating Characters","url":"/submissions/detail/1002878172/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690221857,"status":10,"runtime":"76 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length

        max_length = 0
        start = 0
        indexes = {s[0]: 0}
        for end in range(1, length):
            letter = s[end]
            if letter not in indexes:
                indexes[letter] = end
                continue

            this_length = end - start
            if this_length > max_length:
                max_length = this_length

            letter_index = indexes[letter]

            for remove_letter in s[start:letter_index]:
                indexes.pop(remove_letter)

            indexes[letter], start = end, letter_index + 1

        return max(max_length, length - start)
