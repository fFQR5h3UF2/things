# Submission title: Rotate Image
# Submission url  : https://leetcode.com/problems/rotate-image/description/
# Submission url  : https://leetcode.com/submissions/detail/1038443511/
# Submission json : {"id":1038443511,"status_display":"Accepted","lang":"python3","question_id":48,"title_slug":"rotate-image","code":"class Solution:\n    def rotate(self, matrix: List[List[int]]) -> None:\n        \"\"\"\n        Do not return anything, modify matrix in-place instead.\n        \"\"\"\n        side_length = len(matrix)\n\n        for row in range(side_length // 2):\n            matrix[row], matrix[-row-1] = matrix[-row-1], matrix[row]\n        \n        for i in range(side_length):\n            for j in range(i):\n                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]","title":"Rotate Image","url":"/submissions/detail/1038443511/","lang_name":"Python3","time":"5 months","timestamp":1693661173,"status":10,"runtime":"46 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        side_length = len(matrix)

        for row in range(side_length // 2):
            matrix[row], matrix[-row - 1] = matrix[-row - 1], matrix[row]

        for i in range(side_length):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
