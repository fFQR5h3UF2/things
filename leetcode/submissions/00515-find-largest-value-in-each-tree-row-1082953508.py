# Submission title: Find Largest Value in Each Tree Row
# Submission url  : https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
# Submission url  : https://leetcode.com/submissions/detail/1082953508/
# Submission json : {"id":1082953508,"status_display":"Accepted","lang":"python3","question_id":515,"title_slug":"find-largest-value-in-each-tree-row","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def largestValues(self, root: Optional[TreeNode]) -> List[int]:\n        if not root:\n            return []\n\n        largest = []\n        cur, nxt = [root], []\n        cur_val = None\n        while cur or nxt:\n            while cur:\n                node = cur.pop()\n                if cur_val is None or node.val > cur_val:\n                    cur_val = node.val\n                if node.left:\n                    nxt.append(node.left)\n                if node.right:\n                    nxt.append(node.right)\n            largest.append(cur_val)\n            cur.clear()\n            cur_val = None\n            cur, nxt = nxt, cur\n        return largest","title":"Find Largest Value in Each Tree Row","url":"/submissions/detail/1082953508/","lang_name":"Python3","time":"3 months, 1 week","timestamp":1698148515,"status":10,"runtime":"45 ms","is_pending":"Not Pending","memory":"18.7 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        largest = []
        cur, nxt = [root], []
        cur_val = None
        while cur or nxt:
            while cur:
                node = cur.pop()
                if cur_val is None or node.val > cur_val:
                    cur_val = node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            largest.append(cur_val)
            cur.clear()
            cur_val = None
            cur, nxt = nxt, cur
        return largest
