# Submission title: for Peak Index in a Mountain Array
# Submission url  : https://leetcode.com/submissions/detail/1003589521/
# Submission json : {"id": 1003589521, "status_display": "Accepted", "lang": "python3", "question_id": 882, "title_slug": "peak-index-in-a-mountain-array", "code": "class Solution:\n    # [0,3,2,1,0]\n    def peakIndexInMountainArray(self, arr: List[int]) -> int:\n        length = len(arr)\n\n        left, right = 0, length - 1\n        while left < right:\n            mid = left + (right - left) // 2\n\n            if arr[mid] < arr[mid + 1]:\n                left = mid + 1\n            else:\n                right = mid\n\n        return left\n        ", "title": "Peak Index in a Mountain Array", "url": "/submissions/detail/1003589521/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690292740, "status": 10, "runtime": "602 ms", "is_pending": "Not Pending", "memory": "30.2 MB", "compare_result": "111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # [0,3,2,1,0]
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)

        left, right = 0, length - 1
        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
