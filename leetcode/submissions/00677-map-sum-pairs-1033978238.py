# Submission title: for Map Sum Pairs
# Submission url  : https://leetcode.com/submissions/detail/1033978238/
# Submission json : {"id": 1033978238, "status_display": "Accepted", "lang": "python3", "question_id": 677, "title_slug": "map-sum-pairs", "code": "class MapSum:\n\n    def __init__(self):\n        self._map = {}\n\n    def insert(self, key: str, val: int) -> None:\n        self._map[key] = val\n\n    def sum(self, prefix: str) -> int:\n        return sum(value for key, value in self._map.items() if key.startswith(prefix))\n\n\n# Your MapSum object will be instantiated and called as such:\n# obj = MapSum()\n# obj.insert(key,val)\n# param_2 = obj.sum(prefix)", "title": "Map Sum Pairs", "url": "/submissions/detail/1033978238/", "lang_name": "Python3", "time": "5\u00a0months, 1\u00a0week", "timestamp": 1693219078, "status": 10, "runtime": "44 ms", "is_pending": "Not Pending", "memory": "16.5 MB", "compare_result": "11111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class MapSum:

    def __init__(self):
        self._map = {}

    def insert(self, key: str, val: int) -> None:
        self._map[key] = val

    def sum(self, prefix: str) -> int:
        return sum(value for key, value in self._map.items() if key.startswith(prefix))


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
