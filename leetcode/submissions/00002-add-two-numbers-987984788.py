# Submission title: Add Two Numbers
# Submission url  : https://leetcode.com/problems/add-two-numbers/description/
# Submission url  : https://leetcode.com/submissions/detail/987984788/
# Submission json : {"id":987984788,"status_display":"Accepted","lang":"python3","question_id":2,"title_slug":"add-two-numbers","code":"# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    # create the result pointer that points towards one of the lists\n    # create the result root pointer that will point towards the root of the result list\n    # 1. start infinite loop\n    # 2. if result is false - break, we reached the end\n    # 3. get values from non-empty pointers\n    # 4. add values together, store the carry in a variable\n    # 5. store the value in the result pointer\n    # 6. move the result pointer to the next node, if there is no next node, use a node from\n    #    another list\n    # 7. move list pointers\n    # 8. if we have a carry left, add a node to the result list\n    def addTwoNumbers(self, l1: Optional[ListNode], \n                            l2: Optional[ListNode]) -> Optional[ListNode]:\n        carry = 0\n        result, result_root = l1, l1\n\n        while True:\n            if not l1 and not l2:\n                break\n            \n            number_1 = l1.val if l1 else 0\n            number_2 = l2.val if l2 else 0\n            result_val = number_1 + number_2 + carry\n            if result_val > 9:\n                carry, result_val = 1, result_val - 10\n            else:\n                carry = 0\n            \n            result.val = result_val\n            if not result.next and l2:\n                l1 = None\n                result.next = l2.next\n\n            if result.next:\n                result = result.next\n            if l1:\n                l1 = l1.next\n            if l2:\n                l2 = l2.next\n\n        if carry:\n            result.next = ListNode(carry)\n\n        return result_root","title":"Add Two Numbers","url":"/submissions/detail/987984788/","lang_name":"Python3","time":"7 months","timestamp":1688665460,"status":10,"runtime":"83 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # create the result pointer that points towards one of the lists
    # create the result root pointer that will point towards the root of the result list
    # 1. start infinite loop
    # 2. if result is false - break, we reached the end
    # 3. get values from non-empty pointers
    # 4. add values together, store the carry in a variable
    # 5. store the value in the result pointer
    # 6. move the result pointer to the next node, if there is no next node, use a node from
    #    another list
    # 7. move list pointers
    # 8. if we have a carry left, add a node to the result list
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        result, result_root = l1, l1

        while True:
            if not l1 and not l2:
                break

            number_1 = l1.val if l1 else 0
            number_2 = l2.val if l2 else 0
            result_val = number_1 + number_2 + carry
            if result_val > 9:
                carry, result_val = 1, result_val - 10
            else:
                carry = 0

            result.val = result_val
            if not result.next and l2:
                l1 = None
                result.next = l2.next

            if result.next:
                result = result.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            result.next = ListNode(carry)

        return result_root
