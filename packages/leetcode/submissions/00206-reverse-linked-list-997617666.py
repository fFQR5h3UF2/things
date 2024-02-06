# Submission title: for Reverse Linked List
# Submission url  : https://leetcode.com/submissions/detail/997617666/
# Submission json : {"id": 997617666, "status_display": "Accepted", "lang": "python3", "question_id": 206, "title_slug": "reverse-linked-list", "code": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        previous = None\n        while head:\n            next, head.next = head.next, previous\n            previous, head = head, next\n\n        return previous", "title": "Reverse Linked List", "url": "/submissions/detail/997617666/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689689429, "status": 10, "runtime": "65 ms", "is_pending": "Not Pending", "memory": "17.9 MB", "compare_result": "1111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head:
            next, head.next = head.next, previous
            previous, head = head, next

        return previous
