# Submission title: for Binary Search Tree Iterator
# Submission url  : https://leetcode.com/submissions/detail/1047381678/
# Submission json : {"id": 1047381678, "status_display": "Accepted", "lang": "python3", "question_id": 173, "title_slug": "binary-search-tree-iterator", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass BSTIterator:\n\n    def __init__(self, root: Optional[TreeNode]):\n        self._stack = []\n        while root:\n            self._stack.append(root)\n            root = root.left\n\n    def next(self) -> int:\n        node = self._stack.pop()\n        right = node.right\n        while right:\n            self._stack.append(right)\n            right = right.left\n        \n        return node.val\n\n    def hasNext(self) -> bool:\n        return self._stack\n\n\n# Your BSTIterator object will be instantiated and called as such:\n# obj = BSTIterator(root)\n# param_1 = obj.next()\n# param_2 = obj.hasNext()", "title": "Binary Search Tree Iterator", "url": "/submissions/detail/1047381678/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694516504, "status": 10, "runtime": "73 ms", "is_pending": "Not Pending", "memory": "22.7 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._stack = []
        while root:
            self._stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self._stack.pop()
        right = node.right
        while right:
            self._stack.append(right)
            right = right.left

        return node.val

    def hasNext(self) -> bool:
        return self._stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
