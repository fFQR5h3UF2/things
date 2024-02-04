# Submission for Merge Two Sorted Lists
# Submission url: https://leetcode.com/submissions/detail/995786418/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        head = None
        if list1.val > list2.val:
            head, list2 = list2, list2.next
        else:
            head, list1 = list1, list1.next

        current = head
        while current:
            if not list1:
                current.next = list2
                break

            if not list2:
                current.next = list1
                break

            if list1.val > list2.val:
                current.next, list2 = list2, list2.next
                continue

            current.next, list1 = list1, list1.next

        return head
