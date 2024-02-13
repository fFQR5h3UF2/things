# Submission title: Minimum Falling Path Sum
# Submission url  : https://leetcode.com/problems/minimum-falling-path-sum/description/
# Submission url  : https://leetcode.com/submissions/detail/1150545529/
# Submission json : {"id":1150545529,"status_display":"Accepted","lang":"python3","question_id":967,"title_slug":"minimum-falling-path-sum","code":"class Solution:\n    def minFallingPathSum(self, matrix: List[List[int]]) -> int:\n        length = len(matrix)\n        cache = {}\n        deltas = ((1, 0), (1, 1), (1, -1))\n        last_row = length - 1\n\n        def dp(row: int, col: int) -> int:\n            if (row, col) in cache:\n                return cache[(row, col)]\n            val = matrix[row][col]\n            if row == last_row:\n                return val\n            min_cost = None\n            for delta_row, delta_col in deltas:\n                new_row, new_col = row + delta_row, col + delta_col\n                if new_col == length or new_col == -1:\n                    continue\n                cost = dp(new_row, new_col)\n                min_cost = cost if min_cost is None else min(min_cost, cost)\n            res = val + min_cost\n            cache[(row, col)] = res\n            return res\n\n        return min(dp(0, col) for col in range(length))","title":"Minimum Falling Path Sum","url":"/submissions/detail/1150545529/","lang_name":"Python3","time":"2 weeks, 2 days","timestamp":1705653981,"status":10,"runtime":"154 ms","is_pending":"Not Pending","memory":"26.9 MB","compare_result":"11111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        cache = {}
        deltas = ((1, 0), (1, 1), (1, -1))
        last_row = length - 1

        def dp(row: int, col: int) -> int:
            if (row, col) in cache:
                return cache[(row, col)]
            val = matrix[row][col]
            if row == last_row:
                return val
            min_cost = None
            for delta_row, delta_col in deltas:
                new_row, new_col = row + delta_row, col + delta_col
                if new_col == length or new_col == -1:
                    continue
                cost = dp(new_row, new_col)
                min_cost = cost if min_cost is None else min(min_cost, cost)
            res = val + min_cost
            cache[(row, col)] = res
            return res

        return min(dp(0, col) for col in range(length))
