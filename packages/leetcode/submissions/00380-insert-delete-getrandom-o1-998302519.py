# Submission title: for Insert Delete GetRandom O(1)
# Submission url  : https://leetcode.com/submissions/detail/998302519/
# Submission json : {"id": 998302519, "status_display": "Accepted", "lang": "python3", "question_id": 380, "title_slug": "insert-delete-getrandom-o1", "code": "class RandomizedSet:\n\n    def __init__(self):\n        self._set = set()\n        self._items = []\n        self._indexes = {}\n        \n\n    def insert(self, val: int) -> bool:\n        is_in = val in self._set\n        if not is_in:\n            self._set.add(val)\n            self._items.append(val)\n            self._indexes[val] = len(self._items) - 1\n        return not is_in\n\n    def remove(self, val: int) -> bool:\n        if val not in self._set:\n            return False\n\n        last = self._items[-1]\n        val_index = self._indexes[val]\n        self._items[val_index] = last\n        self._indexes[last] = val_index\n        \n        self._set.remove(val)\n        self._items.pop()\n        self._indexes.pop(val)\n\n        return True\n\n    def getRandom(self) -> int:\n        return random.choice(self._items)\n\n\n# Your RandomizedSet object will be instantiated and called as such:\n# obj = RandomizedSet()\n# param_1 = obj.insert(val)\n# param_2 = obj.remove(val)\n# param_3 = obj.getRandom()", "title": "Insert Delete GetRandom O(1)", "url": "/submissions/detail/998302519/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689756542, "status": 10, "runtime": "363 ms", "is_pending": "Not Pending", "memory": "63.2 MB", "compare_result": "1111111111111111111", "has_notes": false, "flag_type": 1}


class RandomizedSet:

    def __init__(self):
        self._set = set()
        self._items = []
        self._indexes = {}

    def insert(self, val: int) -> bool:
        is_in = val in self._set
        if not is_in:
            self._set.add(val)
            self._items.append(val)
            self._indexes[val] = len(self._items) - 1
        return not is_in

    def remove(self, val: int) -> bool:
        if val not in self._set:
            return False

        last = self._items[-1]
        val_index = self._indexes[val]
        self._items[val_index] = last
        self._indexes[last] = val_index

        self._set.remove(val)
        self._items.pop()
        self._indexes.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self._items)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
