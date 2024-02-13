# Submission title: Design Linked List
# Submission url  : https://leetcode.com/problems/design-linked-list/description/
# Submission url  : https://leetcode.com/submissions/detail/1050221160/
# Submission json : {"id":1050221160,"status_display":"Accepted","lang":"python3","question_id":838,"title_slug":"design-linked-list","code":"class Node:\n    def __init__(self, val: int = 0, prev_node: 'Node' = None, next_node: 'Node' = None):\n        self.val, self.prev, self.next = val, prev_node, next_node\n\nclass MyLinkedList:\n\n    def __init__(self):\n        self._head, self._tail = Node(float(\"-inf\")), Node(float(\"inf\"))\n        self._head.next, self._tail.prev = self._tail, self._head\n        self._length = 0\n\n    def _getNode(self, index: int) -> Node:\n        if not 0 <= index < self._length:\n            return None\n        if index == 0:\n            return self._head.next\n        if index == self._length - 1:\n            return self._tail.prev\n\n        cur_idx, cur_node = 0, self._head.next\n        while cur_idx < index:\n            cur_node = cur_node.next\n            cur_idx += 1\n\n        return cur_node\n    \n    def get(self, index: int) -> int:\n        node = self._getNode(index)\n        return node.val if node else -1\n\n    def addAtHead(self, val: int) -> None:\n        old_first = self._head.next\n        new_node = Node(val, self._head, old_first)\n        self._head.next, old_first.prev = new_node, new_node\n        self._length += 1\n\n    def addAtTail(self, val: int) -> None:\n        old_tail = self._tail.prev\n        new_node = Node(val, old_tail, self._tail)\n        self._tail.prev, old_tail.next = new_node, new_node\n        self._length += 1\n\n    def addAtIndex(self, index: int, val: int) -> None:\n        if not 0 <= index <= self._length:\n            return\n        if index == 0:\n            self.addAtHead(val)\n            return\n        if index == self._length:\n            self.addAtTail(val)\n            return\n        \n        target_node = self._getNode(index)\n        prev_node = target_node.prev\n        new_node = Node(val, prev_node, target_node)\n        prev_node.next, target_node.prev = new_node, new_node\n        self._length += 1\n\n    def deleteAtIndex(self, index: int) -> None:\n        if not 0 <= index < self._length:\n            return\n        \n        target_node = self._getNode(index)\n        old_prev, old_next = target_node.prev, target_node.next\n        old_prev.next, old_next.prev = old_next, old_prev\n        self._length -= 1\n\n# Your MyLinkedList object will be instantiated and called as such:\n# obj = MyLinkedList()\n# param_1 = obj.get(index)\n# obj.addAtHead(val)\n# obj.addAtTail(val)\n# obj.addAtIndex(index,val)\n# obj.deleteAtIndex(index)","title":"Design Linked List","url":"/submissions/detail/1050221160/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694793179,"status":10,"runtime":"148 ms","is_pending":"Not Pending","memory":"17.9 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Node:
    def __init__(
        self, val: int = 0, prev_node: "Node" = None, next_node: "Node" = None
    ):
        self.val, self.prev, self.next = val, prev_node, next_node


class MyLinkedList:

    def __init__(self):
        self._head, self._tail = Node(float("-inf")), Node(float("inf"))
        self._head.next, self._tail.prev = self._tail, self._head
        self._length = 0

    def _getNode(self, index: int) -> Node:
        if not 0 <= index < self._length:
            return None
        if index == 0:
            return self._head.next
        if index == self._length - 1:
            return self._tail.prev

        cur_idx, cur_node = 0, self._head.next
        while cur_idx < index:
            cur_node = cur_node.next
            cur_idx += 1

        return cur_node

    def get(self, index: int) -> int:
        node = self._getNode(index)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        old_first = self._head.next
        new_node = Node(val, self._head, old_first)
        self._head.next, old_first.prev = new_node, new_node
        self._length += 1

    def addAtTail(self, val: int) -> None:
        old_tail = self._tail.prev
        new_node = Node(val, old_tail, self._tail)
        self._tail.prev, old_tail.next = new_node, new_node
        self._length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if not 0 <= index <= self._length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self._length:
            self.addAtTail(val)
            return

        target_node = self._getNode(index)
        prev_node = target_node.prev
        new_node = Node(val, prev_node, target_node)
        prev_node.next, target_node.prev = new_node, new_node
        self._length += 1

    def deleteAtIndex(self, index: int) -> None:
        if not 0 <= index < self._length:
            return

        target_node = self._getNode(index)
        old_prev, old_next = target_node.prev, target_node.next
        old_prev.next, old_next.prev = old_next, old_prev
        self._length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
