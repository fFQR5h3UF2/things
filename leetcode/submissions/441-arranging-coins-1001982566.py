# Submission for Arranging Coins
# Submission url: https://leetcode.com/submissions/detail/1001982566/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            middle = left + (right - left) // 2
            coins = middle * (middle + 1) // 2

            if coins == n:
                return middle

            if coins > h:
                right = middle - 1
            else:
                left = middle + 1

        return right
