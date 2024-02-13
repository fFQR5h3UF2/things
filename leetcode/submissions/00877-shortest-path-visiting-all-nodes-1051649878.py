# Submission title: Shortest Path Visiting All Nodes
# Submission url  : https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/
# Submission url  : https://leetcode.com/submissions/detail/1051649878/
# Submission json : {"id":1051649878,"status_display":"Accepted","lang":"python3","question_id":877,"title_slug":"shortest-path-visiting-all-nodes","code":"from collections import deque, namedtuple\n\nclass Solution:\n    def shortestPathLength(self, graph):\n        n = len(graph)\n        all_mask = (1 << n) - 1\n        visited = set()\n        Node = namedtuple('Node', ['node', 'mask', 'cost'])\n\n        q = deque()\n        for i in range(n):\n            mask_value = (1 << i)\n            this_node = Node(i, mask_value, 1)\n            q.append(this_node)\n            visited.add((i, mask_value))\n\n        while q:\n            curr = q.popleft()\n\n            if curr.mask == all_mask:\n                return curr.cost - 1\n\n            for adj in graph[curr.node]:\n                both_visited_mask = curr.mask | (1 << adj)\n                this_node = Node(adj, both_visited_mask, curr.cost + 1)\n\n                if (adj, both_visited_mask) not in visited:\n                    visited.add((adj, both_visited_mask))\n                    q.append(this_node)\n\n        return -1\n","title":"Shortest Path Visiting All Nodes","url":"/submissions/detail/1051649878/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1694940338,"status":10,"runtime":"340 ms","is_pending":"Not Pending","memory":"21.4 MB","compare_result":"111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

from collections import deque, namedtuple


class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        all_mask = (1 << n) - 1
        visited = set()
        Node = namedtuple("Node", ["node", "mask", "cost"])

        q = deque()
        for i in range(n):
            mask_value = 1 << i
            this_node = Node(i, mask_value, 1)
            q.append(this_node)
            visited.add((i, mask_value))

        while q:
            curr = q.popleft()

            if curr.mask == all_mask:
                return curr.cost - 1

            for adj in graph[curr.node]:
                both_visited_mask = curr.mask | (1 << adj)
                this_node = Node(adj, both_visited_mask, curr.cost + 1)

                if (adj, both_visited_mask) not in visited:
                    visited.add((adj, both_visited_mask))
                    q.append(this_node)

        return -1
