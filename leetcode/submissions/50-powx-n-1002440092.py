# Submission for Pow(x, n)
# Submission url: https://leetcode.com/submissions/detail/1002440092/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1

        while n:
            if n > 0:
                result *= x
                n -= 1
                continue

            result /= x
            n += 1

        return result

    def pow(self, x: float, n: int) -> float:
        pass
