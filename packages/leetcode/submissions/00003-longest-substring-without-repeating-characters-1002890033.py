# Submission title: for Longest Substring Without Repeating Characters
# Submission url  : https://leetcode.com/submissions/detail/1002890033/
# Submission json : {"id": 1002890033, "status_display": "Accepted", "lang": "python3", "question_id": 3, "title_slug": "longest-substring-without-repeating-characters", "code": "class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        length = len(s)\n        if length < 2:\n            return length\n        \n        max_length, left, charset = 1, 0, set([s[0]])\n        for right in range(1, length):\n            letter = s[right]\n            if letter not in charset:\n                charset.add(letter)\n                continue\n\n            this_length = right - left\n            if this_length > max_length:\n                max_length = this_length\n            \n            while letter in charset:\n                charset.remove(s[left])\n                left += 1\n            \n            charset.add(letter)\n\n        return max(max_length, length - left)", "title": "Longest Substring Without Repeating Characters", "url": "/submissions/detail/1002890033/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690222629, "status": 10, "runtime": "53 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length

        max_length, left, charset = 1, 0, set([s[0]])
        for right in range(1, length):
            letter = s[right]
            if letter not in charset:
                charset.add(letter)
                continue

            this_length = right - left
            if this_length > max_length:
                max_length = this_length

            while letter in charset:
                charset.remove(s[left])
                left += 1

            charset.add(letter)

        return max(max_length, length - left)
