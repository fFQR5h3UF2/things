# Submission title: for Binary Search Tree Iterator
# Submission url  : https://leetcode.com/submissions/detail/1047383991/
# Submission json : {"id": 1047383991, "status_display": "Accepted", "lang": "python3", "question_id": 173, "title_slug": "binary-search-tree-iterator", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass BSTIterator:\n\n    def __init__(self, root: Optional[TreeNode]):\n        def generate(node: TreeNode) -> int:\n            if not node:\n                return\n            yield from generate(node.left)\n            yield node\n            yield from generate(node.right)\n\n        self._generate = generate(root)\n        self._next = next(self._generate)\n\n    def next(self) -> int:\n        next_val = self._next.val\n        self._next = next(self._generate, None)\n        return next_val \n\n    def hasNext(self) -> bool:\n        return self._next is not None\n\n\n# Your BSTIterator object will be instantiated and called as such:\n# obj = BSTIterator(root)\n# param_1 = obj.next()\n# param_2 = obj.hasNext()", "title": "Binary Search Tree Iterator", "url": "/submissions/detail/1047383991/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694516744, "status": 10, "runtime": "77 ms", "is_pending": "Not Pending", "memory": "22.8 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def generate(node: TreeNode) -> int:
            if not node:
                return
            yield from generate(node.left)
            yield node
            yield from generate(node.right)

        self._generate = generate(root)
        self._next = next(self._generate)

    def next(self) -> int:
        next_val = self._next.val
        self._next = next(self._generate, None)
        return next_val

    def hasNext(self) -> bool:
        return self._next is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
