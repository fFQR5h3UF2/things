# Submission title: for Search a 2D Matrix
# Submission url  : https://leetcode.com/submissions/detail/997676878/
# Submission json : {"id": 997676878, "status_display": "Accepted", "lang": "python3", "question_id": 74, "title_slug": "search-a-2d-matrix", "code": "class Solution:\n    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:\n        length_vertical, length_horizontal = len(matrix), len(matrix[0])\n\n\n        left, right = 0, length_vertical - 1\n        while left <= right:\n            mid = left + (right - left) // 2\n            mid_number = matrix[mid][0]\n            \n            if mid_number == target:\n                return True\n            \n            if mid_number > target:\n                right = mid - 1\n            else:\n                left = mid + 1\n        \n        vertical_index = right\n        left, right = 0, length_horizontal - 1\n        while left <= right:\n            mid = left + (right - left) // 2\n            mid_number = matrix[vertical_index][mid]\n\n            if mid_number == target:\n                return True\n            \n            if mid_number > target:\n                right = mid - 1\n            else:\n                left = mid + 1\n            \n        return False", "title": "Search a 2D Matrix", "url": "/submissions/detail/997676878/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689693923, "status": 10, "runtime": "67 ms", "is_pending": "Not Pending", "memory": "16.8 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length_vertical, length_horizontal = len(matrix), len(matrix[0])

        left, right = 0, length_vertical - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_number = matrix[mid][0]

            if mid_number == target:
                return True

            if mid_number > target:
                right = mid - 1
            else:
                left = mid + 1

        vertical_index = right
        left, right = 0, length_horizontal - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_number = matrix[vertical_index][mid]

            if mid_number == target:
                return True

            if mid_number > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
