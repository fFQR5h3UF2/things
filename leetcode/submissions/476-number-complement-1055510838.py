# Submission for Number Complement
# Submission url: https://leetcode.com/submissions/detail/1055510838/


class Solution:
    def findComplement(self, num: int) -> int:
        answer = 0
        while num:
            answer = (answer << 1) | ((num & 1) ^ 1)
            num >>= 1

        return answer
