# Submission title: for Design HashMap
# Submission url  : https://leetcode.com/submissions/detail/1066538268/
# Submission json : {"id": 1066538268, "status_display": "Accepted", "lang": "python3", "question_id": 817, "title_slug": "design-hashmap", "code": "class MyHashMap:\n    def __init__(self):\n        self.data = [None] * 1000001\n\n    def put(self, key: int, val: int) -> None:\n        self.data[key] = val\n        \n    def get(self, key: int) -> int:\n        val = self.data[key]\n        return -1 if val is None else val\n\n    def remove(self, key: int) -> None:\n        self.data[key] = None\n        \n\n\n# Your MyHashMap object will be instantiated and called as such:\n# obj = MyHashMap()\n# obj.put(key,value)\n# param_2 = obj.get(key)\n# obj.remove(key)", "title": "Design HashMap", "url": "/submissions/detail/1066538268/", "lang_name": "Python3", "time": "4\u00a0months", "timestamp": 1696399045, "status": 10, "runtime": "286 ms", "is_pending": "Not Pending", "memory": "41.9 MB", "compare_result": "111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class MyHashMap:
    def __init__(self):
        self.data = [None] * 1000001

    def put(self, key: int, val: int) -> None:
        self.data[key] = val

    def get(self, key: int) -> int:
        val = self.data[key]
        return -1 if val is None else val

    def remove(self, key: int) -> None:
        self.data[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
