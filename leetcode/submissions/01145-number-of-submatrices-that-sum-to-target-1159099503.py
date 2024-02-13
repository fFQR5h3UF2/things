# Submission title: Number of Submatrices That Sum to Target
# Submission url  : https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/
# Submission url  : https://leetcode.com/submissions/detail/1159099503/
# Submission json : {"id":1159099503,"status_display":"Accepted","lang":"python3","question_id":1145,"title_slug":"number-of-submatrices-that-sum-to-target","code":"class Solution:\n    def numSubmatrixSumTarget(self, matrix, target):\n        m, n = len(matrix), len(matrix[0])\n\n        for row in range(m):\n            for col in range(1, n):\n                matrix[row][col] += matrix[row][col - 1]\n\n        count = 0\n\n        for c1 in range(n):\n            for c2 in range(c1, n):\n                prefix_sum_count = {0: 1}\n                sum_val = 0\n\n                for row in range(m):\n                    sum_val += matrix[row][c2] - (matrix[row][c1 - 1] if c1 > 0 else 0)\n                    count += prefix_sum_count.get(sum_val - target, 0)\n                    prefix_sum_count[sum_val] = prefix_sum_count.get(sum_val, 0) + 1\n\n        return count\n\n","title":"Number of Submatrices That Sum to Target","url":"/submissions/detail/1159099503/","lang_name":"Python3","time":"1 week","timestamp":1706438043,"status":10,"runtime":"422 ms","is_pending":"Not Pending","memory":"17.7 MB","compare_result":"1111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        for row in range(m):
            for col in range(1, n):
                matrix[row][col] += matrix[row][col - 1]

        count = 0

        for c1 in range(n):
            for c2 in range(c1, n):
                prefix_sum_count = {0: 1}
                sum_val = 0

                for row in range(m):
                    sum_val += matrix[row][c2] - (matrix[row][c1 - 1] if c1 > 0 else 0)
                    count += prefix_sum_count.get(sum_val - target, 0)
                    prefix_sum_count[sum_val] = prefix_sum_count.get(sum_val, 0) + 1

        return count
