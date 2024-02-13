# Submission title: Insert Greatest Common Divisors in Linked List
# Submission url  : https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
# Submission url  : https://leetcode.com/submissions/detail/1012983639/
# Submission json : {"id":1012983639,"status_display":"Accepted","lang":"python3","question_id":2903,"title_slug":"insert-greatest-common-divisors-in-linked-list","code":"# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        root = head\n        \n        while head and head.next:\n            next = head.next\n            new_node = ListNode(math.gcd(head.val, head.next.val), next)\n            head.next = new_node\n            head = next\n        \n        return root","title":"Insert Greatest Common Divisors in Linked List","url":"/submissions/detail/1012983639/","lang_name":"Python3","time":"6 months","timestamp":1691247204,"status":10,"runtime":"100 ms","is_pending":"Not Pending","memory":"21.2 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


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
