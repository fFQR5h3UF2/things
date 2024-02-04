# Submission for Sqrt(x)
# Submission url: https://leetcode.com/submissions/detail/997663480/


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 1, x

        while left <= right:
            mid = left + (right - left) / 2
            square = mid * mid

            if square > x:
                right = mid - 1
            elif square == x:
                return mid
            else:
                left = mid + 1

        return int(round(right))
