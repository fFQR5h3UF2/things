# Submission title: for Minimum Size Subarray Sum
# Submission url  : https://leetcode.com/submissions/detail/1010087351/
# Submission json : {"id": 1010087351, "status_display": "Accepted", "lang": "python3", "question_id": 209, "title_slug": "minimum-size-subarray-sum", "code": "class Solution:\n    def minSubArrayLen(self, target: int, nums: List[int]) -> int:\n        left = 0\n        sum_of_subarray = 0\n        min_length = float('inf')\n        \n        for right in range(len(nums)):\n            sum_of_subarray += nums[right]\n            \n            while sum_of_subarray >= target:\n                min_length = min(min_length, right - left + 1)\n                sum_of_subarray -= nums[left]\n                left += 1\n\n        if min_length == float('inf'):\n            return 0\n\n        return min_length", "title": "Minimum Size Subarray Sum", "url": "/submissions/detail/1010087351/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1690963763, "status": 10, "runtime": "229 ms", "is_pending": "Not Pending", "memory": "29.6 MB", "compare_result": "111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_of_subarray = 0
        min_length = float("inf")

        for right in range(len(nums)):
            sum_of_subarray += nums[right]

            while sum_of_subarray >= target:
                min_length = min(min_length, right - left + 1)
                sum_of_subarray -= nums[left]
                left += 1

        if min_length == float("inf"):
            return 0

        return min_length
