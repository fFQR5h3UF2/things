# Submission for Design a Number Container System
# Submission url: https://leetcode.com/submissions/detail/1050258557/


class NumberContainers:

    def __init__(self):
        self._idx_number = {}
        self._number_idx = defaultdict(set)

    def change(self, index: int, number: int) -> None:
        cur_number = self._idx_number.get(index, -1)
        self._idx_number[index] = number
        self._number_idx[number].add(index)
        if cur_number != -1:
            self._number_idx[cur_number].discard(index)

    def find(self, number: int) -> int:
        ids = self._number_idx[number]
        return min(ids) if ids else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
