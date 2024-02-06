# Submission title: for Search in Rotated Sorted Array
# Submission url  : https://leetcode.com/submissions/detail/1015557330/
# Submission json : {"id": 1015557330, "status_display": "Accepted", "lang": "python3", "question_id": 33, "title_slug": "search-in-rotated-sorted-array", "code": "class Solution:\n    def search(self, nums: List[int], target: int) -> int:\n        nums_count = len(nums)\n        left, right = 0, len(nums) - 1\n\n        first_num, last_num = nums[0], nums[-1]\n        if first_num == target:\n            return 0\n        if last_num == target:\n            return nums_count - 1\n        \n        # Find the index of the pivot element (the smallest element)\n        while left <= right:\n            mid = left + (right - left) // 2\n            if nums[mid] > last_num:\n                left = mid + 1\n            else:\n                right = mid - 1\n        \n        pivot_num = nums[left]\n        if pivot_num == target:\n            return left\n        \n        if pivot_num < target < last_num:\n            right = nums_count - 1\n        else:\n            left = 0\n        \n        while left <= right:\n            mid = left + (right - left) // 2\n            mid_num = nums[mid]\n            if mid_num == target:\n                return mid\n            elif mid_num > target:\n                right = mid - 1\n            else:\n                left = mid + 1\n        \n        return -1", "title": "Search in Rotated Sorted Array", "url": "/submissions/detail/1015557330/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1691492140, "status": 10, "runtime": "47 ms", "is_pending": "Not Pending", "memory": "16.6 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_count = len(nums)
        left, right = 0, len(nums) - 1

        first_num, last_num = nums[0], nums[-1]
        if first_num == target:
            return 0
        if last_num == target:
            return nums_count - 1

        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > last_num:
                left = mid + 1
            else:
                right = mid - 1

        pivot_num = nums[left]
        if pivot_num == target:
            return left

        if pivot_num < target < last_num:
            right = nums_count - 1
        else:
            left = 0

        while left <= right:
            mid = left + (right - left) // 2
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            elif mid_num > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
