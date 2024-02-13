# Submission title: Linked List Cycle
# Submission url  : https://leetcode.com/problems/linked-list-cycle/description/
# Submission url  : https://leetcode.com/submissions/detail/995769608/
# Submission json : {"id":995769608,"status_display":"Accepted","lang":"python3","question_id":141,"title_slug":"linked-list-cycle","code":"# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, x):\n#         self.val = x\n#         self.next = None\n\nclass Solution:\n    def hasCycle(self, head: Optional[ListNode]) -> bool:\n        slow_p, fast_p = head, head.next if head else None\n        while slow_p and fast_p:\n            if slow_p == fast_p:\n                return True\n            slow_p = slow_p.next\n            fast_p = fast_p.next if fast_p else None\n            fast_p = fast_p.next if fast_p else None\n        \n        return False","title":"Linked List Cycle","url":"/submissions/detail/995769608/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689501061,"status":10,"runtime":"79 ms","is_pending":"Not Pending","memory":"20.3 MB","compare_result":"11111111111111111111111","has_notes":false,"flag_type":1}

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p, fast_p = head, head.next if head else None
        while slow_p and fast_p:
            if slow_p == fast_p:
                return True
            slow_p = slow_p.next
            fast_p = fast_p.next if fast_p else None
            fast_p = fast_p.next if fast_p else None

        return False
