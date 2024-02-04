# Submission title: for Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
# Submission url  : https://leetcode.com/submissions/detail/1025739989/
# Submission json : {"id": 1025739989, "status_display": "Accepted", "lang": "python3", "question_id": 1613, "title_slug": "find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree", "code": "class Solution:\n\n    class UnionFind:\n        def __init__(self, n):\n            self.parent = list(range(n))\n            self.size = [1] * n\n            self.max_size = 1\n\n        def find(self, x):\n            # Finds the root of x\n            if x != self.parent[x]:\n                self.parent[x] = self.find(self.parent[x])\n            return self.parent[x]\n\n        def union(self, x, y):\n            # Connects x and y\n            root_x = self.find(x)\n            root_y = self.find(y)\n            if root_x != root_y:\n                if self.size[root_x] < self.size[root_y]:\n                    root_x, root_y = root_y, root_x\n                self.parent[root_y] = root_x\n                self.size[root_x] += self.size[root_y]\n                self.max_size = max(self.max_size, self.size[root_x])\n                return True\n            return False\n\n    def findCriticalAndPseudoCriticalEdges(self, n, edges):\n        new_edges = [edge.copy() for edge in edges]\n        # Add index to edges for tracking\n        for i, edge in enumerate(new_edges):\n            edge.append(i)\n        # Sort edges based on weight\n        new_edges.sort(key=lambda x: x[2])\n\n        # Find MST weight using union-find\n        uf_std = self.UnionFind(n)\n        std_weight = 0\n        for u, v, w, _ in new_edges:\n            if uf_std.union(u, v):\n                std_weight += w\n\n        # Check each edge for critical and pseudo-critical\n        critical = []\n        pseudo_critical = []\n        for (u, v, w, i) in new_edges:\n            # Ignore this edge and calculate MST weight\n            uf_ignore = self.UnionFind(n)\n            ignore_weight = 0\n            for (x, y, w_ignore, j) in new_edges:\n                if i != j and uf_ignore.union(x, y):\n                    ignore_weight += w_ignore\n            # If the graph is disconnected or the total weight is greater,\n            # the edge is critical\n            if uf_ignore.max_size < n or ignore_weight > std_weight:\n                critical.append(i)\n                continue\n\n            # Force this edge and calculate MST weight\n            uf_force = self.UnionFind(n)\n            force_weight = w\n            uf_force.union(u, v)\n            for (x, y, w_force, j) in new_edges:\n                if i != j and uf_force.union(x, y):\n                    force_weight += w_force\n            # If total weight is the same, the edge is pseudo-critical\n            if force_weight == std_weight:\n                pseudo_critical.append(i)\n\n        return [critical, pseudo_critical]", "title": "Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree", "url": "/submissions/detail/1025739989/", "lang_name": "Python3", "time": "5\u00a0months, 2\u00a0weeks", "timestamp": 1692454418, "status": 10, "runtime": "1147 ms", "is_pending": "Not Pending", "memory": "16.7 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:

    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
            self.max_size = 1

        def find(self, x):
            # Finds the root of x
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            # Connects x and y
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x != root_y:
                if self.size[root_x] < self.size[root_y]:
                    root_x, root_y = root_y, root_x
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
                self.max_size = max(self.max_size, self.size[root_x])
                return True
            return False

    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        new_edges = [edge.copy() for edge in edges]
        # Add index to edges for tracking
        for i, edge in enumerate(new_edges):
            edge.append(i)
        # Sort edges based on weight
        new_edges.sort(key=lambda x: x[2])

        # Find MST weight using union-find
        uf_std = self.UnionFind(n)
        std_weight = 0
        for u, v, w, _ in new_edges:
            if uf_std.union(u, v):
                std_weight += w

        # Check each edge for critical and pseudo-critical
        critical = []
        pseudo_critical = []
        for u, v, w, i in new_edges:
            # Ignore this edge and calculate MST weight
            uf_ignore = self.UnionFind(n)
            ignore_weight = 0
            for x, y, w_ignore, j in new_edges:
                if i != j and uf_ignore.union(x, y):
                    ignore_weight += w_ignore
            # If the graph is disconnected or the total weight is greater,
            # the edge is critical
            if uf_ignore.max_size < n or ignore_weight > std_weight:
                critical.append(i)
                continue

            # Force this edge and calculate MST weight
            uf_force = self.UnionFind(n)
            force_weight = w
            uf_force.union(u, v)
            for x, y, w_force, j in new_edges:
                if i != j and uf_force.union(x, y):
                    force_weight += w_force
            # If total weight is the same, the edge is pseudo-critical
            if force_weight == std_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
