# Submission title: Valid Anagram
# Submission url  : https://leetcode.com/problems/valid-anagram/description/
# Submission url  : https://leetcode.com/submissions/detail/995272408/
# Submission json : {"id":995272408,"status_display":"Accepted","lang":"python3","question_id":242,"title_slug":"valid-anagram","code":"class Solution:\n    def isAnagram(self, s: str, t: str) -> bool:\n        s_length, t_length = len(s), len(t)\n\n        if s_length != t_length:\n            return False\n        \n        count = defaultdict(int)\n        for i, s_symbol in enumerate(s):\n            t_symbol = t[i]\n            count[s_symbol] += 1\n            count[t_symbol] -= 1\n\n        return not any((i != 0 for i in count.values())) ","title":"Valid Anagram","url":"/submissions/detail/995272408/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689445336,"status":10,"runtime":"63 ms","is_pending":"Not Pending","memory":"16.7 MB","compare_result":"1111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length, t_length = len(s), len(t)

        if s_length != t_length:
            return False

        count = defaultdict(int)
        for i, s_symbol in enumerate(s):
            t_symbol = t[i]
            count[s_symbol] += 1
            count[t_symbol] -= 1

        return not any((i != 0 for i in count.values()))
