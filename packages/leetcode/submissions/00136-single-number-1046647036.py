# Submission title: for Single Number
# Submission url  : https://leetcode.com/submissions/detail/1046647036/
# Submission json : {"id": 1046647036, "status_display": "Accepted", "lang": "python3", "question_id": 136, "title_slug": "single-number", "code": "class Solution:\n    def singleNumber(self, nums: List[int]) -> int:\n        nums_count = len(nums)\n        if nums_count == 1:\n            return nums[0]\n        \n        nums.sort()\n        for i in range(0, nums_count, 2):\n            if i + 1 == nums_count:\n                return nums[i]\n\n            cur_num, next_num = nums[i], nums[i+1]\n            if cur_num == next_num:\n                continue\n            \n            return cur_num\n        \n        return 0", "title": "Single Number", "url": "/submissions/detail/1046647036/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694447748, "status": 10, "runtime": "131 ms", "is_pending": "Not Pending", "memory": "19.1 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_count = len(nums)
        if nums_count == 1:
            return nums[0]

        nums.sort()
        for i in range(0, nums_count, 2):
            if i + 1 == nums_count:
                return nums[i]

            cur_num, next_num = nums[i], nums[i + 1]
            if cur_num == next_num:
                continue

            return cur_num

        return 0
