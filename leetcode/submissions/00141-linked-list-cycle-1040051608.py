# Submission title: Linked List Cycle
# Submission url  : https://leetcode.com/problems/linked-list-cycle/description/
# Submission url  : https://leetcode.com/submissions/detail/1040051608/
# Submission json : {"id":1040051608,"status_display":"Accepted","lang":"python3","question_id":141,"title_slug":"linked-list-cycle","code":"# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, x):\n#         self.val = x\n#         self.next = None\n\nclass Solution:\n    def hasCycle(self, head: Optional[ListNode]) -> bool:\n        slow_p, fast_p = head, head.next if head else None\n        while fast_p and fast_p.next:\n            if slow_p == fast_p:\n                return True\n            slow_p, fast_p = slow_p.next, fast_p.next.next\n\n        return False","title":"Linked List Cycle","url":"/submissions/detail/1040051608/","lang_name":"Python3","time":"5 months","timestamp":1693809429,"status":10,"runtime":"64 ms","is_pending":"Not Pending","memory":"20.6 MB","compare_result":"11111111111111111111111","has_notes":false,"flag_type":1}

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p, fast_p = head, head.next if head else None
        while fast_p and fast_p.next:
            if slow_p == fast_p:
                return True
            slow_p, fast_p = slow_p.next, fast_p.next.next

        return False
