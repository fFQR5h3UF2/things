# Submission title: Plus One
# Submission url  : https://leetcode.com/problems/plus-one/description/
# Submission url  : https://leetcode.com/submissions/detail/1000160504/"


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
