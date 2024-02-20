# Submission title: Number of Laser Beams in a Bank
# Submission url  : https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
# Submission url  : https://leetcode.com/submissions/detail/1135579756/"


class Solution:
    def numberOfBeams(self, bank):
        ans, temp = 0, 0
        for s in bank:
            n = s.count("1")
            if n == 0:
                continue
            ans += temp * n
            temp = n
        return ans
