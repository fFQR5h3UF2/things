# Submission title: Happy Number
# Submission url  : https://leetcode.com/problems/happy-number/description/"
# Submission url  : https://leetcode.com/submissions/detail/995701431/"


class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()
        while n != 1:
            if n in sums:
                return False
            sums.add(n)

            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n = n // 10
            n = sum

        return True
