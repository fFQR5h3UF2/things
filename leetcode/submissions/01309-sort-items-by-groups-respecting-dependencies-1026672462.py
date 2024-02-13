# Submission title: Sort Items by Groups Respecting Dependencies
# Submission url  : https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/
# Submission url  : https://leetcode.com/submissions/detail/1026672462/
# Submission json : {"id":1026672462,"status_display":"Accepted","lang":"python3","question_id":1309,"title_slug":"sort-items-by-groups-respecting-dependencies","code":"class Solution:\n    def sortItems(self, n, m, group, beforeItems):\n        # If an item belongs to zero group, assign it a unique group id.\n        group_id = m\n        for i in range(n):\n            if group[i] == -1:\n                group[i] = group_id\n                group_id += 1\n        \n        # Sort all item regardless of group dependencies.\n        item_graph = [[] for _ in range(n)]\n        item_indegree = [0] * n\n        \n        # Sort all groups regardless of item dependencies.\n        group_graph = [[] for _ in range(group_id)]\n        group_indegree = [0] * group_id      \n        \n        for curr in range(n):\n            for prev in beforeItems[curr]:\n                # Each (prev -> curr) represents an edge in the item graph.\n                item_graph[prev].append(curr)\n                item_indegree[curr] += 1\n                \n                # If they belong to different groups, add an edge in the group graph.\n                if group[curr] != group[prev]:\n                    group_graph[group[prev]].append(group[curr])\n                    group_indegree[group[curr]] += 1      \n        \n        # Tologlogical sort nodes in graph, return [] if a cycle exists.\n        def topologicalSort(graph, indegree):\n            visited = []\n            stack = [node for node in range(len(graph)) if indegree[node] == 0]\n            while stack:\n                cur = stack.pop()\n                visited.append(cur)\n                for neib in graph[cur]:\n                    indegree[neib] -= 1\n                    if indegree[neib] == 0:\n                        stack.append(neib)\n            return visited if len(visited) == len(graph) else []\n\n        item_order = topologicalSort(item_graph, item_indegree)\n        group_order = topologicalSort(group_graph, group_indegree)\n        \n        if not item_order or not group_order: \n            return []\n        \n        # Items are sorted regardless of groups, we need to \n        # differentiate them by the groups they belong to.\n        ordered_groups = collections.defaultdict(list)\n        for item in item_order:\n            ordered_groups[group[item]].append(item)\n        \n        # Concatenate sorted items in all sorted groups.\n        # [group 1, group 2, ... ] -> [(item 1, item 2, ...), (item 1, item 2, ...), ...]\n        answer = []\n        for group_index in group_order:\n            answer += ordered_groups[group_index]\n        return answer","title":"Sort Items by Groups Respecting Dependencies","url":"/submissions/detail/1026672462/","lang_name":"Python3","time":"5 months, 2 weeks","timestamp":1692531281,"status":10,"runtime":"352 ms","is_pending":"Not Pending","memory":"35.6 MB","compare_result":"11111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def sortItems(self, n, m, group, beforeItems):
        # If an item belongs to zero group, assign it a unique group id.
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        # Sort all item regardless of group dependencies.
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        # Sort all groups regardless of item dependencies.
        group_graph = [[] for _ in range(group_id)]
        group_indegree = [0] * group_id

        for curr in range(n):
            for prev in beforeItems[curr]:
                # Each (prev -> curr) represents an edge in the item graph.
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                # If they belong to different groups, add an edge in the group graph.
                if group[curr] != group[prev]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        # Tologlogical sort nodes in graph, return [] if a cycle exists.
        def topologicalSort(graph, indegree):
            visited = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                cur = stack.pop()
                visited.append(cur)
                for neib in graph[cur]:
                    indegree[neib] -= 1
                    if indegree[neib] == 0:
                        stack.append(neib)
            return visited if len(visited) == len(graph) else []

        item_order = topologicalSort(item_graph, item_indegree)
        group_order = topologicalSort(group_graph, group_indegree)

        if not item_order or not group_order:
            return []

        # Items are sorted regardless of groups, we need to
        # differentiate them by the groups they belong to.
        ordered_groups = collections.defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        # Concatenate sorted items in all sorted groups.
        # [group 1, group 2, ... ] -> [(item 1, item 2, ...), (item 1, item 2, ...), ...]
        answer = []
        for group_index in group_order:
            answer += ordered_groups[group_index]
        return answer
