# Submission title: for Design Memory Allocator
# Submission url  : https://leetcode.com/submissions/detail/1049366325/
# Submission json : {"id": 1049366325, "status_display": "Accepted", "lang": "python3", "question_id": 2587, "title_slug": "design-memory-allocator", "code": "class Allocator:\n\n    def __init__(self, n: int):\n      self._units = [1] * n\n      self._units[0] = n\n      self._id_units = defaultdict(list)\n      self._units_count = n\n\n    def find_avail_units(self, start: int, size: int) -> Tuple[int, int]:\n        i = start\n        count = 0\n        while i < self._units_count and i - start < size:\n            units_avail = self._units[i]\n            if units_avail < 0:\n                return i + units_avail if i == start else i, count\n            i += units_avail\n            count += units_avail\n\n        return i, count\n            \n\n    def allocate(self, size: int, mID: int) -> int:\n        i = 0\n        units_start, units_count = None, 0\n        while i < self._units_count and units_count < size:\n            units_avail = self._units[i]\n            if units_avail < 0:\n                i += -units_avail\n                units_start, units_count = None, 0\n                continue\n\n            if units_start is None:\n                units_start = i\n            units_count += units_avail\n            i += units_avail\n\n        if units_count < size:\n            return -1 \n\n        self._units[units_start] = -size\n        if units_count > size:\n            self._units[units_start + size] = units_count - size\n        self._id_units[mID].append(units_start)\n        return units_start\n\n    def free(self, mID: int) -> int:\n        count = 0\n        conseq_units = self._id_units[mID]\n        while conseq_units:\n            units_start = conseq_units.pop()\n            units_freed = -self._units[units_start]\n            count += units_freed\n            self._units[units_start] = units_freed\n\n        return count\n\n\n# Your Allocator object will be instantiated and called as such:\n# obj = Allocator(n)\n# param_1 = obj.allocate(size,mID)\n# param_2 = obj.free(mID)", "title": "Design Memory Allocator", "url": "/submissions/detail/1049366325/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694704090, "status": 10, "runtime": "139 ms", "is_pending": "Not Pending", "memory": "17 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Allocator:

    def __init__(self, n: int):
        self._units = [1] * n
        self._units[0] = n
        self._id_units = defaultdict(list)
        self._units_count = n

    def find_avail_units(self, start: int, size: int) -> Tuple[int, int]:
        i = start
        count = 0
        while i < self._units_count and i - start < size:
            units_avail = self._units[i]
            if units_avail < 0:
                return i + units_avail if i == start else i, count
            i += units_avail
            count += units_avail

        return i, count

    def allocate(self, size: int, mID: int) -> int:
        i = 0
        units_start, units_count = None, 0
        while i < self._units_count and units_count < size:
            units_avail = self._units[i]
            if units_avail < 0:
                i += -units_avail
                units_start, units_count = None, 0
                continue

            if units_start is None:
                units_start = i
            units_count += units_avail
            i += units_avail

        if units_count < size:
            return -1

        self._units[units_start] = -size
        if units_count > size:
            self._units[units_start + size] = units_count - size
        self._id_units[mID].append(units_start)
        return units_start

    def free(self, mID: int) -> int:
        count = 0
        conseq_units = self._id_units[mID]
        while conseq_units:
            units_start = conseq_units.pop()
            units_freed = -self._units[units_start]
            count += units_freed
            self._units[units_start] = units_freed

        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
