# Submission title: for Intersection of Two Arrays
# Submission url  : https://leetcode.com/submissions/detail/1002668315/
# Submission json : {"id": 1002668315, "status_display": "Accepted", "lang": "python3", "question_id": 349, "title_slug": "intersection-of-two-arrays", "code": "class Solution:\n    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:\n        return set(nums1).intersection(nums2)", "title": "Intersection of Two Arrays", "url": "/submissions/detail/1002668315/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690207015, "status": 10, "runtime": "60 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(nums2)