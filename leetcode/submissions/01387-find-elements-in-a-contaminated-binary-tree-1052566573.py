# Submission title: Find Elements in a Contaminated Binary Tree
# Submission url  : https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/
# Submission url  : https://leetcode.com/submissions/detail/1052566573/
# Submission json : {"id":1052566573,"status_display":"Accepted","lang":"python3","question_id":1387,"title_slug":"find-elements-in-a-contaminated-binary-tree","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass FindElements:\n\n    def __init__(self, root: Optional[TreeNode]):\n        root.val = 0\n        nodes = [root]\n        self.values = set((0, )) \n        while nodes:\n            node = nodes.pop()\n            if node.left:\n                val = 2 * node.val + 1\n                node.left.val = val\n                nodes.append(node.left)\n                self.values.add(val)\n            if node.right:\n                val = 2 * node.val + 2\n                node.right.val = val\n                nodes.append(node.right)\n                self.values.add(val)\n\n    def find(self, target: int) -> bool:\n        return target in self.values\n\n# Your FindElements object will be instantiated and called as such:\n# obj = FindElements(root)\n# param_1 = obj.find(target)","title":"Find Elements in a Contaminated Binary Tree","url":"/submissions/detail/1052566573/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695037048,"status":10,"runtime":"69 ms","is_pending":"Not Pending","memory":"20.6 MB","compare_result":"1111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        nodes = [root]
        self.values = set((0,))
        while nodes:
            node = nodes.pop()
            if node.left:
                val = 2 * node.val + 1
                node.left.val = val
                nodes.append(node.left)
                self.values.add(val)
            if node.right:
                val = 2 * node.val + 2
                node.right.val = val
                nodes.append(node.right)
                self.values.add(val)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
