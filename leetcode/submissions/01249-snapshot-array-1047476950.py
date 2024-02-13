# Submission title: Snapshot Array
# Submission url  : https://leetcode.com/problems/snapshot-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1047476950/
# Submission json : {"id":1047476950,"status_display":"Accepted","lang":"python3","question_id":1249,"title_slug":"snapshot-array","code":"class SnapshotArray:\n\n    def __init__(self, length: int):\n        self._cur_snap = 0\n        self._elems = [[(0, 0)] for _ in range(length)]\n\n    def set(self, index: int, val: int) -> None:\n        values = self._elems[index]\n        if values[-1][0] == self._cur_snap:\n            values.pop()\n        values.append((self._cur_snap, val))\n\n    def snap(self) -> int:\n        self._cur_snap += 1\n        return self._cur_snap - 1 \n\n    def get(self, index: int, snap_id: int) -> int:\n        for cur_snap_id, val in reversed(self._elems[index]):\n            if cur_snap_id > snap_id:\n                continue\n            return val\n        \n        return -1\n        \n\n\n# Your SnapshotArray object will be instantiated and called as such:\n# obj = SnapshotArray(length)\n# obj.set(index,val)\n# param_2 = obj.snap()\n# param_3 = obj.get(index,snap_id)","title":"Snapshot Array","url":"/submissions/detail/1047476950/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694525529,"status":10,"runtime":"3918 ms","is_pending":"Not Pending","memory":"41.8 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class SnapshotArray:

    def __init__(self, length: int):
        self._cur_snap = 0
        self._elems = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        values = self._elems[index]
        if values[-1][0] == self._cur_snap:
            values.pop()
        values.append((self._cur_snap, val))

    def snap(self) -> int:
        self._cur_snap += 1
        return self._cur_snap - 1

    def get(self, index: int, snap_id: int) -> int:
        for cur_snap_id, val in reversed(self._elems[index]):
            if cur_snap_id > snap_id:
                continue
            return val

        return -1


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
