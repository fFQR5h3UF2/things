# Submission title: for Find Eventual Safe States
# Submission url  : https://leetcode.com/submissions/detail/1010367344/
# Submission json : {"id": 1010367344, "status_display": "Accepted", "lang": "python3", "question_id": 820, "title_slug": "find-eventual-safe-states", "code": "class Solution:\n    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:\n        length = len(graph)\n        indegree = [0] * length\n        adj = [[] for _ in range(length)]\n\n        for i in range(length):\n            for edge in graph[i]:\n                adj[edge].append(i)\n                indegree[i] += 1\n\n        q = deque()\n        # Push all the nodes with indegree zero in the queue.\n        for i in range(length):\n            if indegree[i] == 0:\n                q.append(i)\n\n        safe = [False] * length\n        while q:\n            node = q.popleft()\n            safe[node] = True\n\n            for neighbor in adj[node]:\n                # Delete the edge \"node -> neighbor\".\n                indegree[neighbor] -= 1\n                if indegree[neighbor] == 0:\n                    q.append(neighbor)\n\n        safe_nodes = []\n        for i in range(length):\n            if safe[i]:\n                safe_nodes.append(i)\n\n        return safe_nodes", "title": "Find Eventual Safe States", "url": "/submissions/detail/1010367344/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1690989104, "status": 10, "runtime": "601 ms", "is_pending": "Not Pending", "memory": "23.7 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        indegree = [0] * length
        adj = [[] for _ in range(length)]

        for i in range(length):
            for edge in graph[i]:
                adj[edge].append(i)
                indegree[i] += 1

        q = deque()
        # Push all the nodes with indegree zero in the queue.
        for i in range(length):
            if indegree[i] == 0:
                q.append(i)

        safe = [False] * length
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                # Delete the edge "node -> neighbor".
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        safe_nodes = []
        for i in range(length):
            if safe[i]:
                safe_nodes.append(i)

        return safe_nodes
