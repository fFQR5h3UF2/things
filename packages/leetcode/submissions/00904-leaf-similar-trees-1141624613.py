# Submission title: for Leaf-Similar Trees
# Submission url  : https://leetcode.com/submissions/detail/1141624613/
# Submission json : {"id": 1141624613, "status_display": "Accepted", "lang": "python3", "question_id": 904, "title_slug": "leaf-similar-trees", "code": "class Solution:\n    def leafSimilar(self, root1, root2):\n        def dfs(node):\n            if node:\n                if not node.left and not node.right:\n                    yield node.val\n                yield from dfs(node.left)\n                yield from dfs(node.right)\n\n        return list(dfs(root1)) == list(dfs(root2))", "title": "Leaf-Similar Trees", "url": "/submissions/detail/1141624613/", "lang_name": "Python3", "time": "3\u00a0weeks, 4\u00a0days", "timestamp": 1704818740, "status": 10, "runtime": "35 ms", "is_pending": "Not Pending", "memory": "17.2 MB", "compare_result": "1111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
