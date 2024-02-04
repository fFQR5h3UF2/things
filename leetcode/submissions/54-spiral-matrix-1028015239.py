# Submission for Spiral Matrix
# Submission url: https://leetcode.com/submissions/detail/1028015239/


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
            result.extend(matrix[top][left : right + 1])
            top += 1

            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                result.extend(matrix[bottom][right : left - 1 : -1])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                    left += 1

        return result
