# Submission title: for Is Subsequence
# Submission url  : https://leetcode.com/submissions/detail/993708456/
# Submission json : {"id": 993708456, "status_display": "Accepted", "lang": "python3", "question_id": 392, "title_slug": "is-subsequence", "code": "class Solution:\n    # create two pointers, original and sub, both are zero\n    # while either of those pointers have not reached the end:\n    # - if original symbol is equal to the sub, move both pointer to the right\n    # - if not, move original pointer to the right\n    # if sub pointer reached the end, return True, otherwise False\n    def isSubsequence(self, s: str, t: str) -> bool:\n        original, sub = 0, 0\n        original_length, sub_length = len(t), len(s)\n\n        while original < original_length and sub < sub_length:\n            if s[sub] == t[original]:\n                original += 1\n                sub += 1\n                continue\n            \n            original += 1\n\n        return sub == sub_length", "title": "Is Subsequence", "url": "/submissions/detail/993708456/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689271893, "status": 10, "runtime": "47 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # create two pointers, original and sub, both are zero
    # while either of those pointers have not reached the end:
    # - if original symbol is equal to the sub, move both pointer to the right
    # - if not, move original pointer to the right
    # if sub pointer reached the end, return True, otherwise False
    def isSubsequence(self, s: str, t: str) -> bool:
        original, sub = 0, 0
        original_length, sub_length = len(t), len(s)

        while original < original_length and sub < sub_length:
            if s[sub] == t[original]:
                original += 1
                sub += 1
                continue

            original += 1

        return sub == sub_length
