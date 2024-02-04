# Submission for 'Minimum Changes To Make Alternating Binary String'
# Submission url: https://leetcode.com/submissions/detail/1127327445/

class Solution:
    def minOperations(self, s: str) -> int:
        start0 = 0
        start1 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    start1 += 1
                else:
                    start0 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1

        return min(start0, start1)
