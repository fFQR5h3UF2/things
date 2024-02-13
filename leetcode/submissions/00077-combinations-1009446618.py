# Submission title: Combinations
# Submission url  : https://leetcode.com/problems/combinations/description/
# Submission url  : https://leetcode.com/submissions/detail/1009446618/
# Submission json : {"id":1009446618,"status_display":"Accepted","lang":"python3","question_id":77,"title_slug":"combinations","code":"class Solution:\n    def combine(self, n: int, k: int) -> List[List[int]]:\n        current, result = [], []\n        \n        def backtrack(first: int) -> None:\n            if len(current) == k:\n                result.append(tuple(current[:]))\n                return\n\n            for i in range(first, n + 1):\n                current.append(i)\n                backtrack(i + 1)\n                current.pop()\n            \n            return\n\n        backtrack(1)\n\n        return result ","title":"Combinations","url":"/submissions/detail/1009446618/","lang_name":"Python3","time":"6 months, 1 week","timestamp":1690900402,"status":10,"runtime":"281 ms","is_pending":"Not Pending","memory":"18.3 MB","compare_result":"111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        current, result = [], []

        def backtrack(first: int) -> None:
            if len(current) == k:
                result.append(tuple(current[:]))
                return

            for i in range(first, n + 1):
                current.append(i)
                backtrack(i + 1)
                current.pop()

            return

        backtrack(1)

        return result
