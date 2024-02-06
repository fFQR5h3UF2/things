# Submission title: for Populating Next Right Pointers in Each Node II
# Submission url  : https://leetcode.com/submissions/detail/1057810766/
# Submission json : {"id": 1057810766, "status_display": "Accepted", "lang": "python3", "question_id": 117, "title_slug": "populating-next-right-pointers-in-each-node-ii", "code": "from collections import deque\n\nclass Solution:\n  def connect(self, root: 'Node') -> 'Node':\n    # Edge case - If the root is None, then return None\n    if root is None:\n        return None\n    \n    # Create a queue and enqueue the root node\n    q = deque([root])\n    \n    # Traverse the tree level by level\n    while q:\n        \n        # Get the number of nodes of the current level\n        level_size = len(q)\n        \n        # Process the nodes of the current level\n        for i in range(level_size):\n            \n            # Dequeue a node from the front of the queue\n            node = q.popleft()\n            \n            # Assign the next pointer of the node\n            if i < level_size - 1:\n                node.next = q[0]\n            \n            # Enqueue the children of the node (if any)\n            if node.left is not None:\n                q.append(node.left)\n            if node.right is not None:\n                q.append(node.right)\n    \n    # Return the root node\n    return root\n", "title": "Populating Next Right Pointers in Each Node II", "url": "/submissions/detail/1057810766/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695549563, "status": 10, "runtime": "51 ms", "is_pending": "Not Pending", "memory": "17.7 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


from collections import deque


class Solution:
    def connect(self, root: "Node") -> "Node":
        # Edge case - If the root is None, then return None
        if root is None:
            return None

        # Create a queue and enqueue the root node
        q = deque([root])

        # Traverse the tree level by level
        while q:

            # Get the number of nodes of the current level
            level_size = len(q)

            # Process the nodes of the current level
            for i in range(level_size):

                # Dequeue a node from the front of the queue
                node = q.popleft()

                # Assign the next pointer of the node
                if i < level_size - 1:
                    node.next = q[0]

                # Enqueue the children of the node (if any)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

        # Return the root node
        return root
