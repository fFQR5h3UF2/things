# Submission title: Partition List
# Submission url  : https://leetcode.com/problems/partition-list/description/
# Submission url  : https://leetcode.com/submissions/detail/1022117762/
# Submission json : {"id":1022117762,"status_display":"Accepted","lang":"python3","question_id":86,"title_slug":"partition-list","code":"# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:\n        before_head, after_head = ListNode(0), ListNode(0)\n        before_tail, after_tail = before_head, after_head\n        \n        while head: \n            if head.val < x:\n                before_tail.next, before_tail = head, head\n            else:\n                after_tail.next, after_tail = head, head\n            head = head.next\n        \n        after_tail.next, before_tail.next = None, after_head.next\n        \n        return before_head.next","title":"Partition List","url":"/submissions/detail/1022117762/","lang_name":"Python3","time":"5 months, 3 weeks","timestamp":1692108409,"status":10,"runtime":"42 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head, after_head = ListNode(0), ListNode(0)
        before_tail, after_tail = before_head, after_head

        while head:
            if head.val < x:
                before_tail.next, before_tail = head, head
            else:
                after_tail.next, after_tail = head, head
            head = head.next

        after_tail.next, before_tail.next = None, after_head.next

        return before_head.next
