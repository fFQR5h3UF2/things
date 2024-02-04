# Submission title: for Min Stack
# Submission url  : https://leetcode.com/submissions/detail/997558323/
# Submission json : {"id": 997558323, "status_display": "Accepted", "lang": "python3", "question_id": 155, "title_slug": "min-stack", "code": "from sortedcontainers import sortedset\n\nclass MinStack:\n    class Node:\n        def __init__(self, val: int, prev: 'Node'):\n            self.val = val\n            self.prev = prev\n\n\n    def __init__(self):\n        self.stack: List[Node] = []\n        self.min_node = None\n\n    def push(self, val: int) -> None:\n        new_node = self.Node(val, None)\n        self.stack.append(new_node)\n        if self.min_node is None or val <= self.min_node.val:\n            new_node.prev = self.min_node\n            self.min_node = new_node\n\n    def pop(self) -> None:\n        pop = self.stack.pop()\n        if pop == self.min_node:\n            self.min_node = self.min_node.prev\n\n    def top(self) -> int:\n        return self.stack[-1].val\n\n    def getMin(self) -> int:\n        return self.min_node.val\n\n\n# Your MinStack object will be instantiated and called as such:\n# obj = MinStack()\n# obj.push(val)\n# obj.pop()\n# param_3 = obj.top()\n# param_4 = obj.getMin()", "title": "Min Stack", "url": "/submissions/detail/997558323/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689684364, "status": 10, "runtime": "84 ms", "is_pending": "Not Pending", "memory": "21.6 MB", "compare_result": "1111111111111111111111111111111", "has_notes": false, "flag_type": 1}


from sortedcontainers import sortedset


class MinStack:
    class Node:
        def __init__(self, val: int, prev: "Node"):
            self.val = val
            self.prev = prev

    def __init__(self):
        self.stack: List[Node] = []
        self.min_node = None

    def push(self, val: int) -> None:
        new_node = self.Node(val, None)
        self.stack.append(new_node)
        if self.min_node is None or val <= self.min_node.val:
            new_node.prev = self.min_node
            self.min_node = new_node

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop == self.min_node:
            self.min_node = self.min_node.prev

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.min_node.val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
