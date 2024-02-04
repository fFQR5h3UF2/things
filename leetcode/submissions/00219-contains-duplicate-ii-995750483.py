# Submission title: for Contains Duplicate II
# Submission url  : https://leetcode.com/submissions/detail/995750483/
# Submission json : {"id": 995750483, "status_display": "Accepted", "lang": "python3", "question_id": 219, "title_slug": "contains-duplicate-ii", "code": "class Solution:\n    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:\n        indexes = defaultdict(set)\n        for i, number in enumerate(nums):\n            if number in indexes and any(abs(i - j) <= k for j in indexes[number]):\n                return True\n            indexes[number].add(i)\n        return False\n\n            ", "title": "Contains Duplicate II", "url": "/submissions/detail/995750483/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689498969, "status": 10, "runtime": "682 ms", "is_pending": "Not Pending", "memory": "46.5 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = defaultdict(set)
        for i, number in enumerate(nums):
            if number in indexes and any(abs(i - j) <= k for j in indexes[number]):
                return True
            indexes[number].add(i)
        return False
