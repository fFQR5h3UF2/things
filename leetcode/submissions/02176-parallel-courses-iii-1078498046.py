# Submission title: Parallel Courses III
# Submission url  : https://leetcode.com/problems/parallel-courses-iii/description/
# Submission url  : https://leetcode.com/submissions/detail/1078498046/
# Submission json : {"id":1078498046,"status_display":"Accepted","lang":"python3","question_id":2176,"title_slug":"parallel-courses-iii","code":"class Solution:\n    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:\n        graph = defaultdict(list)\n        indegree = [0] * n\n        \n        for (x, y) in relations:\n            graph[x - 1].append(y - 1)\n            indegree[y - 1] += 1\n        \n        queue = deque()\n        max_time = [0] * n\n        for node in range(n):\n            if indegree[node] == 0:\n                queue.append(node)\n                max_time[node] = time[node]\n\n        while queue:\n            node = queue.popleft()\n            for neighbor in graph[node]:\n                max_time[neighbor] = max(max_time[neighbor], max_time[node] + time[neighbor])\n                indegree[neighbor] -= 1\n                if indegree[neighbor] == 0:\n                    queue.append(neighbor)\n\n        return max(max_time)","title":"Parallel Courses III","url":"/submissions/detail/1078498046/","lang_name":"Python3","time":"3 months, 2 weeks","timestamp":1697647133,"status":10,"runtime":"1416 ms","is_pending":"Not Pending","memory":"45.1 MB","compare_result":"111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n

        for x, y in relations:
            graph[x - 1].append(y - 1)
            indegree[y - 1] += 1

        queue = deque()
        max_time = [0] * n
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
                max_time[node] = time[node]

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                max_time[neighbor] = max(
                    max_time[neighbor], max_time[node] + time[neighbor]
                )
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return max(max_time)
