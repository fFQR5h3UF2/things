# Submission title: Find the Difference
# Submission url  : https://leetcode.com/problems/find-the-difference/description/
# Submission url  : https://leetcode.com/submissions/detail/1002666484/
# Submission json : {"id":1002666484,"status_display":"Accepted","lang":"python3","question_id":389,"title_slug":"find-the-difference","code":"class Solution:\n    def findTheDifference(self, s: str, t: str) -> str:\n        letters = defaultdict(int)\n        for letter in s:\n            letters[letter] += 1\n\n        for letter in t:\n            if letters[letter] == 0:\n                return letter\n            \n            letters[letter] -= 1\n        \n        return None","title":"Find the Difference","url":"/submissions/detail/1002666484/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690206878,"status":10,"runtime":"51 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = defaultdict(int)
        for letter in s:
            letters[letter] += 1

        for letter in t:
            if letters[letter] == 0:
                return letter

            letters[letter] -= 1

        return None
