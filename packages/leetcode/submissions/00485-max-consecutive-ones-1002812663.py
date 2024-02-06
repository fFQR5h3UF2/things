# Submission title: for Max Consecutive Ones
# Submission url  : https://leetcode.com/submissions/detail/1002812663/
# Submission json : {"id": 1002812663, "status_display": "Accepted", "lang": "python3", "question_id": 485, "title_slug": "max-consecutive-ones", "code": "class Solution:\n    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:\n        max_count, count = 0, 0\n        for number in nums:\n            if not number:\n                max_count = max(max_count, count)\n                count = 0\n                continue\n            \n            count += 1\n        \n        return max(max_count, count)", "title": "Max Consecutive Ones", "url": "/submissions/detail/1002812663/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690217579, "status": 10, "runtime": "330 ms", "is_pending": "Not Pending", "memory": "16.7 MB", "compare_result": "111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, count = 0, 0
        for number in nums:
            if not number:
                max_count = max(max_count, count)
                count = 0
                continue

            count += 1

        return max(max_count, count)
