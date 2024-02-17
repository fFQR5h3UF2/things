# Submission title: Leaf-Similar Trees
# Submission url  : https://leetcode.com/problems/leaf-similar-trees/description/"
# Submission url  : https://leetcode.com/submissions/detail/1141624613/"


class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
