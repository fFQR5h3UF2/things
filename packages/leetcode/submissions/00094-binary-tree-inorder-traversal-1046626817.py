# Submission title: for Binary Tree Inorder Traversal
# Submission url  : https://leetcode.com/submissions/detail/1046626817/
# Submission json : {"id": 1046626817, "status_display": "Accepted", "lang": "python3", "question_id": 94, "title_slug": "binary-tree-inorder-traversal", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:\n        def get_nodes(root: TreeNode) -> Generator[None, None, TreeNode]:\n            if not root:\n                return\n\n            if root.left:\n                yield from get_nodes(root.left)\n            \n            yield root.val\n\n            if root.right:\n                yield from get_nodes(root.right)\n        \n        return tuple(get_nodes(root))", "title": "Binary Tree Inorder Traversal", "url": "/submissions/detail/1046626817/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694446255, "status": 10, "runtime": "41 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def get_nodes(root: TreeNode) -> Generator[None, None, TreeNode]:
            if not root:
                return

            if root.left:
                yield from get_nodes(root.left)

            yield root.val

            if root.right:
                yield from get_nodes(root.right)

        return tuple(get_nodes(root))
