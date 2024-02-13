# Submission title: First Unique Character in a String
# Submission url  : https://leetcode.com/problems/first-unique-character-in-a-string/description/
# Submission url  : https://leetcode.com/submissions/detail/1166558069/
# Submission json : {"id":1166558069,"status_display":"Accepted","lang":"python3","question_id":387,"title_slug":"first-unique-character-in-a-string","code":"class Solution:\n    def firstUniqChar(self, s: str) -> int:\n        counter = [0] * 26\n\n        for char in s:\n            idx = ord(char) - ord('a')\n            if counter[idx] in (0, 1):\n                counter[idx] += 1\n        for i in range(len(s)):\n            if counter[ord(s[i]) - ord('a')] == 1:\n                return i\n        return -1","title":"First Unique Character in a String","url":"/submissions/detail/1166558069/","lang_name":"Python3","time":"2 hours, 29 minutes","timestamp":1707117177,"status":10,"runtime":"103 ms","is_pending":"Not Pending","memory":"16.7 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = [0] * 26

        for char in s:
            idx = ord(char) - ord("a")
            if counter[idx] in (0, 1):
                counter[idx] += 1
        for i in range(len(s)):
            if counter[ord(s[i]) - ord("a")] == 1:
                return i
        return -1
