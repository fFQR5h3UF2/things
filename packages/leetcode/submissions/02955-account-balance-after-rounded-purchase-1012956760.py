# Submission title: for Account Balance After Rounded Purchase
# Submission url  : https://leetcode.com/submissions/detail/1012956760/
# Submission json : {"id": 1012956760, "status_display": "Accepted", "lang": "python3", "question_id": 2955, "title_slug": "account-balance-after-rounded-purchase", "code": "class Solution:\n    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:\n        remainder = purchaseAmount % 10\n        if remainder == 0:\n            return 100 - purchaseAmount\n\n        if remainder >= 5:\n            return 100 - ((purchaseAmount // 10) + 1) * 10 \n        \n        return 100 - (purchaseAmount // 10) * 10", "title": "Account Balance After Rounded Purchase", "url": "/submissions/detail/1012956760/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1691246438, "status": 10, "runtime": "40 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        remainder = purchaseAmount % 10
        if remainder == 0:
            return 100 - purchaseAmount

        if remainder >= 5:
            return 100 - ((purchaseAmount // 10) + 1) * 10

        return 100 - (purchaseAmount // 10) * 10
