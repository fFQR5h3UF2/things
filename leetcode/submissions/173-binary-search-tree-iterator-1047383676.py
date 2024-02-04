# Submission for 'Binary Search Tree Iterator'
# Submission url: https://leetcode.com/submissions/detail/1047383676/

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
        return not self._next is None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
