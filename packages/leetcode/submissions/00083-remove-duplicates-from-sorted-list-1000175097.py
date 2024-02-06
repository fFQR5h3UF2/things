# Submission title: for Remove Duplicates from Sorted List
# Submission url  : https://leetcode.com/submissions/detail/1000175097/
# Submission json : {"id": 1000175097, "status_display": "Accepted", "lang": "python3", "question_id": 83, "title_slug": "remove-duplicates-from-sorted-list", "code": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        result = head\n        \n        while head and head.next:\n            if head.next.val == head.val:\n                head.next = head.next.next\n                continue\n            \n            head = head.next\n        \n        return result", "title": "Remove Duplicates from Sorted List", "url": "/submissions/detail/1000175097/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689944372, "status": 10, "runtime": "54 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head

        while head and head.next:
            if head.next.val == head.val:
                head.next = head.next.next
                continue

            head = head.next

        return result
