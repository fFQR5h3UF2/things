# Submission title: for Implement Queue using Stacks
# Submission url  : https://leetcode.com/submissions/detail/1159838959/
# Submission json : {"id": 1159838959, "status_display": "Accepted", "lang": "python3", "question_id": 232, "title_slug": "implement-queue-using-stacks", "code": "class MyQueue:\n\n    def __init__(self):\n        self.stack_in = []\n        self.stack_out = []\n\n    def push(self, x: int) -> None:\n        self.stack_in.append(x)\n\n    def pop(self) -> int:\n        self.peek()\n        return self.stack_out.pop()\n\n    def peek(self) -> int:\n        if self.stack_out:\n            return self.stack_out[-1]\n        \n        while self.stack_in:\n            self.stack_out.append(self.stack_in.pop())\n\n        return self.stack_out[-1]\n\n    def empty(self) -> bool:\n        return not self.stack_out and not self.stack_in\n\n\n# Your MyQueue object will be instantiated and called as such:\n# obj = MyQueue()\n# obj.push(x)\n# param_2 = obj.pop()\n# param_3 = obj.peek()\n# param_4 = obj.empty()", "title": "Implement Queue using Stacks", "url": "/submissions/detail/1159838959/", "lang_name": "Python3", "time": "6\u00a0days, 7\u00a0hours", "timestamp": 1706510673, "status": 10, "runtime": "39 ms", "is_pending": "Not Pending", "memory": "16.5 MB", "compare_result": "1111111111111111111111", "has_notes": false, "flag_type": 1}


class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack_out.pop()

    def peek(self) -> int:
        if self.stack_out:
            return self.stack_out[-1]

        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_out and not self.stack_in


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
