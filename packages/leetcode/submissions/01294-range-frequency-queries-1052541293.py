# Submission title: for Range Frequency Queries
# Submission url  : https://leetcode.com/submissions/detail/1052541293/
# Submission json : {"id": 1052541293, "status_display": "Accepted", "lang": "python3", "question_id": 1294, "title_slug": "range-frequency-queries", "code": "class RangeFreqQuery:\n    def __init__(self, arr: List[int]):\n        self.l = [[] for _ in range(10001)]\n        for i, v in enumerate(arr):\n            self.l[v].append(i)\n            \n    def query(self, left: int, right: int, v: int) -> int:\n        return bisect_right(self.l[v], right) - bisect_left(self.l[v], left)\n\n# Your RangeFreqQuery object will be instantiated and called as such:\n# obj = RangeFreqQuery(arr)\n# param_1 = obj.query(left,right,value)", "title": "Range Frequency Queries", "url": "/submissions/detail/1052541293/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1695034450, "status": 10, "runtime": "1095 ms", "is_pending": "Not Pending", "memory": "55.8 MB", "compare_result": "11111111111111111111", "has_notes": false, "flag_type": 1}


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.l = [[] for _ in range(10001)]
        for i, v in enumerate(arr):
            self.l[v].append(i)

    def query(self, left: int, right: int, v: int) -> int:
        return bisect_right(self.l[v], right) - bisect_left(self.l[v], left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
