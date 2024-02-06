# Submission title: for Find Elements in a Contaminated Binary Tree
# Submission url  : https://leetcode.com/submissions/detail/1052565015/
# Submission json : {"id": 1052565015, "status_display": "Accepted", "lang": "python3", "question_id": 1387, "title_slug": "find-elements-in-a-contaminated-binary-tree", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass FindElements:\n\n    def __init__(self, root: Optional[TreeNode]):\n        self.root = root\n        root.val = 0\n        nodes = [root]\n        while nodes:\n            node = nodes.pop()\n            new_val = 2 * node.val\n            if node.left:\n                node.left.val = new_val + 1\n                nodes.append(node.left)\n            if node.right:\n                node.right.val = new_val + 2\n                nodes.append(node.right)\n\n    def dfs(self, node: TreeNode, target: int) -> bool:\n        if not node or node.val > target:\n            return False\n        if node.val == target:\n            return True\n        return self.dfs(node.left, target) or self.dfs(node.right, target)\n\n    def find(self, target: int) -> bool:\n        return self.dfs(self.root, target)\n\n# Your FindElements object will be instantiated and called as such:\n# obj = FindElements(root)\n# param_1 = obj.find(target)", "title": "Find Elements in a Contaminated Binary Tree", "url": "/submissions/detail/1052565015/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1695036888, "status": 10, "runtime": "3275 ms", "is_pending": "Not Pending", "memory": "20 MB", "compare_result": "1111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        root.val = 0
        nodes = [root]
        while nodes:
            node = nodes.pop()
            new_val = 2 * node.val
            if node.left:
                node.left.val = new_val + 1
                nodes.append(node.left)
            if node.right:
                node.right.val = new_val + 2
                nodes.append(node.right)

    def dfs(self, node: TreeNode, target: int) -> bool:
        if not node or node.val > target:
            return False
        if node.val == target:
            return True
        return self.dfs(node.left, target) or self.dfs(node.right, target)

    def find(self, target: int) -> bool:
        return self.dfs(self.root, target)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
