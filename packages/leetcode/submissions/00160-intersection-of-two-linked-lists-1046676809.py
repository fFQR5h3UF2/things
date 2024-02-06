# Submission title: for Intersection of Two Linked Lists
# Submission url  : https://leetcode.com/submissions/detail/1046676809/
# Submission json : {"id": 1046676809, "status_display": "Accepted", "lang": "python3", "question_id": 160, "title_slug": "intersection-of-two-linked-lists", "code": "class Solution:\n    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:\n        if headA and headB:\n            A, B = headA, headB\n            while A != B:\n                A = A.next if A else headB\n                B = B.next if B else headA\n            return B\n        ", "title": "Intersection of Two Linked Lists", "url": "/submissions/detail/1046676809/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694449871, "status": 10, "runtime": "130 ms", "is_pending": "Not Pending", "memory": "31.4 MB", "compare_result": "111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if headA and headB:
            A, B = headA, headB
            while A != B:
                A = A.next if A else headB
                B = B.next if B else headA
            return B
