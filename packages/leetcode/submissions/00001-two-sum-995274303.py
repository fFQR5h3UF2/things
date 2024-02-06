# Submission title: for Two Sum
# Submission url  : https://leetcode.com/submissions/detail/995274303/
# Submission json : {"id": 995274303, "status_display": "Accepted", "lang": "python3", "question_id": 1, "title_slug": "two-sum", "code": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        indexes = {}\n        for i, number in enumerate(nums):\n            diff = target - number\n            if diff in indexes: \n                return [indexes[diff], i]\n            indexes[number] = i", "title": "Two Sum", "url": "/submissions/detail/995274303/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689445487, "status": 10, "runtime": "67 ms", "is_pending": "Not Pending", "memory": "17.6 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i, number in enumerate(nums):
            diff = target - number
            if diff in indexes:
                return [indexes[diff], i]
            indexes[number] = i
