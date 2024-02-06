# Submission title: for Peak Index in a Mountain Array
# Submission url  : https://leetcode.com/submissions/detail/1003583841/
# Submission json : {"id": 1003583841, "status_display": "Accepted", "lang": "python3", "question_id": 882, "title_slug": "peak-index-in-a-mountain-array", "code": "class Solution:\n    # [0,3,2,1,0]\n    def peakIndexInMountainArray(self, arr: List[int]) -> int:\n        length = len(arr)\n\n        left, right = 0, length - 1\n        while left <= right:\n            peak = left + (right - left) // 2\n            left_val, right_val = arr[peak-1], arr[peak+1]\n            peak_val = arr[peak]\n\n            if left_val < peak_val > right_val:\n                return peak\n            \n            if right_val > peak_val:\n                left = peak + 1\n            else:\n                right = peak - 1\n        \n        return left\n        ", "title": "Peak Index in a Mountain Array", "url": "/submissions/detail/1003583841/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690292305, "status": 10, "runtime": "603 ms", "is_pending": "Not Pending", "memory": "30.2 MB", "compare_result": "111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # [0,3,2,1,0]
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)

        left, right = 0, length - 1
        while left <= right:
            peak = left + (right - left) // 2
            left_val, right_val = arr[peak - 1], arr[peak + 1]
            peak_val = arr[peak]

            if left_val < peak_val > right_val:
                return peak

            if right_val > peak_val:
                left = peak + 1
            else:
                right = peak - 1

        return left
