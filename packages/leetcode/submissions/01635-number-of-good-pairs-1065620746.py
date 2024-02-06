# Submission title: for Number of Good Pairs
# Submission url  : https://leetcode.com/submissions/detail/1065620746/
# Submission json : {"id": 1065620746, "status_display": "Accepted", "lang": "python3", "question_id": 1635, "title_slug": "number-of-good-pairs", "code": "class Solution:\n    def numIdenticalPairs(self, nums: List[int]) -> int:        \n        return sum((count ** 2 - count) // 2 for count in Counter(nums).values() if count > 1)", "title": "Number of Good Pairs", "url": "/submissions/detail/1065620746/", "lang_name": "Python3", "time": "4\u00a0months", "timestamp": 1696313620, "status": 10, "runtime": "43 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(
            (count**2 - count) // 2 for count in Counter(nums).values() if count > 1
        )
