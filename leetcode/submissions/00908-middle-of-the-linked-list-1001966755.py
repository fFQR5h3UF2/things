# Submission title: Middle of the Linked List
# Submission url  : https://leetcode.com/problems/middle-of-the-linked-list/description/
# Submission url  : https://leetcode.com/submissions/detail/1001966755/
# Submission json : {"id":1001966755,"status_display":"Accepted","lang":"python3","question_id":908,"title_slug":"middle-of-the-linked-list","code":"# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        middle = head.next if head else None \n        tail = middle.next if middle else None\n        move = True\n        while tail and tail.next:\n            tail = tail.next\n            if move:\n                middle = middle.next\n            \n            move = not move\n\n        return middle if middle else head\n","title":"Middle of the Linked List","url":"/submissions/detail/1001966755/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690131341,"status":10,"runtime":"40 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head.next if head else None
        tail = middle.next if middle else None
        move = True
        while tail and tail.next:
            tail = tail.next
            if move:
                middle = middle.next

            move = not move

        return middle if middle else head
