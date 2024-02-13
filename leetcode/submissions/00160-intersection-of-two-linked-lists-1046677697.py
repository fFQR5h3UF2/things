# Submission title: Intersection of Two Linked Lists
# Submission url  : https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Submission url  : https://leetcode.com/submissions/detail/1046677697/
# Submission json : {"id":1046677697,"status_display":"Accepted","lang":"python3","question_id":160,"title_slug":"intersection-of-two-linked-lists","code":"class Solution:\n    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:\n        if not headA or not headB:\n            return None\n        \n        tail1, tail2 = headA, headB\n        while tail1 != tail2:\n            tail1 = tail1.next if tail1 else headB\n            tail2 = tail2.next if tail2 else headA\n        \n        return tail2\n    ","title":"Intersection of Two Linked Lists","url":"/submissions/detail/1046677697/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694449935,"status":10,"runtime":"119 ms","is_pending":"Not Pending","memory":"31.8 MB","compare_result":"111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        tail1, tail2 = headA, headB
        while tail1 != tail2:
            tail1 = tail1.next if tail1 else headB
            tail2 = tail2.next if tail2 else headA

        return tail2
