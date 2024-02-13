# Submission title: Count the Number of Consistent Strings
# Submission url  : https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
# Submission url  : https://leetcode.com/submissions/detail/1056137764/
# Submission json : {"id":1056137764,"status_display":"Accepted","lang":"python3","question_id":1786,"title_slug":"count-the-number-of-consistent-strings","code":"class Solution:\n    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:\n        allowed = set(allowed)\n        count = 0\n        for word in words:\n            if all(char in allowed for char in word):\n                count += 1\n        return count","title":"Count the Number of Consistent Strings","url":"/submissions/detail/1056137764/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695371681,"status":10,"runtime":"239 ms","is_pending":"Not Pending","memory":"18.2 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            if all(char in allowed for char in word):
                count += 1
        return count
