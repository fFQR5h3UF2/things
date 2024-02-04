# Submission for 'Find the Difference'
# Submission url: https://leetcode.com/submissions/detail/1058461369/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(operator.xor, (ord(char) for char in chain(s, t))))
