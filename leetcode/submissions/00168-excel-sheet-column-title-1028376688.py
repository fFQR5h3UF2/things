# Submission title: for Excel Sheet Column Title
# Submission url  : https://leetcode.com/submissions/detail/1028376688/
# Submission json : {"id": 1028376688, "status_display": "Accepted", "lang": "python3", "question_id": 168, "title_slug": "excel-sheet-column-title", "code": "class Solution:\n    def convertToTitle(self, columnNumber: int) -> str:\n        result = []\n        while columnNumber:\n            columnNumber, remainder = divmod(columnNumber - 1, 26)\n            result.append(chr(65 + remainder))\n        return ''.join(reversed(result))", "title": "Excel Sheet Column Title", "url": "/submissions/detail/1028376688/", "lang_name": "Python3", "time": "5\u00a0months, 2\u00a0weeks", "timestamp": 1692689547, "status": 10, "runtime": "32 ms", "is_pending": "Not Pending", "memory": "16.2 MB", "compare_result": "1111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result.append(chr(65 + remainder))
        return "".join(reversed(result))
