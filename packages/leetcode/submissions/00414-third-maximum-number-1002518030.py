# Submission title: for Third Maximum Number
# Submission url  : https://leetcode.com/submissions/detail/1002518030/
# Submission json : {"id": 1002518030, "status_display": "Accepted", "lang": "python3", "question_id": 414, "title_slug": "third-maximum-number", "code": "class Solution:\n    def thirdMax(self, nums: List[int]) -> int:\n        nums.sort(reverse=True)\n        number_max = nums[0]\n        count = 1\n        for i in range(1, len(nums)):\n            number = nums[i]\n            if number == nums[i-1]:\n                continue\n            \n            count += 1\n\n            if count == 3:\n                return number \n        \n        return number_max", "title": "Third Maximum Number", "url": "/submissions/detail/1002518030/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690193069, "status": 10, "runtime": "69 ms", "is_pending": "Not Pending", "memory": "17.3 MB", "compare_result": "1111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        number_max = nums[0]
        count = 1
        for i in range(1, len(nums)):
            number = nums[i]
            if number == nums[i - 1]:
                continue

            count += 1

            if count == 3:
                return number

        return number_max
