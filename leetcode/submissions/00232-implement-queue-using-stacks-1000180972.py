# Submission title: Implement Queue using Stacks
# Submission url  : https://leetcode.com/problems/implement-queue-using-stacks/description/
# Submission url  : https://leetcode.com/submissions/detail/1000180972/
# Submission json : {"id":1000180972,"status_display":"Accepted","lang":"python3","question_id":232,"title_slug":"implement-queue-using-stacks","code":"class MyQueue:\n\n    def __init__(self):\n        self.queue = deque()\n\n    def push(self, x: int) -> None:\n        self.queue.appendleft(x)\n\n    def pop(self) -> int:\n        return self.queue.pop()\n\n    def peek(self) -> int:\n        return self.queue[-1]\n\n    def empty(self) -> bool:\n        return len(self.queue) == 0\n\n\n# Your MyQueue object will be instantiated and called as such:\n# obj = MyQueue()\n# obj.push(x)\n# param_2 = obj.pop()\n# param_3 = obj.peek()\n# param_4 = obj.empty()","title":"Implement Queue using Stacks","url":"/submissions/detail/1000180972/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689944980,"status":10,"runtime":"50 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"1111111111111111111111","has_notes":false,"flag_type":1}


class MyQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.appendleft(x)

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
