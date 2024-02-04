# Submission title: for House Robber
# Submission url  : https://leetcode.com/submissions/detail/1152842944/
# Submission json : {"id": 1152842944, "status_display": "Accepted", "lang": "python3", "question_id": 198, "title_slug": "house-robber", "code": "class Solution:\n    def rob(self, nums: List[int]) -> int:\n        length = len(nums)\n        cache = {}\n\n        def dp(i: int) -> int:\n            if i >= length:\n                return 0\n            val = nums[i]\n            if i in cache:\n                return cache[i]\n            res = max(dp(i + 1), val + dp(i + 2))\n            cache[i] = res\n            return res \n\n        return dp(0)", "title": "House Robber", "url": "/submissions/detail/1152842944/", "lang_name": "Python3", "time": "1\u00a0week, 6\u00a0days", "timestamp": 1705860741, "status": 10, "runtime": "41 ms", "is_pending": "Not Pending", "memory": "16.5 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        cache = {}

        def dp(i: int) -> int:
            if i >= length:
                return 0
            val = nums[i]
            if i in cache:
                return cache[i]
            res = max(dp(i + 1), val + dp(i + 2))
            cache[i] = res
            return res

        return dp(0)
