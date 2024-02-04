# Submission for Split Linked List in Parts
# Submission url: https://leetcode.com/submissions/detail/1042044665/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        heads = []

        while head and len(heads) < k:
            head.next, next_node = None, head.next
            heads.append(head)
            head = next_node

        if not head:
            return heads + [None] * (k - len(heads))

        tails = heads[:]
        nodes_count = len(tails)

        i = 0
        while head:
            if i == nodes_count:
                i = 0

            head.next, next_node = None, head.next
            tails[i], tails[i].next = head, head
            head = next_node
            i += 1

        return heads
