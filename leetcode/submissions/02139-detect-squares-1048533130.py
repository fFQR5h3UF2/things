# Submission title: for Detect Squares
# Submission url  : https://leetcode.com/submissions/detail/1048533130/
# Submission json : {"id": 1048533130, "status_display": "Accepted", "lang": "python3", "question_id": 2139, "title_slug": "detect-squares", "code": "class DetectSquares:\n\n    def __init__(self):\n        self._row_col = defaultdict(lambda: defaultdict(int))\n\n    def add(self, point: List[int]) -> None:\n        self._row_col[point[0]][point[1]] += 1\n\n    def count(self, point: List[int]) -> int:\n        ways_count = 0\n        row1, col1 = point\n        for col2, col2_count in self._row_col[row1].items():\n            if col2 == col1:\n                continue\n\n            side = col2 - col1\n            for row2 in (row1 + side, row1 - side):\n                point3_count = self._row_col[row2][col1]\n                point4_count = self._row_col[row2][col2]\n                ways_count += col2_count * point3_count * point4_count\n\n        return ways_count\n\n# Your DetectSquares object will be instantiated and called as such:\n# obj = DetectSquares()\n# obj.add(point)\n# param_2 = obj.count(point)", "title": "Detect Squares", "url": "/submissions/detail/1048533130/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694622004, "status": 10, "runtime": "217 ms", "is_pending": "Not Pending", "memory": "18.2 MB", "compare_result": "111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class DetectSquares:

    def __init__(self):
        self._row_col = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self._row_col[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        ways_count = 0
        row1, col1 = point
        for col2, col2_count in self._row_col[row1].items():
            if col2 == col1:
                continue

            side = col2 - col1
            for row2 in (row1 + side, row1 - side):
                point3_count = self._row_col[row2][col1]
                point4_count = self._row_col[row2][col2]
                ways_count += col2_count * point3_count * point4_count

        return ways_count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
