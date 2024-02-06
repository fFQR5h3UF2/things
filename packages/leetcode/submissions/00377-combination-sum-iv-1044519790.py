# Submission title: for Combination Sum IV
# Submission url  : https://leetcode.com/submissions/detail/1044519790/
# Submission json : {"id": 1044519790, "status_display": "Accepted", "lang": "python3", "question_id": 377, "title_slug": "combination-sum-iv", "code": "class Solution:\n    def combinationSum4(self, nums: List[int], target: int) -> int:\n\n        @cache\n        def dp(cur_sum: int) -> int:\n            if cur_sum == target:\n                return 1\n            if cur_sum > target:\n                return 0\n            \n            return sum(dp(cur_sum + num) for num in nums)\n\n        return dp(0)\n            ", "title": "Combination Sum IV", "url": "/submissions/detail/1044519790/", "lang_name": "Python3", "time": "4\u00a0months, 4\u00a0weeks", "timestamp": 1694244057, "status": 10, "runtime": "44 ms", "is_pending": "Not Pending", "memory": "16.9 MB", "compare_result": "111111111111111", "has_notes": true, "flag_type": 1}


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dp(cur_sum: int) -> int:
            if cur_sum == target:
                return 1
            if cur_sum > target:
                return 0

            return sum(dp(cur_sum + num) for num in nums)

        return dp(0)
