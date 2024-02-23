# Submission title: Arranging Coins
# Submission url  : https://leetcode.com/problems/arranging-coins/description/
# Submission url  : https://leetcode.com/submissions/detail/1001972349/"


class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        row = 1
        while n >= row:
            n -= row
            row += 1
            count += 1

        return count
