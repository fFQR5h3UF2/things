# Submission title: for Search Insert Position
# Submission url  : https://leetcode.com/submissions/detail/997668741/
# Submission json : {"id": 997668741, "status_display": "Accepted", "lang": "python3", "question_id": 35, "title_slug": "search-insert-position", "code": "class Solution:\n    def searchInsert(self, nums: List[int], target: int) -> int:\n        length = len(nums)\n        left, right = 0, length - 1\n\n        while left <= right:\n            mid = left + (right - left) // 2\n            mid_number = nums[mid]\n\n            if mid_number == target:\n                return mid\n\n            if mid_number > target:\n                right = mid - 1\n            else:\n                left = mid + 1\n\n        return left", "title": "Search Insert Position", "url": "/submissions/detail/997668741/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689693287, "status": 10, "runtime": "67 ms", "is_pending": "Not Pending", "memory": "17 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left, right = 0, length - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_number = nums[mid]

            if mid_number == target:
                return mid

            if mid_number > target:
                right = mid - 1
            else:
                left = mid + 1

        return left
