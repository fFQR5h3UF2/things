# Submission title: Combinations
# Submission url  : https://leetcode.com/problems/combinations/description/
# Submission url  : https://leetcode.com/submissions/detail/1057808867/
# Submission json : {"id":1057808867,"status_display":"Accepted","lang":"python3","question_id":77,"title_slug":"combinations","code":"class Solution:\n    def combine(self, n: int, k: int) -> List[List[int]]:\n        current = []\n        \n        def backtrack(first: int) -> Generator[None, None, List[int]]:\n            if len(current) == k:\n                yield tuple(current[:])\n                return\n\n            for i in range(first, n + 1):\n                current.append(i)\n                yield from backtrack(i + 1)\n                current.pop()\n            \n            return\n\n        return tuple(combination for combination in backtrack(1)) ","title":"Combinations","url":"/submissions/detail/1057808867/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695549356,"status":10,"runtime":"964 ms","is_pending":"Not Pending","memory":"61.7 MB","compare_result":"111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        current = []

        def backtrack(first: int) -> Generator[None, None, List[int]]:
            if len(current) == k:
                yield tuple(current[:])
                return

            for i in range(first, n + 1):
                current.append(i)
                yield from backtrack(i + 1)
                current.pop()

            return

        return tuple(combination for combination in backtrack(1))
