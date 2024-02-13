# Submission title: Amount of Time for Binary Tree to Be Infected
# Submission url  : https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/
# Submission url  : https://leetcode.com/submissions/detail/1142229574/
# Submission json : {"id":1142229574,"status_display":"Accepted","lang":"python3","question_id":2461,"title_slug":"amount-of-time-for-binary-tree-to-be-infected","code":"class Solution:\n    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:\n        def dfs(node):\n            if node is None:\n                return\n            if node.left:\n                graph[node.val].append(node.left.val)\n                graph[node.left.val].append(node.val)\n            if node.right:\n                graph[node.val].append(node.right.val)\n                graph[node.right.val].append(node.val)\n            dfs(node.left)\n            dfs(node.right)\n\n        graph = defaultdict(list)\n        dfs(root)\n        visited = set()\n        queue = deque([start])\n        time = -1\n        while queue:\n            time += 1\n            for _ in range(len(queue)):\n                current_node = queue.popleft()\n                visited.add(current_node)\n                for neighbor in graph[current_node]:\n                    if neighbor not in visited:\n                        queue.append(neighbor)\n        return time","title":"Amount of Time for Binary Tree to Be Infected","url":"/submissions/detail/1142229574/","lang_name":"Python3","time":"3 weeks, 4 days","timestamp":1704875666,"status":10,"runtime":"414 ms","is_pending":"Not Pending","memory":"63.1 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)
        visited = set()
        queue = deque([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time
