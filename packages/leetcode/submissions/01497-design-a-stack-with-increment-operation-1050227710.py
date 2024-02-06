# Submission title: for Design a Stack With Increment Operation
# Submission url  : https://leetcode.com/submissions/detail/1050227710/
# Submission json : {"id": 1050227710, "status_display": "Accepted", "lang": "python3", "question_id": 1497, "title_slug": "design-a-stack-with-increment-operation", "code": "class CustomStack:\n\n    def __init__(self, maxSize: int):\n        self._stack = []\n        self._max_size = maxSize\n        self._size = 0\n\n    def push(self, x: int) -> None:\n        if self._size == self._max_size:\n            return\n        self._stack.append(x)\n        self._size += 1\n\n    def pop(self) -> int:\n        if self._size == 0:\n            return -1\n        last = self._stack.pop()\n        self._size -= 1\n        return last\n\n    def increment(self, k: int, val: int) -> None:\n        for i in range(min(k, self._size)):\n            self._stack[i] += val\n\n\n# Your CustomStack object will be instantiated and called as such:\n# obj = CustomStack(maxSize)\n# obj.push(x)\n# param_2 = obj.pop()\n# obj.increment(k,val)", "title": "Design a Stack With Increment Operation", "url": "/submissions/detail/1050227710/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694793762, "status": 10, "runtime": "112 ms", "is_pending": "Not Pending", "memory": "17.1 MB", "compare_result": "1111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class CustomStack:

    def __init__(self, maxSize: int):
        self._stack = []
        self._max_size = maxSize
        self._size = 0

    def push(self, x: int) -> None:
        if self._size == self._max_size:
            return
        self._stack.append(x)
        self._size += 1

    def pop(self) -> int:
        if self._size == 0:
            return -1
        last = self._stack.pop()
        self._size -= 1
        return last

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self._size)):
            self._stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
