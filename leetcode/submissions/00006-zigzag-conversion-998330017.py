# Submission title: Zigzag Conversion
# Submission url  : https://leetcode.com/problems/zigzag-conversion/description/
# Submission url  : https://leetcode.com/submissions/detail/998330017/
# Submission json : {"id":998330017,"status_display":"Accepted","lang":"python3","question_id":6,"title_slug":"zigzag-conversion","code":"class Solution:\n    def convert(self, s: str, numRows: int) -> str:\n        if numRows < 2:\n            return s\n        \n        result: List[List[str]] = [[] for _ in range(numRows)]\n    \n        row, is_ascending, last = 0, True, numRows - 1\n        for symbol in s:\n            result[row].append(symbol)\n            \n            if is_ascending and row < last:\n                row += 1\n            elif is_ascending:\n                is_ascending = False\n            \n            if is_ascending:\n                continue\n\n            if row > 0:\n                row -= 1\n            else:\n                is_ascending = True\n                row = 1\n    \n        \n        return \"\".join(\"\".join(row) for row in result)","title":"Zigzag Conversion","url":"/submissions/detail/998330017/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689759202,"status":10,"runtime":"65 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        result: List[List[str]] = [[] for _ in range(numRows)]

        row, is_ascending, last = 0, True, numRows - 1
        for symbol in s:
            result[row].append(symbol)

            if is_ascending and row < last:
                row += 1
            elif is_ascending:
                is_ascending = False

            if is_ascending:
                continue

            if row > 0:
                row -= 1
            else:
                is_ascending = True
                row = 1

        return "".join("".join(row) for row in result)
