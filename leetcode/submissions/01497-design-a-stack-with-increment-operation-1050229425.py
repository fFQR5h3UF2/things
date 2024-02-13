# Submission title: Design a Stack With Increment Operation
# Submission url  : https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
# Submission url  : https://leetcode.com/submissions/detail/1050229425/
# Submission json : {"id":1050229425,"status_display":"Accepted","lang":"python3","question_id":1497,"title_slug":"design-a-stack-with-increment-operation","code":"class CustomStack:\n\n    def __init__(self, maxSize: int):\n        self._stack = []\n        self._max_size = maxSize\n\n    def push(self, x: int) -> None:\n        if len(self._stack) != self._max_size:\n            self._stack.append(x)\n\n    def pop(self) -> int:\n        return self._stack.pop() if self._stack else -1 \n        \n    def increment(self, k: int, val: int) -> None:\n        for i in range(min(k, len(self._stack))):\n            self._stack[i] += val\n\n\n# Your CustomStack object will be instantiated and called as such:\n# obj = CustomStack(maxSize)\n# obj.push(x)\n# param_2 = obj.pop()\n# obj.increment(k,val)","title":"Design a Stack With Increment Operation","url":"/submissions/detail/1050229425/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694793916,"status":10,"runtime":"100 ms","is_pending":"Not Pending","memory":"17.3 MB","compare_result":"1111111111111111111111111111111111","has_notes":false,"flag_type":1}


class CustomStack:

    def __init__(self, maxSize: int):
        self._stack = []
        self._max_size = maxSize

    def push(self, x: int) -> None:
        if len(self._stack) != self._max_size:
            self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop() if self._stack else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self._stack))):
            self._stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
