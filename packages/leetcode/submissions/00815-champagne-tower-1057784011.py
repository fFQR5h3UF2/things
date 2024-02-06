# Submission title: for Champagne Tower
# Submission url  : https://leetcode.com/submissions/detail/1057784011/
# Submission json : {"id": 1057784011, "status_display": "Accepted", "lang": "python3", "question_id": 815, "title_slug": "champagne-tower", "code": "class Solution:\n    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:\n        if query_row == 0:\n            return min(1, poured)\n        if query_glass in (0, query_row):\n            while query_row and poured:\n                poured = (poured - 1) / 2 if poured > 1 else 0\n                query_row -= 1\n            return min(1, poured)\n\n        cur_row, next_row = [0] * (query_row + 2), [0] * (query_row + 2)\n        cur_row[0] = poured\n        for row in range(query_row + 1):\n            next_row[0] = 0\n            for col in range(row + 1):\n                overflow = (cur_row[col] - 1) / 2\n                if overflow > 0:\n                    next_row[col] += overflow\n                    next_row[col + 1] = overflow\n                else:\n                    next_row[col + 1] = 0\n            cur_row, next_row = next_row, cur_row\n        return min(1, next_row[query_glass])", "title": "Champagne Tower", "url": "/submissions/detail/1057784011/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695546558, "status": 10, "runtime": "69 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0:
            return min(1, poured)
        if query_glass in (0, query_row):
            while query_row and poured:
                poured = (poured - 1) / 2 if poured > 1 else 0
                query_row -= 1
            return min(1, poured)

        cur_row, next_row = [0] * (query_row + 2), [0] * (query_row + 2)
        cur_row[0] = poured
        for row in range(query_row + 1):
            next_row[0] = 0
            for col in range(row + 1):
                overflow = (cur_row[col] - 1) / 2
                if overflow > 0:
                    next_row[col] += overflow
                    next_row[col + 1] = overflow
                else:
                    next_row[col + 1] = 0
            cur_row, next_row = next_row, cur_row
        return min(1, next_row[query_glass])
