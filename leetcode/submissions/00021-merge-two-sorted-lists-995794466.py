# Submission title: Merge Two Sorted Lists
# Submission url  : https://leetcode.com/problems/merge-two-sorted-lists/description/
# Submission url  : https://leetcode.com/submissions/detail/995794466/
# Submission json : {"id":995794466,"status_display":"Accepted","lang":"python3","question_id":21,"title_slug":"merge-two-sorted-lists","code":"# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\n\nclass Solution:\n    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\n        if not list1:\n            return list2\n        \n        if not list2:\n            return list1\n        \n        head = None\n        if list1.val < list2.val:\n            head, list1 = list1, list1.next \n        else:\n            head, list2 = list2, list2.next\n        \n        current = head\n        while list1 and list2:\n            if list1.val < list2.val:\n                current.next, list1 = list1, list1.next\n            else:\n                current.next, list2 = list2, list2.next\n            \n            current = current.next\n\n        if list1 or list2:\n            current.next = list1 if list1 else list2\n\n        return head","title":"Merge Two Sorted Lists","url":"/submissions/detail/995794466/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689503689,"status":10,"runtime":"51 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        head = None
        if list1.val < list2.val:
            head, list1 = list1, list1.next
        else:
            head, list2 = list2, list2.next

        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next, list1 = list1, list1.next
            else:
                current.next, list2 = list2, list2.next

            current = current.next

        if list1 or list2:
            current.next = list1 if list1 else list2

        return head
