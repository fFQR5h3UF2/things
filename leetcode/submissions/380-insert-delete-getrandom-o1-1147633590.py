# Submission for Insert Delete GetRandom O(1)
# Submission url: https://leetcode.com/submissions/detail/1147633590/


import random


class RandomizedSet:

    def __init__(self):
        self._nums_map = {}
        self._nums = []

    def insert(self, val: int) -> bool:
        if val in self._nums_map:
            return False
        self._nums_map[val] = len(self._nums)
        self._nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._nums_map:
            return False
        last = self._nums[-1]
        idx = self._nums_map.pop(val)
        self._nums_map[last] = idx
        self._nums[idx] = last
        self._nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self._nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
