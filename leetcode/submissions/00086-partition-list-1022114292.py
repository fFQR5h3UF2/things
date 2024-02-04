# Submission title: for Partition List
# Submission url  : https://leetcode.com/submissions/detail/1022114292/
# Submission json : {"id": 1022114292, "status_display": "Accepted", "lang": "python3", "question_id": 86, "title_slug": "partition-list", "code": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:\n        first_left, last_left, first_right, last_right = None, None, None, None\n\n        while head:\n            is_left = head.val < x\n            is_right = not is_left\n            next_node = head.next\n            head.next = first_right if is_left else None\n            \n            if is_left and last_left:\n                last_left.next = head\n                last_left = head\n            elif is_left and not first_left:\n                first_left, last_left = head, head\n\n            if is_right and first_right:\n                last_right.next = head\n                last_right = head\n            elif is_right and not first_right:\n                first_right, last_right = head, head\n                if last_left:\n                    last_left.next = head\n\n            head = next_node\n\n        return first_left if first_left else first_right", "title": "Partition List", "url": "/submissions/detail/1022114292/", "lang_name": "Python3", "time": "5\u00a0months, 3\u00a0weeks", "timestamp": 1692108168, "status": 10, "runtime": "52 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first_left, last_left, first_right, last_right = None, None, None, None

        while head:
            is_left = head.val < x
            is_right = not is_left
            next_node = head.next
            head.next = first_right if is_left else None

            if is_left and last_left:
                last_left.next = head
                last_left = head
            elif is_left and not first_left:
                first_left, last_left = head, head

            if is_right and first_right:
                last_right.next = head
                last_right = head
            elif is_right and not first_right:
                first_right, last_right = head, head
                if last_left:
                    last_left.next = head

            head = next_node

        return first_left if first_left else first_right
