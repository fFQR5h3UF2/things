# Submission title: Simple Bank System
# Submission url  : https://leetcode.com/problems/simple-bank-system/description/
# Submission url  : https://leetcode.com/submissions/detail/1050716326/
# Submission json : {"id":1050716326,"status_display":"Accepted","lang":"python3","question_id":2169,"title_slug":"simple-bank-system","code":"class Bank:\n\n    def __init__(self, balance: List[int]):\n        self.balance = balance\n        self.size = len(balance)\n\n    def transfer(self, account1: int, account2: int, money: int) -> bool:\n        if not 0 < account1 <= self.size or not 0 < account2 <= self.size or (\n            self.balance[account1-1] < money\n        ):\n            return False\n        self.balance[account2-1] += money\n        self.balance[account1-1] -= money\n        return True\n\n    def deposit(self, account: int, money: int) -> bool:\n        if not 0 < account <= self.size:\n            return False\n        self.balance[account-1] += money\n        return True\n\n    def withdraw(self, account: int, money: int) -> bool:\n        if not 0 < account <= self.size or self.balance[account-1] < money:\n            return False\n        self.balance[account-1] -= money\n        return True\n\n\n# Your Bank object will be instantiated and called as such:\n# obj = Bank(balance)\n# param_1 = obj.transfer(account1,account2,money)\n# param_2 = obj.deposit(account,money)\n# param_3 = obj.withdraw(account,money)","title":"Simple Bank System","url":"/submissions/detail/1050716326/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694853351,"status":10,"runtime":"590 ms","is_pending":"Not Pending","memory":"46.2 MB","compare_result":"11111111111111111111111","has_notes":false,"flag_type":1}


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.size = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            not 0 < account1 <= self.size
            or not 0 < account2 <= self.size
            or (self.balance[account1 - 1] < money)
        ):
            return False
        self.balance[account2 - 1] += money
        self.balance[account1 - 1] -= money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not 0 < account <= self.size:
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not 0 < account <= self.size or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
