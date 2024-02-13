# Submission title: Design an ATM Machine
# Submission url  : https://leetcode.com/problems/design-an-atm-machine/description/
# Submission url  : https://leetcode.com/submissions/detail/1049394271/
# Submission json : {"id":1049394271,"status_display":"Accepted","lang":"python3","question_id":2352,"title_slug":"design-an-atm-machine","code":"class ATM:\n\n    def __init__(self):\n        self._banknotes = (0, ) * 5\n        self._values = (20, 50, 100, 200, 500)\n\n    def deposit(self, banknotesCount: List[int]) -> None:\n        self._banknotes = tuple(banknotesCount[i] + self._banknotes[i] for i in range(5))\n\n    def withdraw(self, amount: int) -> List[int]:\n        withdrawn = [0] * 5\n        for i in reversed(range(5)):\n            value, notes_left = self._values[i], self._banknotes[i]\n            notes_need = min(notes_left, amount // value)\n            \n            if notes_need == 0:\n                continue\n            \n            amount -= value * notes_need\n            withdrawn[i] = notes_need\n\n            if amount == 0:\n                self._banknotes = tuple(self._banknotes[i] - withdrawn[i] \n                                        for i in range(5))\n                return withdrawn\n\n        return (-1, )\n\n\n# Your ATM object will be instantiated and called as such:\n# obj = ATM()\n# obj.deposit(banknotesCount)\n# param_2 = obj.withdraw(amount)","title":"Design an ATM Machine","url":"/submissions/detail/1049394271/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694706267,"status":10,"runtime":"605 ms","is_pending":"Not Pending","memory":"19.9 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class ATM:

    def __init__(self):
        self._banknotes = (0,) * 5
        self._values = (20, 50, 100, 200, 500)

    def deposit(self, banknotesCount: List[int]) -> None:
        self._banknotes = tuple(
            banknotesCount[i] + self._banknotes[i] for i in range(5)
        )

    def withdraw(self, amount: int) -> List[int]:
        withdrawn = [0] * 5
        for i in reversed(range(5)):
            value, notes_left = self._values[i], self._banknotes[i]
            notes_need = min(notes_left, amount // value)

            if notes_need == 0:
                continue

            amount -= value * notes_need
            withdrawn[i] = notes_need

            if amount == 0:
                self._banknotes = tuple(
                    self._banknotes[i] - withdrawn[i] for i in range(5)
                )
                return withdrawn

        return (-1,)


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
