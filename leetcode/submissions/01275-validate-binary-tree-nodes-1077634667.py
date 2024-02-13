# Submission title: Validate Binary Tree Nodes
# Submission url  : https://leetcode.com/problems/validate-binary-tree-nodes/description/
# Submission url  : https://leetcode.com/submissions/detail/1077634667/
# Submission json : {"id":1077634667,"status_display":"Accepted","lang":"python3","question_id":1275,"title_slug":"validate-binary-tree-nodes","code":"class Solution:\n    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:\n        parents = [-1] * n\n\n        for i in range(n):\n            left, right = leftChild[i], rightChild[i] \n            left_valid, right_valid = left != -1, right != -1\n            if (left_valid and parents[left] != -1) or (\n                right_valid and parents[right] != -1\n            ):\n                return False\n            if left_valid:\n                parents[left] = i\n            if right_valid:\n                parents[right] = i\n\n            parent = parents[i]\n            if parent != -1 and (parent == left or parent == right):\n                return False\n\n        root = None\n        for i, node in enumerate(parents):\n            if node == -1 and root is not None:\n                return False\n            if node == -1:\n                root = i\n\n        if root is None:\n            return False\n\n        to_visit = [root]\n        visited = set()\n\n        while to_visit:\n            node = to_visit.pop()\n            if node in visited:\n                return False\n            visited.add(node)\n            left, right = leftChild[node], rightChild[node]\n            if left != -1:\n                to_visit.append(left)\n            if right != -1:\n                to_visit.append(right)\n\n        return len(visited) == n \n        \n","title":"Validate Binary Tree Nodes","url":"/submissions/detail/1077634667/","lang_name":"Python3","time":"3 months, 2 weeks","timestamp":1697557521,"status":10,"runtime":"265 ms","is_pending":"Not Pending","memory":"18.6 MB","compare_result":"11111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        parents = [-1] * n

        for i in range(n):
            left, right = leftChild[i], rightChild[i]
            left_valid, right_valid = left != -1, right != -1
            if (left_valid and parents[left] != -1) or (
                right_valid and parents[right] != -1
            ):
                return False
            if left_valid:
                parents[left] = i
            if right_valid:
                parents[right] = i

            parent = parents[i]
            if parent != -1 and (parent == left or parent == right):
                return False

        root = None
        for i, node in enumerate(parents):
            if node == -1 and root is not None:
                return False
            if node == -1:
                root = i

        if root is None:
            return False

        to_visit = [root]
        visited = set()

        while to_visit:
            node = to_visit.pop()
            if node in visited:
                return False
            visited.add(node)
            left, right = leftChild[node], rightChild[node]
            if left != -1:
                to_visit.append(left)
            if right != -1:
                to_visit.append(right)

        return len(visited) == n
