# Submission title: for K-th Symbol in Grammar
# Submission url  : https://leetcode.com/submissions/detail/1083664565/
# Submission json : {"id": 1083664565, "status_display": "Accepted", "lang": "python3", "question_id": 795, "title_slug": "k-th-symbol-in-grammar", "code": "class Solution:\n    def kthGrammar(self, n: int, k: int) -> int:\n\n        def get(row: int, column: int) -> int:\n            if column == 0 or column == 1:\n                return column\n            \n            prev_row_length = 2 ** (row - 1)\n            if column >= prev_row_length:\n                return 1 ^ get(row - 1, column - prev_row_length)\n            return get(row - 1, column)\n\n        return get(n - 1, k - 1)\n\n        # 0\n        # 0 1\n        # 0 1 1 0\n        # 0 1 1 0 1 0 0 1\n        # 0 1 1 0 1 0 0 1\n", "title": "K-th Symbol in Grammar", "url": "/submissions/detail/1083664565/", "lang_name": "Python3", "time": "3\u00a0months, 1\u00a0week", "timestamp": 1698222665, "status": 10, "runtime": "41 ms", "is_pending": "Not Pending", "memory": "16.1 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def get(row: int, column: int) -> int:
            if column == 0 or column == 1:
                return column

            prev_row_length = 2 ** (row - 1)
            if column >= prev_row_length:
                return 1 ^ get(row - 1, column - prev_row_length)
            return get(row - 1, column)

        return get(n - 1, k - 1)

        # 0
        # 0 1
        # 0 1 1 0
        # 0 1 1 0 1 0 0 1
        # 0 1 1 0 1 0 0 1
