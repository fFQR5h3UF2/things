# Submission for Design Memory Allocator
# Submission url: https://leetcode.com/submissions/detail/1049284790/


class Allocator:

    def __init__(self, n: int):
        self._units = [0] * n
        self._units[0] = -n
        self._id_units = defaultdict(list)
        self._units_count = n

    def allocate(self, size: int, mID: int) -> int:
        i = 0
        while i < self._units_count:
            val = self._units[i]
            if val == 0:
                raise Exception()
            if val > 0:
                i += val
                continue
            if -val < size:
                i -= val
                continue

            self._units[i] = size
            if -val != size:
                self._units[i + size] = val + size
            self._id_units[mID].append(i)
            return i

        return -1

    def free(self, mID: int) -> int:
        count = 0
        for unit in self._id_units[mID]:
            count += self._units[unit]
            self._units[unit] *= -1
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
