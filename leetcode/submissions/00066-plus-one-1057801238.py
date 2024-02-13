# Submission title: Plus One
# Submission url  : https://leetcode.com/problems/plus-one/description/
# Submission url  : https://leetcode.com/submissions/detail/1057801238/
# Submission json : {"id":1057801238,"status_display":"Accepted","lang":"python3","question_id":66,"title_slug":"plus-one","code":"class Solution:\n    def plusOne(self, digits: List[int]) -> List[int]:\n        carry = 1\n        for i in reversed(range(len(digits))):\n            new_digit = digits[i] + carry\n            if new_digit > 9:\n                carry = 1\n                new_digit %= 10\n            else:\n                carry = 0\n            digits[i] = new_digit\n        \n        if carry:\n            digits.insert(0, carry)\n        \n        return digits","title":"Plus One","url":"/submissions/detail/1057801238/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695548496,"status":10,"runtime":"46 ms","is_pending":"Not Pending","memory":"16.1 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            new_digit = digits[i] + carry
            if new_digit > 9:
                carry = 1
                new_digit %= 10
            else:
                carry = 0
            digits[i] = new_digit

        if carry:
            digits.insert(0, carry)

        return digits
