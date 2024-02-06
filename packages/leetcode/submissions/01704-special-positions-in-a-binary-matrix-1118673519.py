# Submission title: for Special Positions in a Binary Matrix
# Submission url  : https://leetcode.com/submissions/detail/1118673519/
# Submission json : {"id": 1118673519, "status_display": "Accepted", "lang": "python3", "question_id": 1704, "title_slug": "special-positions-in-a-binary-matrix", "code": "class Solution:\n    def numSpecial(self, mat: List[List[int]]) -> int:\n        def get_column_sum(col_idx):\n            return sum(row[col_idx] for row in mat)\n\n        special = 0\n        for row in mat:\n            if sum(row) == 1:\n                col_idx = row.index(1)\n                special += get_column_sum(col_idx) == 1\n\n        return special", "title": "Special Positions in a Binary Matrix", "url": "/submissions/detail/1118673519/", "lang_name": "Python3", "time": "1\u00a0month, 3\u00a0weeks", "timestamp": 1702455059, "status": 10, "runtime": "137 ms", "is_pending": "Not Pending", "memory": "16.7 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def get_column_sum(col_idx):
            return sum(row[col_idx] for row in mat)

        special = 0
        for row in mat:
            if sum(row) == 1:
                col_idx = row.index(1)
                special += get_column_sum(col_idx) == 1

        return special
