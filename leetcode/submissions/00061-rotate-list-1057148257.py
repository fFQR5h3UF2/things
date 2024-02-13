# Submission title: Rotate List
# Submission url  : https://leetcode.com/problems/rotate-list/description/
# Submission url  : https://leetcode.com/submissions/detail/1057148257/
# Submission json : {"id":1057148257,"status_display":"Accepted","lang":"python3","question_id":61,"title_slug":"rotate-list","code":"# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:\n        if k == 0 or not head:\n            return head\n        temp_head, tail, length = head, head, 0\n        while temp_head:\n            length += 1\n            tail, temp_head = temp_head, temp_head.next\n        rotation = k % length\n        if rotation == 0:\n            return head\n        new_head_idx = length - rotation\n        new_tail_idx = new_head_idx - 1 \n        i, new_head, new_tail = 0, None, None\n        temp_head = head\n        while temp_head:\n            if i == new_head_idx:\n                new_head = temp_head\n                break\n            if i == new_tail_idx:\n                new_tail = temp_head\n            i += 1\n            temp_head = temp_head.next\n        tail.next = head\n        new_tail.next = None\n        return new_head\n\n            \n","title":"Rotate List","url":"/submissions/detail/1057148257/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695481563,"status":10,"runtime":"40 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        temp_head, tail, length = head, head, 0
        while temp_head:
            length += 1
            tail, temp_head = temp_head, temp_head.next
        rotation = k % length
        if rotation == 0:
            return head
        new_head_idx = length - rotation
        new_tail_idx = new_head_idx - 1
        i, new_head, new_tail = 0, None, None
        temp_head = head
        while temp_head:
            if i == new_head_idx:
                new_head = temp_head
                break
            if i == new_tail_idx:
                new_tail = temp_head
            i += 1
            temp_head = temp_head.next
        tail.next = head
        new_tail.next = None
        return new_head
