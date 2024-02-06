# Submission title: for Remove Nth Node From End of List
# Submission url  : https://leetcode.com/submissions/detail/1057313158/
# Submission json : {"id": 1057313158, "status_display": "Accepted", "lang": "python3", "question_id": 19, "title_slug": "remove-nth-node-from-end-of-list", "code": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:\n        cur_length, target_length, before_removed = 0, n + 1, head\n        tail = head\n        while tail and cur_length != target_length:\n            tail = tail.next\n            cur_length += 1\n        if not tail and cur_length != target_length:\n            return head.next\n        while tail:\n            before_removed = before_removed.next\n            tail = tail.next\n        before_removed.next = before_removed.next.next\n        return head", "title": "Remove Nth Node From End of List", "url": "/submissions/detail/1057313158/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695495298, "status": 10, "runtime": "39 ms", "is_pending": "Not Pending", "memory": "16.1 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur_length, target_length, before_removed = 0, n + 1, head
        tail = head
        while tail and cur_length != target_length:
            tail = tail.next
            cur_length += 1
        if not tail and cur_length != target_length:
            return head.next
        while tail:
            before_removed = before_removed.next
            tail = tail.next
        before_removed.next = before_removed.next.next
        return head
