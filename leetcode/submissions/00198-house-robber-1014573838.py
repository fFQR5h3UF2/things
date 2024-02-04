# Submission title: for House Robber
# Submission url  : https://leetcode.com/submissions/detail/1014573838/
# Submission json : {"id": 1014573838, "status_display": "Accepted", "lang": "python3", "question_id": 198, "title_slug": "house-robber", "code": "class Solution:\n    def rob(self, nums: List[int]) -> int:\n        house_count = len(nums)\n\n        dp = [0 for _ in range(house_count + 1)]\n        dp[1] = nums[0]\n\n        for house in range(1, house_count):\n            dp[house+1] = max(dp[house-1] + nums[house], dp[house])\n\n        return dp[-1]\n", "title": "House Robber", "url": "/submissions/detail/1014573838/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1691402840, "status": 10, "runtime": "43 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def rob(self, nums: List[int]) -> int:
        house_count = len(nums)

        dp = [0 for _ in range(house_count + 1)]
        dp[1] = nums[0]

        for house in range(1, house_count):
            dp[house + 1] = max(dp[house - 1] + nums[house], dp[house])

        return dp[-1]
