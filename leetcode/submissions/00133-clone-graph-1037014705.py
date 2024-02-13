# Submission title: Clone Graph
# Submission url  : https://leetcode.com/problems/clone-graph/description/
# Submission url  : https://leetcode.com/submissions/detail/1037014705/
# Submission json : {"id":1037014705,"status_display":"Accepted","lang":"python3","question_id":133,"title_slug":"clone-graph","code":"\"\"\"\n# Definition for a Node.\nclass Node:\n    def __init__(self, val = 0, neighbors = None):\n        self.val = val\n        self.neighbors = neighbors if neighbors is not None else []\n\"\"\"\n\nclass Solution:\n    def cloneGraph(self, node: 'Node') -> 'Node':\n        old_to_new = {}\n        \n        def clone(node: Node) -> Node:\n            if node in old_to_new:\n                return old_to_new[node]\n            \n            new_node = Node(node.val)\n            old_to_new[node] = new_node\n            new_node.neighbors = [clone(neighbor) for neighbor in node.neighbors]\n\n            return new_node\n\n        return clone(node) if node else node","title":"Clone Graph","url":"/submissions/detail/1037014705/","lang_name":"Python3","time":"5 months","timestamp":1693503902,"status":10,"runtime":"49 ms","is_pending":"Not Pending","memory":"16.8 MB","compare_result":"1111111111111111111111","has_notes":false,"flag_type":1}

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        old_to_new = {}

        def clone(node: Node) -> Node:
            if node in old_to_new:
                return old_to_new[node]

            new_node = Node(node.val)
            old_to_new[node] = new_node
            new_node.neighbors = [clone(neighbor) for neighbor in node.neighbors]

            return new_node

        return clone(node) if node else node
