# Submission title: for Spiral Matrix
# Submission url  : https://leetcode.com/submissions/detail/1028017265/
# Submission json : {"id": 1028017265, "status_display": "Accepted", "lang": "python3", "question_id": 54, "title_slug": "spiral-matrix", "code": "class Solution:\n    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:\n        row_count, col_count = len(matrix), len(matrix[0])\n        if row_count == 1:\n            return matrix[0]\n        if col_count == 1:\n            return [row[0] for row in matrix]\n\n\n        result = []\n        top, bot, left, right = 0, row_count - 1, 0, col_count - 1\n        capacity = row_count * col_count\n\n        while len(result) < capacity:\n            for col in range(left, right + 1):\n                result.append(matrix[top][col])\n            top += 1\n\n            for row in range(top, bot + 1):\n                result.append(matrix[row][right])\n            right -= 1\n\n            if top <= bot:\n                for col in range(right, left - 1, -1):\n                    result.append(matrix[bot][col])\n                bot -= 1\n            \n            if left <= right:\n                for row in range(bot, top - 1, -1):\n                    result.append(matrix[row][left])\n                left += 1\n\n        return result", "title": "Spiral Matrix", "url": "/submissions/detail/1028017265/", "lang_name": "Python3", "time": "5\u00a0months, 2\u00a0weeks", "timestamp": 1692650326, "status": 10, "runtime": "37 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_count, col_count = len(matrix), len(matrix[0])
        if row_count == 1:
            return matrix[0]
        if col_count == 1:
            return [row[0] for row in matrix]

        result = []
        top, bot, left, right = 0, row_count - 1, 0, col_count - 1
        capacity = row_count * col_count

        while len(result) < capacity:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            for row in range(top, bot + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bot:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bot][col])
                bot -= 1

            if left <= right:
                for row in range(bot, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
