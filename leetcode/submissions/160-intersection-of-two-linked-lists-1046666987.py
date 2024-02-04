# Submission for Intersection of Two Linked Lists
# Submission url: https://leetcode.com/submissions/detail/1046666987/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        while headA and headB:
            if headA is headB:
                return headA
            headA, headB = headA.next, headB.next

        return None
