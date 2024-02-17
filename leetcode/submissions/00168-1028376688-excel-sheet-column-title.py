# Submission title: Excel Sheet Column Title
# Submission url  : https://leetcode.com/problems/excel-sheet-column-title/description/"
# Submission url  : https://leetcode.com/submissions/detail/1028376688/"


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result.append(chr(65 + remainder))
        return "".join(reversed(result))
