# Submission title: Binary Tree Right Side View
# Submission url  : https://leetcode.com/problems/binary-tree-right-side-view/description/
# Submission url  : https://leetcode.com/submissions/detail/1087427052/
# Submission json : {"id":1087427052,"status_display":"Accepted","lang":"python3","question_id":199,"title_slug":"binary-tree-right-side-view","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:\n        if not root:\n            return []\n        cur, nxt = [root], []\n        answer = []\n        \n        while cur:\n            last_node = cur.pop()\n            if last_node.right:\n                nxt.append(last_node.right)\n            if last_node.left:\n                nxt.append(last_node.left)\n            answer.append(last_node.val)\n            \n            while cur:\n                node = cur.pop()\n                if node.right:\n                    nxt.append(node.right)\n                if node.left:\n                    nxt.append(node.left)\n            \n            cur.clear()\n            nxt.reverse()\n            cur, nxt = nxt, cur\n\n        return answer","title":"Binary Tree Right Side View","url":"/submissions/detail/1087427052/","lang_name":"Python3","time":"3 months, 1 week","timestamp":1698657034,"status":10,"runtime":"48 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        cur, nxt = [root], []
        answer = []

        while cur:
            last_node = cur.pop()
            if last_node.right:
                nxt.append(last_node.right)
            if last_node.left:
                nxt.append(last_node.left)
            answer.append(last_node.val)

            while cur:
                node = cur.pop()
                if node.right:
                    nxt.append(node.right)
                if node.left:
                    nxt.append(node.left)

            cur.clear()
            nxt.reverse()
            cur, nxt = nxt, cur

        return answer
