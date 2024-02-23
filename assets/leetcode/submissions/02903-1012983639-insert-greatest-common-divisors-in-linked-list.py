# Submission title: Insert Greatest Common Divisors in Linked List
# Submission url  : https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
# Submission url  : https://leetcode.com/submissions/detail/1012983639/"


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        root = head

        while head and head.next:
            next = head.next
            new_node = ListNode(math.gcd(head.val, head.next.val), next)
            head.next = new_node
            head = next

        return root
