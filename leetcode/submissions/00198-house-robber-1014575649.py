# Submission title: for House Robber
# Submission url  : https://leetcode.com/submissions/detail/1014575649/
# Submission json : {"id": 1014575649, "status_display": "Accepted", "lang": "python3", "question_id": 198, "title_slug": "house-robber", "code": "class Solution:\n    def rob(self, nums: List[int]) -> int:\n        house_count = len(nums)\n\n        prev_1, prev_2 = 0, 0\n\n        for house in range(0, house_count):\n            prev_1, prev_2 = max(prev_2 + nums[house], prev_1), prev_1\n\n        return prev_1\n", "title": "House Robber", "url": "/submissions/detail/1014575649/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1691403004, "status": 10, "runtime": "36 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def rob(self, nums: List[int]) -> int:
        house_count = len(nums)

        prev_1, prev_2 = 0, 0

        for house in range(0, house_count):
            prev_1, prev_2 = max(prev_2 + nums[house], prev_1), prev_1

        return prev_1
