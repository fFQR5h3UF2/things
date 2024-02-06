# Submission title: for Implement Queue using Stacks
# Submission url  : https://leetcode.com/submissions/detail/1000187382/
# Submission json : {"id": 1000187382, "status_display": "Accepted", "lang": "python3", "question_id": 232, "title_slug": "implement-queue-using-stacks", "code": "class MyQueue:\n\n    def __init__(self):\n        self.queue = []\n\n    def push(self, x: int) -> None:\n        self.queue.insert(0, x)\n\n    def pop(self) -> int:\n        return self.queue.pop()\n\n    def peek(self) -> int:\n        return self.queue[-1]\n\n    def empty(self) -> bool:\n        return len(self.queue) == 0\n\n\n# Your MyQueue object will be instantiated and called as such:\n# obj = MyQueue()\n# obj.push(x)\n# param_2 = obj.pop()\n# param_3 = obj.peek()\n# param_4 = obj.empty()", "title": "Implement Queue using Stacks", "url": "/submissions/detail/1000187382/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689945649, "status": 10, "runtime": "55 ms", "is_pending": "Not Pending", "memory": "16.5 MB", "compare_result": "1111111111111111111111", "has_notes": false, "flag_type": 1}


class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.insert(0, x)

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
