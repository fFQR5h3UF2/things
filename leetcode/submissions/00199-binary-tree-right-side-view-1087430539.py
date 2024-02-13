# Submission title: Binary Tree Right Side View
# Submission url  : https://leetcode.com/problems/binary-tree-right-side-view/description/
# Submission url  : https://leetcode.com/submissions/detail/1087430539/
# Submission json : {"id":1087430539,"status_display":"Accepted","lang":"python3","question_id":199,"title_slug":"binary-tree-right-side-view","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:\n        if not root:\n            return []\n        \n        q_cur, q_next, answer = deque(), deque(), []\n        q_cur.append(root)\n\n        while q_cur:\n            last_val = None\n            \n            while q_cur:\n                node = q_cur.popleft()\n                last_val = node.val\n                if node.left:\n                    q_next.append(node.left)\n                if node.right:\n                    q_next.append(node.right)\n            \n            q_cur, q_next = q_next, q_cur\n            answer.append(last_val)\n    \n        return answer","title":"Binary Tree Right Side View","url":"/submissions/detail/1087430539/","lang_name":"Python3","time":"3 months, 1 week","timestamp":1698657424,"status":10,"runtime":"32 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


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

        q_cur, q_next, answer = deque(), deque(), []
        q_cur.append(root)

        while q_cur:
            last_val = None

            while q_cur:
                node = q_cur.popleft()
                last_val = node.val
                if node.left:
                    q_next.append(node.left)
                if node.right:
                    q_next.append(node.right)

            q_cur, q_next = q_next, q_cur
            answer.append(last_val)

        return answer
