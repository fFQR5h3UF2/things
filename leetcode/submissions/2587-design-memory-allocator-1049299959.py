# Submission for Design Memory Allocator
# Submission url: https://leetcode.com/submissions/detail/1049299959/


class Allocator:

    def __init__(self, n: int):
        self._units = [1] * n
        self._units[0] = n
        self._id_units = defaultdict(list)
        self._units_count = n

    def allocate(self, size: int, mID: int) -> int:
        i = 0
        while i < self._units_count:
            units_avail = self._units[i]
            if units_avail < 0:
                i += -units_avail
                continue
            if units_avail < size:
                i += units_avail
                continue

            self._units[i] = -size
            if units_avail > size:
                self._units[i + size] = units_avail - size
            self._id_units[mID].append(i)
            return i

        return -1

    def free(self, mID: int) -> int:
        count = 0
        conseq_units = self._id_units[mID]
        while conseq_units:
            units_start = conseq_units.pop()
            units_freed = -self._units[units_start]
            count += units_freed
            self._units[units_start] = units_freed

            units_next = units_start + units_freed
            if units_next >= self._units_count:
                continue
            units_next_val = self._units[units_next]
            if units_next_val > 0:
                self._units[units_start] += units_next_val

        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
