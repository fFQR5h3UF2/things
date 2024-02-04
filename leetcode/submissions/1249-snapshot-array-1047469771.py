# Submission for Snapshot Array
# Submission url: https://leetcode.com/submissions/detail/1047469771/


class SnapshotArray:

    def __init__(self, length: int):
        self._snap_count = 0
        self._elems = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        values = self._elems[index]
        if values[-1][0] == self._snap_count:
            values[-1] = (self._snap_count, val)
        else:
            values.append((self._snap_count, val))

    def snap(self) -> int:
        self._snap_count += 1
        return self._snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        for cur_snap_id, val in self._elems[index]:
            if cur_snap_id > snap_id:
                continue
            return val

        return -1


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
