# Submission title: for Monotonic Array
# Submission url  : https://leetcode.com/submissions/detail/1061998725/
# Submission json : {"id": 1061998725, "status_display": "Accepted", "lang": "python3", "question_id": 932, "title_slug": "monotonic-array", "code": "class Solution:\n    def isMonotonic(self, nums: List[int]) -> bool:\n        length = len(nums)\n        if length < 3:\n            return True\n        is_increasing = None\n        for i in range(1, length):\n            cur, prev = nums[i], nums[i-1]\n            if cur == prev:\n                continue\n            is_increasing_cur = cur > prev\n            if is_increasing is None:\n                is_increasing = is_increasing_cur\n                continue\n            if is_increasing and not is_increasing_cur or (\n                not is_increasing and is_increasing_cur\n            ):\n                return False\n        return True", "title": "Monotonic Array", "url": "/submissions/detail/1061998725/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695965769, "status": 10, "runtime": "836 ms", "is_pending": "Not Pending", "memory": "30.6 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 3:
            return True
        is_increasing = None
        for i in range(1, length):
            cur, prev = nums[i], nums[i - 1]
            if cur == prev:
                continue
            is_increasing_cur = cur > prev
            if is_increasing is None:
                is_increasing = is_increasing_cur
                continue
            if (
                is_increasing
                and not is_increasing_cur
                or (not is_increasing and is_increasing_cur)
            ):
                return False
        return True
