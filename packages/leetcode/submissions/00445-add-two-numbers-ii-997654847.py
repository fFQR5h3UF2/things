# Submission title: for Add Two Numbers II
# Submission url  : https://leetcode.com/submissions/detail/997654847/
# Submission json : {"id": 997654847, "status_display": "Accepted", "lang": "python3", "question_id": 445, "title_slug": "add-two-numbers-ii", "code": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def reverse(self, head: ListNode) -> ListNode:\n        previous = None\n        while head:\n            next, head.next = head.next, previous\n            previous, head = head, next\n        return previous\n\n    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:\n        l1, l2 = self.reverse(l1), self.reverse(l2)\n        head, tail, carry = l1, l1, 0\n\n        while l1 or l2 or carry:\n            val_1 = l1.val if l1 else 0\n            val_2 = l2.val if l2 else 0\n            sum = val_1 + val_2 + carry\n            if sum > 9:\n                carry = 1\n                sum %= 10\n            else:\n                carry = 0\n\n            tail.val = sum\n            l1, l2 = l1.next if l1 else None, l2.next if l2 else None\n            if not tail.next and l2:\n                tail.next = l2\n                l1 = None\n\n            if not tail.next and carry:\n                tail.next = ListNode(carry)\n                carry = 0\n                l2 = None\n\n            if tail.next:\n                tail = tail.next\n            \n        return self.reverse(head)", "title": "Add Two Numbers II", "url": "/submissions/detail/997654847/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689692241, "status": 10, "runtime": "68 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        previous = None
        while head:
            next, head.next = head.next, previous
            previous, head = head, next
        return previous

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1, l2 = self.reverse(l1), self.reverse(l2)
        head, tail, carry = l1, l1, 0

        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            sum = val_1 + val_2 + carry
            if sum > 9:
                carry = 1
                sum %= 10
            else:
                carry = 0

            tail.val = sum
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            if not tail.next and l2:
                tail.next = l2
                l1 = None

            if not tail.next and carry:
                tail.next = ListNode(carry)
                carry = 0
                l2 = None

            if tail.next:
                tail = tail.next

        return self.reverse(head)
