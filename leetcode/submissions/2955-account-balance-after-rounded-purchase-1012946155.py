# Submission for Account Balance After Rounded Purchase
# Submission url: https://leetcode.com/submissions/detail/1012946155/


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 == 0:
            return 100 - purchaseAmount

        return 100 - (((purchaseAmount // 10) + 1) * 10)
