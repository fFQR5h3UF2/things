# Submission title: Design a Number Container System
# Submission url  : https://leetcode.com/problems/design-a-number-container-system/description/
# Submission url  : https://leetcode.com/submissions/detail/1050262307/
# Submission json : {"id":1050262307,"status_display":"Accepted","lang":"python3","question_id":2434,"title_slug":"design-a-number-container-system","code":"import sortedcontainers\n\nclass NumberContainers:\n\n    def __init__(self):\n        self._idx_number = {}\n        self._number_idx = defaultdict(sortedcontainers.SortedSet)\n\n    def change(self, index: int, number: int) -> None:\n        cur_number = self._idx_number.get(index, -1)\n        if cur_number != -1:\n            self._number_idx[cur_number].remove(index)\n        self._idx_number[index] = number\n        self._number_idx[number].add(index)\n\n    def find(self, number: int) -> int:\n        ids = self._number_idx[number]\n        return ids[0] if ids else -1\n\n\n# Your NumberContainers object will be instantiated and called as such:\n# obj = NumberContainers()\n# obj.change(index,number)\n# param_2 = obj.find(number)","title":"Design a Number Container System","url":"/submissions/detail/1050262307/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694796782,"status":10,"runtime":"1415 ms","is_pending":"Not Pending","memory":"156.3 MB","compare_result":"111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

import sortedcontainers


class NumberContainers:

    def __init__(self):
        self._idx_number = {}
        self._number_idx = defaultdict(sortedcontainers.SortedSet)

    def change(self, index: int, number: int) -> None:
        cur_number = self._idx_number.get(index, -1)
        if cur_number != -1:
            self._number_idx[cur_number].remove(index)
        self._idx_number[index] = number
        self._number_idx[number].add(index)

    def find(self, number: int) -> int:
        ids = self._number_idx[number]
        return ids[0] if ids else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
