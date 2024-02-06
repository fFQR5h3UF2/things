# Submission title: for Unique Binary Search Trees II
# Submission url  : https://leetcode.com/submissions/detail/1012746905/
# Submission json : {"id": 1012746905, "status_display": "Accepted", "lang": "python3", "question_id": 95, "title_slug": "unique-binary-search-trees-ii", "code": "class Solution:\n    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:\n        @cache\n        def generate_trees(l, r):\n            return [None] if l > r else [\n                TreeNode(val, left, right)\n                for val in range(l, r + 1)\n                for left in generate_trees(l, val - 1)\n                for right in generate_trees(val + 1, r)\n            ]\n        \n        return generate_trees(1, n)", "title": "Unique Binary Search Trees II", "url": "/submissions/detail/1012746905/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1691228380, "status": 10, "runtime": "45 ms", "is_pending": "Not Pending", "memory": "17.2 MB", "compare_result": "11111111", "has_notes": false, "flag_type": 1}


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def generate_trees(l, r):
            return (
                [None]
                if l > r
                else [
                    TreeNode(val, left, right)
                    for val in range(l, r + 1)
                    for left in generate_trees(l, val - 1)
                    for right in generate_trees(val + 1, r)
                ]
            )

        return generate_trees(1, n)
