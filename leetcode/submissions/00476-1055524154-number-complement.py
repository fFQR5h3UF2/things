# Submission title: Number Complement
# Submission url  : https://leetcode.com/problems/number-complement/description/"
# Submission url  : https://leetcode.com/submissions/detail/1055524154/"


class Solution:
    def findComplement(self, num: int) -> int:
        return ~num + (1 << num.bit_length())
