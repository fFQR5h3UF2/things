# Submission title: for Path With Minimum Effort
# Submission url  : https://leetcode.com/submissions/detail/1050711409/
# Submission json : {"id": 1050711409, "status_display": "Accepted", "lang": "python3", "question_id": 1753, "title_slug": "path-with-minimum-effort", "code": "class Solution:\r\n\r\n    def minimumEffortPath(self, heights: List[List[int]]) -> int:\r\n        rows, cols = len(heights), len(heights[0])\r\n        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]\r\n        dist = [[math.inf for _ in range(cols)] for _ in range(rows)]\r\n        dist[0][0] = 0\r\n        minHeap = [(0, 0, 0)] \r\n        while minHeap:\r\n            effort, x, y = heappop(minHeap)\r\n            if x == rows - 1 and y == cols - 1:\r\n                return effort\r\n            for dx, dy in directions:\r\n                nx, ny = x + dx, y + dy\r\n                if 0 <= nx < rows and 0 <= ny < cols:\r\n                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))\r\n                    if new_effort < dist[nx][ny]:\r\n                        dist[nx][ny] = new_effort\r\n                        heappush(minHeap, (new_effort, nx, ny))", "title": "Path With Minimum Effort", "url": "/submissions/detail/1050711409/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694852754, "status": 10, "runtime": "521 ms", "is_pending": "Not Pending", "memory": "17.7 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[math.inf for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)]
        while minHeap:
            effort, x, y = heappop(minHeap)
            if x == rows - 1 and y == cols - 1:
                return effort
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heappush(minHeap, (new_effort, nx, ny))
