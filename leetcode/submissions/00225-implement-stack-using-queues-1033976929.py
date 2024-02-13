# Submission title: Implement Stack using Queues
# Submission url  : https://leetcode.com/problems/implement-stack-using-queues/description/
# Submission url  : https://leetcode.com/submissions/detail/1033976929/
# Submission json : {"id":1033976929,"status_display":"Accepted","lang":"python3","question_id":225,"title_slug":"implement-stack-using-queues","code":"class MyStack:\n\n    def __init__(self):\n        self._queue = []\n\n    def push(self, x: int) -> None:\n        self._queue.append(x)\n\n    def pop(self) -> int:\n        return self._queue.pop()\n\n    def top(self) -> int:\n        return self._queue[-1]\n\n    def empty(self) -> bool:\n        return len(self._queue) == 0 \n\n\n# Your MyStack object will be instantiated and called as such:\n# obj = MyStack()\n# obj.push(x)\n# param_2 = obj.pop()\n# param_3 = obj.top()\n# param_4 = obj.empty()","title":"Implement Stack using Queues","url":"/submissions/detail/1033976929/","lang_name":"Python3","time":"5 months, 1 week","timestamp":1693218954,"status":10,"runtime":"40 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"11111111111111111","has_notes":false,"flag_type":1}


class MyStack:

    def __init__(self):
        self._queue = []

    def push(self, x: int) -> None:
        self._queue.append(x)

    def pop(self) -> int:
        return self._queue.pop()

    def top(self) -> int:
        return self._queue[-1]

    def empty(self) -> bool:
        return len(self._queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
