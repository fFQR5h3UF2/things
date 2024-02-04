# Submission title: for Find Minimum in Rotated Sorted Array
# Submission url  : https://leetcode.com/submissions/detail/1058493656/
# Submission json : {"id": 1058493656, "status_display": "Accepted", "lang": "python3", "question_id": 153, "title_slug": "find-minimum-in-rotated-sorted-array", "code": "class Solution:\n    def findMin(self, nums: List[int]) -> int:\n        length = len(nums)\n        if length == 1:\n            return nums[0]\n        first, last = nums[0], nums[-1]\n        if first < last:\n            return first\n        left, right = 0, length - 1\n        while left <= right:\n            mid = left + (right - left) // 2\n            left_num = nums[mid - 1] if mid > 0 else first\n            mid_num = nums[mid] \n            right_num = nums[mid + 1] if mid + 1 < length else last\n            if left_num > mid_num <= right_num:\n                return mid_num\n            if left_num > mid_num or (left_num <= mid_num and mid_num >= first):\n                left = mid + 1\n            else:\n                right = mid\n        return nums[left]\n\n", "title": "Find Minimum in Rotated Sorted Array", "url": "/submissions/detail/1058493656/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695622619, "status": 10, "runtime": "51 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        first, last = nums[0], nums[-1]
        if first < last:
            return first
        left, right = 0, length - 1
        while left <= right:
            mid = left + (right - left) // 2
            left_num = nums[mid - 1] if mid > 0 else first
            mid_num = nums[mid]
            right_num = nums[mid + 1] if mid + 1 < length else last
            if left_num > mid_num <= right_num:
                return mid_num
            if left_num > mid_num or (left_num <= mid_num and mid_num >= first):
                left = mid + 1
            else:
                right = mid
        return nums[left]
