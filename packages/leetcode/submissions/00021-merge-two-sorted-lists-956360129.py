# Submission title: for Merge Two Sorted Lists
# Submission url  : https://leetcode.com/submissions/detail/956360129/
# Submission json : {"id": 956360129, "status_display": "Accepted", "lang": "python3", "question_id": 21, "title_slug": "merge-two-sorted-lists", "code": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\n\nclass Solution:\n    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\n        result = ListNode()\n        current = result\n        while list1 and list2:               \n            if list1.val < list2.val:\n                current.next = list1\n                list1, current = list1.next, list1\n                continue\n\n            current.next = list2\n            list2, current = list2.next, list2\n                \n        if list1 or list2:\n            current.next = list1 if list1 else list2\n            \n        return result.next", "title": "Merge Two Sorted Lists", "url": "/submissions/detail/956360129/", "lang_name": "Python3", "time": "8\u00a0months, 2\u00a0weeks", "timestamp": 1684922070, "status": 10, "runtime": "55 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()
        current = result
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
                continue

            current.next = list2
            list2, current = list2.next, list2

        if list1 or list2:
            current.next = list1 if list1 else list2

        return result.next
