# Submission title: for Min Cost to Connect All Points
# Submission url  : https://leetcode.com/submissions/detail/1049921218/
# Submission json : {"id": 1049921218, "status_display": "Accepted", "lang": "python3", "question_id": 1706, "title_slug": "min-cost-to-connect-all-points", "code": "def manhattan_distance(p1: List[int], p2: List[int]) -> int:\n    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])\n\nclass Solution:\n    def minCostConnectPoints(self, points: List[List[int]]) -> int:\n        n = len(points)\n        visited = [False] * n\n        heap_dict = {0: 0}  \n        min_heap = [(0, 0)]\n        \n        mst_weight = 0\n        \n        while min_heap:\n            w, u = heappop(min_heap)\n            \n            if visited[u] or heap_dict.get(u, float('inf')) < w:\n                continue\n            \n            visited[u] = True\n            mst_weight += w\n            \n            for v in range(n):\n                if not visited[v]:\n                    new_distance = manhattan_distance(points[u], points[v])\n      \n                    if new_distance < heap_dict.get(v, float('inf')):\n                        heap_dict[v] = new_distance\n                        heappush(min_heap, (new_distance, v))\n        \n        return mst_weight", "title": "Min Cost to Connect All Points", "url": "/submissions/detail/1049921218/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694761155, "status": 10, "runtime": "742 ms", "is_pending": "Not Pending", "memory": "20.3 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


def manhattan_distance(p1: List[int], p2: List[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        heap_dict = {0: 0}
        min_heap = [(0, 0)]

        mst_weight = 0

        while min_heap:
            w, u = heappop(min_heap)

            if visited[u] or heap_dict.get(u, float("inf")) < w:
                continue

            visited[u] = True
            mst_weight += w

            for v in range(n):
                if not visited[v]:
                    new_distance = manhattan_distance(points[u], points[v])

                    if new_distance < heap_dict.get(v, float("inf")):
                        heap_dict[v] = new_distance
                        heappush(min_heap, (new_distance, v))

        return mst_weight
