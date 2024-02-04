# Submission for 'Merge Two Sorted Lists'
# Submission url: https://leetcode.com/submissions/detail/995794466/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        head = None
        if list1.val < list2.val:
            head, list1 = list1, list1.next
        else:
            head, list2 = list2, list2.next

        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next, list1 = list1, list1.next
            else:
                current.next, list2 = list2, list2.next

            current = current.next

        if list1 or list2:
            current.next = list1 if list1 else list2

        return head
