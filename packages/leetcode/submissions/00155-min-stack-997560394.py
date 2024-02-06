# Submission title: for Min Stack
# Submission url  : https://leetcode.com/submissions/detail/997560394/
# Submission json : {"id": 997560394, "status_display": "Accepted", "lang": "python3", "question_id": 155, "title_slug": "min-stack", "code": "from sortedcontainers import sortedset\n\nclass MinStack:\n\n    def __init__(self):\n        self.stack: List[int] = []\n        self.min_stack: List[int] = []\n\n    def push(self, val: int) -> None:\n        self.stack.append(val)\n        if not self.min_stack or val <= self.min_stack[-1]:\n            self.min_stack.append(val)\n\n    def pop(self) -> None:\n        if not self.stack:\n            return\n        pop = self.stack.pop()\n        if pop == self.min_stack[-1]:\n            self.min_stack.pop()\n\n    def top(self) -> int:\n        return self.stack[-1]\n\n    def getMin(self) -> int:\n        return self.min_stack[-1]\n\n\n# Your MinStack object will be instantiated and called as such:\n# obj = MinStack()\n# obj.push(val)\n# obj.pop()\n# param_3 = obj.top()\n# param_4 = obj.getMin()", "title": "Min Stack", "url": "/submissions/detail/997560394/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689684557, "status": 10, "runtime": "77 ms", "is_pending": "Not Pending", "memory": "20.4 MB", "compare_result": "1111111111111111111111111111111", "has_notes": false, "flag_type": 1}


from sortedcontainers import sortedset


class MinStack:

    def __init__(self):
        self.stack: List[int] = []
        self.min_stack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
