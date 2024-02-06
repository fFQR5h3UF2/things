# Submission title: for Number of Recent Calls
# Submission url  : https://leetcode.com/submissions/detail/1047428915/
# Submission json : {"id": 1047428915, "status_display": "Accepted", "lang": "python3", "question_id": 969, "title_slug": "number-of-recent-calls", "code": "class RecentCounter:\n\n    def __init__(self):\n        self._queue = deque()\n\n    def ping(self, t: int) -> int:\n        self._queue.append(t)\n        while self._queue:\n            if t - self._queue[0] > 3000:\n                self._queue.popleft()\n            else:\n                break\n\n        return len(self._queue) \n\n\n# Your RecentCounter object will be instantiated and called as such:\n# obj = RecentCounter()\n# param_1 = obj.ping(t)", "title": "Number of Recent Calls", "url": "/submissions/detail/1047428915/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694521265, "status": 10, "runtime": "217 ms", "is_pending": "Not Pending", "memory": "21.4 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class RecentCounter:

    def __init__(self):
        self._queue = deque()

    def ping(self, t: int) -> int:
        self._queue.append(t)
        while self._queue:
            if t - self._queue[0] > 3000:
                self._queue.popleft()
            else:
                break

        return len(self._queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
