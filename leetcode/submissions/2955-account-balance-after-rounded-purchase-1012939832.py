# Submission for Account Balance After Rounded Purchase
# Submission url: https://leetcode.com/submissions/detail/1012939832/


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - (((purchaseAmount // 10) + 1) * 10)
