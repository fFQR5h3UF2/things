# Submission title: Remove Duplicates from Sorted List II
# Submission url  : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1057799547/
# Submission json : {"id":1057799547,"status_display":"Accepted","lang":"python3","question_id":82,"title_slug":"remove-duplicates-from-sorted-list-ii","code":"# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        tail, before_tail = head, None\n        remove_tail = False\n        while tail:\n            if tail.next and tail.val == tail.next.val:\n                tail.next = tail.next.next\n                remove_tail = True\n                continue\n            if not remove_tail:\n                before_tail, tail = tail, tail.next\n                continue\n            remove_tail = False\n            if before_tail is None:\n                tail = head.next\n                head.next, head = None, head.next\n            else:\n                before_tail.next = tail.next\n                tail = tail.next\n        return head","title":"Remove Duplicates from Sorted List II","url":"/submissions/detail/1057799547/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695548310,"status":10,"runtime":"49 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail, before_tail = head, None
        remove_tail = False
        while tail:
            if tail.next and tail.val == tail.next.val:
                tail.next = tail.next.next
                remove_tail = True
                continue
            if not remove_tail:
                before_tail, tail = tail, tail.next
                continue
            remove_tail = False
            if before_tail is None:
                tail = head.next
                head.next, head = None, head.next
            else:
                before_tail.next = tail.next
                tail = tail.next
        return head
