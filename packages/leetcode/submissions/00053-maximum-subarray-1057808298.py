# Submission title: for Maximum Subarray
# Submission url  : https://leetcode.com/submissions/detail/1057808298/
# Submission json : {"id": 1057808298, "status_display": "Accepted", "lang": "python3", "question_id": 53, "title_slug": "maximum-subarray", "code": "class Solution:\n    def maxSubArray(self, nums: List[int]) -> int:\n        length = len(nums)\n        if length == 0:\n            return 0\n        if length == 1:\n            return nums[0]\n        max_cur, max_overall = 0, float(\"-inf\")\n        for num in nums:\n            max_cur += num\n            if max_cur > max_overall:\n                max_overall = max_cur\n            if max_cur < 0:\n                max_cur = 0\n        return max_overall\n        ", "title": "Maximum Subarray", "url": "/submissions/detail/1057808298/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695549290, "status": 10, "runtime": "551 ms", "is_pending": "Not Pending", "memory": "30.5 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        max_cur, max_overall = 0, float("-inf")
        for num in nums:
            max_cur += num
            if max_cur > max_overall:
                max_overall = max_cur
            if max_cur < 0:
                max_cur = 0
        return max_overall
