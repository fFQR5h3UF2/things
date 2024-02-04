# Submission title: for Two Sum
# Submission url  : https://leetcode.com/submissions/detail/955691548/
# Submission json : {"id": 955691548, "status_display": "Accepted", "lang": "python3", "question_id": 1, "title_slug": "two-sum", "code": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        for i, number in enumerate(nums):\n            for j, number_inner in enumerate(nums[i+1:]):\n                if number + number_inner == target:\n                    return [i, i+j+1]", "title": "Two Sum", "url": "/submissions/detail/955691548/", "lang_name": "Python3", "time": "8\u00a0months, 2\u00a0weeks", "timestamp": 1684834243, "status": 10, "runtime": "3364 ms", "is_pending": "Not Pending", "memory": "17.1 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, number in enumerate(nums):
            for j, number_inner in enumerate(nums[i + 1 :]):
                if number + number_inner == target:
                    return [i, i + j + 1]
