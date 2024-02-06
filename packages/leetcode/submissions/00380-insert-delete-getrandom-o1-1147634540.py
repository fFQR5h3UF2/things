# Submission title: for Insert Delete GetRandom O(1)
# Submission url  : https://leetcode.com/submissions/detail/1147634540/
# Submission json : {"id": 1147634540, "status_display": "Accepted", "lang": "python3", "question_id": 380, "title_slug": "insert-delete-getrandom-o1", "code": "import random\n\nclass RandomizedSet:\n\n    def __init__(self):\n        self._nums_map = {}\n        self._nums = []\n        \n\n    def insert(self, val: int) -> bool:\n        if val in self._nums_map:\n            return False\n        self._nums_map[val] = len(self._nums)\n        self._nums.append(val)\n        return True\n\n    def remove(self, val: int) -> bool:\n        if val not in self._nums_map:\n            return False\n        last = self._nums[-1]\n        idx = self._nums_map[val]\n        self._nums_map[last] = idx\n        self._nums[idx] = last\n        self._nums.pop()\n        self._nums_map.pop(val)\n        return True\n        \n    def getRandom(self) -> int:\n        return random.choice(self._nums) \n\n\n# Your RandomizedSet object will be instantiated and called as such:\n# obj = RandomizedSet()\n# param_1 = obj.insert(val)\n# param_2 = obj.remove(val)\n# param_3 = obj.getRandom()", "title": "Insert Delete GetRandom O(1)", "url": "/submissions/detail/1147634540/", "lang_name": "Python3", "time": "2\u00a0weeks, 5\u00a0days", "timestamp": 1705392241, "status": 10, "runtime": "259 ms", "is_pending": "Not Pending", "memory": "64.3 MB", "compare_result": "1111111111111111111", "has_notes": false, "flag_type": 1}


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
        idx = self._nums_map[val]
        self._nums_map[last] = idx
        self._nums[idx] = last
        self._nums.pop()
        self._nums_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self._nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
