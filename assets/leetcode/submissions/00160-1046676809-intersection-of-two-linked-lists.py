# Submission title: Intersection of Two Linked Lists
# Submission url  : https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Submission url  : https://leetcode.com/submissions/detail/1046676809/"


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
