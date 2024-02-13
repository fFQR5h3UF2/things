# Submission title: 01 Matrix
# Submission url  : https://leetcode.com/problems/01-matrix/description/
# Submission url  : https://leetcode.com/submissions/detail/1023985105/
# Submission json : {"id":1023985105,"status_display":"Accepted","lang":"python3","question_id":542,"title_slug":"01-matrix","code":"class Solution:\n    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:\n        if not mat or not mat[0]:\n            return []\n\n        row_count, column_count = len(mat), len(mat[0])\n        queue = set()\n        MAX_VALUE = row_count * column_count\n        \n        # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.\n        for row in range(row_count):\n            for column in range(column_count):\n                if mat[row][column] == 0:\n                    queue.add((row, column))\n                else:\n                    mat[row][column] = MAX_VALUE\n        \n        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))\n        \n        while queue:\n            center_row, center_column = queue.pop()\n            distance_from_center = mat[center_row][center_column] + 1\n\n            for delta_row, delta_column in directions:\n                new_row, new_column = center_row + delta_row, center_column + delta_column\n                if not 0 <= new_row < row_count or not 0 <= new_column < column_count:\n                    continue\n    \n                if mat[new_row][new_column] > distance_from_center:\n                    queue.add((new_row, new_column))\n                    mat[new_row][new_column] = distance_from_center\n        \n        return mat","title":"01 Matrix","url":"/submissions/detail/1023985105/","lang_name":"Python3","time":"5 months, 3 weeks","timestamp":1692280378,"status":10,"runtime":"533 ms","is_pending":"Not Pending","memory":"19.4 MB","compare_result":"11111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        row_count, column_count = len(mat), len(mat[0])
        queue = set()
        MAX_VALUE = row_count * column_count

        # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.
        for row in range(row_count):
            for column in range(column_count):
                if mat[row][column] == 0:
                    queue.add((row, column))
                else:
                    mat[row][column] = MAX_VALUE

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            center_row, center_column = queue.pop()
            distance_from_center = mat[center_row][center_column] + 1

            for delta_row, delta_column in directions:
                new_row, new_column = (
                    center_row + delta_row,
                    center_column + delta_column,
                )
                if not 0 <= new_row < row_count or not 0 <= new_column < column_count:
                    continue

                if mat[new_row][new_column] > distance_from_center:
                    queue.add((new_row, new_column))
                    mat[new_row][new_column] = distance_from_center

        return mat
