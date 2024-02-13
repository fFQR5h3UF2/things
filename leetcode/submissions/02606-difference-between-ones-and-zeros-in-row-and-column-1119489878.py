# Submission title: Difference Between Ones and Zeros in Row and Column
# Submission url  : https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
# Submission url  : https://leetcode.com/submissions/detail/1119489878/
# Submission json : {"id":1119489878,"status_display":"Accepted","lang":"python3","question_id":2606,"title_slug":"difference-between-ones-and-zeros-in-row-and-column","code":"class Solution:\n    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:\n        m = len(grid)\n        n = len(grid[0])\n\n        rows = {}\n        for r in range(m):        \n            row_sum = 0\n            for c in range(n):\n                row_sum += grid[r][c]\n            \n            rows[r] = row_sum\n\n        cols = {}\n        for c in range(n):\n            col_sum = 0\n            for r in range(m):\n                col_sum += grid[r][c]\n            \n            cols[c] = col_sum\n\n        res = [[0] * n for _ in range(m)]\n\n        for r in range(m):\n            for c in range(n):\n                res[r][c] = rows[r] + cols[c] - (m - rows[r]) - (n - cols[c])\n        \n        return res","title":"Difference Between Ones and Zeros in Row and Column","url":"/submissions/detail/1119489878/","lang_name":"Python3","time":"1 month, 3 weeks","timestamp":1702546254,"status":10,"runtime":"1407 ms","is_pending":"Not Pending","memory":"57.6 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        rows = {}
        for r in range(m):
            row_sum = 0
            for c in range(n):
                row_sum += grid[r][c]

            rows[r] = row_sum

        cols = {}
        for c in range(n):
            col_sum = 0
            for r in range(m):
                col_sum += grid[r][c]

            cols[c] = col_sum

        res = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                res[r][c] = rows[r] + cols[c] - (m - rows[r]) - (n - cols[c])

        return res
