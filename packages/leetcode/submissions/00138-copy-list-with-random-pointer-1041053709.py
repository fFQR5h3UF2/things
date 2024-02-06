# Submission title: for Copy List with Random Pointer
# Submission url  : https://leetcode.com/submissions/detail/1041053709/
# Submission json : {"id": 1041053709, "status_display": "Accepted", "lang": "python3", "question_id": 138, "title_slug": "copy-list-with-random-pointer", "code": "\"\"\"\n# Definition for a Node.\nclass Node:\n    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):\n        self.val = int(x)\n        self.next = next\n        self.random = random\n\"\"\"\n\nclass Solution:\n    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':\n        \n        copied = {None: None}\n\n        def copy_node(node: Node) -> Node:\n            if node in copied:\n                return copied[node]\n            \n            new_node = Node(node.val)\n            copied[node] = new_node\n            new_node.next = copy_node(node.next)\n            new_node.random = copy_node(node.random)\n            return new_node\n        \n        return copy_node(head)\n", "title": "Copy List with Random Pointer", "url": "/submissions/detail/1041053709/", "lang_name": "Python3", "time": "5\u00a0months", "timestamp": 1693903283, "status": 10, "runtime": "38 ms", "is_pending": "Not Pending", "memory": "17.8 MB", "compare_result": "1111111111111111111", "has_notes": false, "flag_type": 1}


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        copied = {None: None}

        def copy_node(node: Node) -> Node:
            if node in copied:
                return copied[node]

            new_node = Node(node.val)
            copied[node] = new_node
            new_node.next = copy_node(node.next)
            new_node.random = copy_node(node.random)
            return new_node

        return copy_node(head)
