# Submission title: Split Linked List in Parts
# Submission url  : https://leetcode.com/problems/split-linked-list-in-parts/description/
# Submission url  : https://leetcode.com/submissions/detail/1042088778/
# Submission json : {"id":1042088778,"status_display":"Accepted","lang":"python3","question_id":725,"title_slug":"split-linked-list-in-parts","code":"class Solution:\n    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:        \n        nodes_count = 0\n        tail = head\n        while tail:\n            tail = tail.next\n            nodes_count += 1\n        \n        quotient, remainder = divmod(nodes_count, k)\n        answer = []\n        for i in range(k):\n            size = quotient + 1 if (remainder := remainder - 1) >= 0 else quotient\n\n            answer.append(head)\n            last = None\n            while size > 0:\n                last = head\n                head = head.next\n                size -= 1\n            if last: \n                last.next = None\n                \n        return answer","title":"Split Linked List in Parts","url":"/submissions/detail/1042088778/","lang_name":"Python3","time":"5 months","timestamp":1694001543,"status":10,"runtime":"39 ms","is_pending":"Not Pending","memory":"16.8 MB","compare_result":"1111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        nodes_count = 0
        tail = head
        while tail:
            tail = tail.next
            nodes_count += 1

        quotient, remainder = divmod(nodes_count, k)
        answer = []
        for i in range(k):
            size = quotient + 1 if (remainder := remainder - 1) >= 0 else quotient

            answer.append(head)
            last = None
            while size > 0:
                last = head
                head = head.next
                size -= 1
            if last:
                last.next = None

        return answer
