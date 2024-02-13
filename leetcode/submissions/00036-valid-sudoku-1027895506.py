# Submission title: Valid Sudoku
# Submission url  : https://leetcode.com/problems/valid-sudoku/description/
# Submission url  : https://leetcode.com/submissions/detail/1027895506/
# Submission json : {"id":1027895506,"status_display":"Accepted","lang":"python3","question_id":36,"title_slug":"valid-sudoku","code":"class Solution:\n    def isValidSudoku(self, board: List[List[str]]) -> bool:\n        row_count, column_count = 9, 9\n\n        \n\n        row_counters = [defaultdict(bool) for _ in range(row_count)]\n        column_counters = [defaultdict(bool) for _ in range(column_count)]\n        subbox_counters = [[defaultdict(bool) for _ in range(column_count//3)] \n                            for _ in range(row_count//3)]\n\n        for row in range(row_count):\n            for column in range(column_count):\n                char = board[row][column]\n                if char == \".\":\n                    continue\n\n                counters = (\n                    row_counters[row], column_counters[column], \n                    subbox_counters[row//3][column//3]\n                )\n                for counter in counters:\n                    if counter[char]:\n                        return False\n\n                    counter[char] = True\n        \n        return True\n\n        ","title":"Valid Sudoku","url":"/submissions/detail/1027895506/","lang_name":"Python3","time":"5 months, 2 weeks","timestamp":1692641290,"status":10,"runtime":"110 ms","is_pending":"Not Pending","memory":"16.2 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count, column_count = 9, 9

        row_counters = [defaultdict(bool) for _ in range(row_count)]
        column_counters = [defaultdict(bool) for _ in range(column_count)]
        subbox_counters = [
            [defaultdict(bool) for _ in range(column_count // 3)]
            for _ in range(row_count // 3)
        ]

        for row in range(row_count):
            for column in range(column_count):
                char = board[row][column]
                if char == ".":
                    continue

                counters = (
                    row_counters[row],
                    column_counters[column],
                    subbox_counters[row // 3][column // 3],
                )
                for counter in counters:
                    if counter[char]:
                        return False

                    counter[char] = True

        return True
