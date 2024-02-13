# Submission title: Minimum ASCII Delete Sum for Two Strings
# Submission url  : https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
# Submission url  : https://leetcode.com/submissions/detail/1008445470/
# Submission json : {"id":1008445470,"status_display":"Accepted","lang":"python3","question_id":712,"title_slug":"minimum-ascii-delete-sum-for-two-strings","code":"class Solution:\n    def minimumDeleteSum(self, s1: str, s2: str) -> int:\n        length_1, length_2 = len(s1), len(s2)\n\n        @cache\n        def calculate(i: int, j: int) -> int:    \n            if i >= length_1 and j >= length_2:\n                return 0\n            \n            if i >= length_1:\n                return sum(ord(char) for char in s2[j:])\n            \n            if j >= length_2:\n                return sum(ord(char) for char in s1[i:])\n            \n            if s1[i] == s2[j]:\n                return calculate(i + 1, j + 1)\n            \n            return min(\n                ord(s1[i]) + calculate(i + 1, j),\n                ord(s2[j]) + calculate(i, j + 1)\n            )\n\n        return calculate(0, 0)","title":"Minimum ASCII Delete Sum for Two Strings","url":"/submissions/detail/1008445470/","lang_name":"Python3","time":"6 months, 1 week","timestamp":1690803999,"status":10,"runtime":"862 ms","is_pending":"Not Pending","memory":"221.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        length_1, length_2 = len(s1), len(s2)

        @cache
        def calculate(i: int, j: int) -> int:
            if i >= length_1 and j >= length_2:
                return 0

            if i >= length_1:
                return sum(ord(char) for char in s2[j:])

            if j >= length_2:
                return sum(ord(char) for char in s1[i:])

            if s1[i] == s2[j]:
                return calculate(i + 1, j + 1)

            return min(
                ord(s1[i]) + calculate(i + 1, j), ord(s2[j]) + calculate(i, j + 1)
            )

        return calculate(0, 0)
