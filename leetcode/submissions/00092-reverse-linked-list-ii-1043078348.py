# Submission title: Reverse Linked List II
# Submission url  : https://leetcode.com/problems/reverse-linked-list-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1043078348/
# Submission json : {"id":1043078348,"status_display":"Accepted","lang":"python3","question_id":92,"title_slug":"reverse-linked-list-ii","code":"# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:\n        cur_node = 1\n        left_head, left_tail = head if left > 1 else None, None\n\n        while cur_node < left:\n            cur_node += 1\n            head, left_tail = head.next, head\n\n        cur_node += 1\n        mid_head, mid_tail, head = head, head, head.next\n        mid_head.next = None\n\n        while cur_node <= right:\n            cur_node += 1\n            mid_head, head.next, head = head, mid_head, head.next\n    \n        mid_tail.next = head\n        if left_head:\n            left_tail.next = mid_head\n        else:\n            left_head = mid_head\n\n        return left_head","title":"Reverse Linked List II","url":"/submissions/detail/1043078348/","lang_name":"Python3","time":"5 months","timestamp":1694096031,"status":10,"runtime":"33 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"11111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        cur_node = 1
        left_head, left_tail = head if left > 1 else None, None

        while cur_node < left:
            cur_node += 1
            head, left_tail = head.next, head

        cur_node += 1
        mid_head, mid_tail, head = head, head, head.next
        mid_head.next = None

        while cur_node <= right:
            cur_node += 1
            mid_head, head.next, head = head, mid_head, head.next

        mid_tail.next = head
        if left_head:
            left_tail.next = mid_head
        else:
            left_head = mid_head

        return left_head
