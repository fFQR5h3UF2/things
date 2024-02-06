# Submission title: for Combination Sum
# Submission url  : https://leetcode.com/submissions/detail/1040286655/
# Submission json : {"id": 1040286655, "status_display": "Accepted", "lang": "python3", "question_id": 39, "title_slug": "combination-sum", "code": "class Solution:\n    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:\n        result = set()\n        cur_nums = []\n\n        def backtrack(cur_sum: int) -> None:\n            if cur_sum == target:\n                result.add(tuple(sorted(cur_nums[:])))\n            if cur_sum >= target:\n                return\n\n            for num in candidates:\n                cur_nums.append(num)\n                backtrack(num + cur_sum)\n                cur_nums.pop() \n\n        backtrack(0)\n\n        return result", "title": "Combination Sum", "url": "/submissions/detail/1040286655/", "lang_name": "Python3", "time": "5\u00a0months", "timestamp": 1693832085, "status": 10, "runtime": "593 ms", "is_pending": "Not Pending", "memory": "16.6 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        cur_nums = []

        def backtrack(cur_sum: int) -> None:
            if cur_sum == target:
                result.add(tuple(sorted(cur_nums[:])))
            if cur_sum >= target:
                return

            for num in candidates:
                cur_nums.append(num)
                backtrack(num + cur_sum)
                cur_nums.pop()

        backtrack(0)

        return result
