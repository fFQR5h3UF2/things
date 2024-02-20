# Submission title: Number of Recent Calls
# Submission url  : https://leetcode.com/problems/number-of-recent-calls/description/
# Submission url  : https://leetcode.com/submissions/detail/1047428915/"


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
