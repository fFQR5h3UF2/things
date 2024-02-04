# Submission for Find Elements in a Contaminated Binary Tree
# Submission url: https://leetcode.com/submissions/detail/1052563124/


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

    def find(self, target: int) -> bool:
        nodes = [self.root]
        while nodes:
            node = nodes.pop()
            if node.val == target:
                return True
            if node.val > target:
                return False
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)

        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
