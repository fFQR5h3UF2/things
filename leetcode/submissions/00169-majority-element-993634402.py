# Submission title: for Majority Element
# Submission url  : https://leetcode.com/submissions/detail/993634402/
# Submission json : {"id": 993634402, "status_display": "Accepted", "lang": "python3", "question_id": 169, "title_slug": "majority-element", "code": "class Solution:\n    def majorityElement(self, nums: List[int]) -> int:\n        return sorted(nums)[len(nums)//2]\n                ", "title": "Majority Element", "url": "/submissions/detail/993634402/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689266255, "status": 10, "runtime": "169 ms", "is_pending": "Not Pending", "memory": "17.9 MB", "compare_result": "111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
