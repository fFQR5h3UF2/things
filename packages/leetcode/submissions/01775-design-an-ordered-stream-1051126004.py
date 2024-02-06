# Submission title: for Design an Ordered Stream
# Submission url  : https://leetcode.com/submissions/detail/1051126004/
# Submission json : {"id": 1051126004, "status_display": "Accepted", "lang": "python3", "question_id": 1775, "title_slug": "design-an-ordered-stream", "code": "class OrderedStream:\n\n    def __init__(self, n: int):\n        self.data = [None]*n\n        self.ptr = 0 # 0-indexed \n\n    def insert(self, id: int, value: str) -> List[str]:\n        id -= 1 # 0-indexed \n        self.data[id] = value \n        if id > self.ptr: return [] # not reaching ptr \n        \n        while self.ptr < len(self.data) and self.data[self.ptr]: self.ptr += 1 # update self.ptr \n        return self.data[id:self.ptr]\n\n\n\n# Your OrderedStream object will be instantiated and called as such:\n# obj = OrderedStream(n)\n# param_1 = obj.insert(idKey,value)", "title": "Design an Ordered Stream", "url": "/submissions/detail/1051126004/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1694884821, "status": 10, "runtime": "251 ms", "is_pending": "Not Pending", "memory": "17 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.ptr = 0  # 0-indexed

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1  # 0-indexed
        self.data[id] = value
        if id > self.ptr:
            return []  # not reaching ptr

        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr += 1  # update self.ptr
        return self.data[id : self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
