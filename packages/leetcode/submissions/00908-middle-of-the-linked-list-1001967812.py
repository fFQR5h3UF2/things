# Submission title: for Middle of the Linked List
# Submission url  : https://leetcode.com/submissions/detail/1001967812/
# Submission json : {"id": 1001967812, "status_display": "Accepted", "lang": "python3", "question_id": 908, "title_slug": "middle-of-the-linked-list", "code": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        slow = fast = head\n        while fast and fast.next:\n            slow = slow.next\n            fast = fast.next.next\n        \n        return slow\n", "title": "Middle of the Linked List", "url": "/submissions/detail/1001967812/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690131433, "status": 10, "runtime": "50 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
