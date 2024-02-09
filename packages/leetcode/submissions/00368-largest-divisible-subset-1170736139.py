# Submission title: for Largest Divisible Subset
# Submission url  : https://leetcode.com/submissions/detail/1170736139/
# Submission json : {"id": 1170736139, "status_display": "Accepted", "lang": "python3", "question_id": 368, "title_slug": "largest-divisible-subset", "code": "class Solution:\n    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:\n        nums.sort()\n        n = len(nums)\n        dp = [1] * n\n        max_size, max_index = 1, 0\n\n        for i in range(1, n):\n            for j in range(i):\n                if nums[i] % nums[j] == 0:\n                    dp[i] = max(dp[i], dp[j] + 1)\n                    if dp[i] > max_size:\n                        max_size = dp[i]\n                        max_index = i\n\n        result = []\n        num = nums[max_index]\n        for i in range(max_index, -1, -1):\n            if num % nums[i] == 0 and dp[i] == max_size:\n                result.append(nums[i])\n                num = nums[i]\n                max_size -= 1\n\n        return result\n\n\n", "title": "Largest Divisible Subset", "url": "/submissions/detail/1170736139/", "lang_name": "Python3", "time": "1\u00a0hour, 32\u00a0minutes", "timestamp": 1707495152, "status": 10, "runtime": "220 ms", "is_pending": "Not Pending", "memory": "16.9 MB", "compare_result": "1111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_size, max_index = 1, 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        result = []
        num = nums[max_index]
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                result.append(nums[i])
                num = nums[i]
                max_size -= 1

        return result
