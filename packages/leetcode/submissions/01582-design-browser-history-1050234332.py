# Submission title: for Design Browser History
# Submission url  : https://leetcode.com/submissions/detail/1050234332/
# Submission json : {"id": 1050234332, "status_display": "Accepted", "lang": "python3", "question_id": 1582, "title_slug": "design-browser-history", "code": "class BrowserHistory:\n\n    def __init__(self, homepage: str):\n        self._history = [homepage]\n        self._cur = 0\n\n    def visit(self, url: str) -> None:\n        self._history[self._cur+1:] = (url, )\n        self._cur += 1\n\n    def back(self, steps: int) -> str:\n        self._cur = max(0, self._cur - steps)\n        return self._history[self._cur]\n\n    def forward(self, steps: int) -> str:\n        self._cur = min(len(self._history) - 1, self._cur + steps)\n        return self._history[self._cur]\n\n\n# Your BrowserHistory object will be instantiated and called as such:\n# obj = BrowserHistory(homepage)\n# obj.visit(url)\n# param_2 = obj.back(steps)\n# param_3 = obj.forward(steps)", "title": "Design Browser History", "url": "/submissions/detail/1050234332/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694794372, "status": 10, "runtime": "208 ms", "is_pending": "Not Pending", "memory": "19.1 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class BrowserHistory:

    def __init__(self, homepage: str):
        self._history = [homepage]
        self._cur = 0

    def visit(self, url: str) -> None:
        self._history[self._cur + 1 :] = (url,)
        self._cur += 1

    def back(self, steps: int) -> str:
        self._cur = max(0, self._cur - steps)
        return self._history[self._cur]

    def forward(self, steps: int) -> str:
        self._cur = min(len(self._history) - 1, self._cur + steps)
        return self._history[self._cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
