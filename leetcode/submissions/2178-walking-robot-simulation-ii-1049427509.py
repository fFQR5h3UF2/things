# Submission for Walking Robot Simulation II
# Submission url: https://leetcode.com/submissions/detail/1049427509/


class Robot:

    def __init__(self, width: int, height: int):
        self._width, self._height = width, height
        self._pos = (0, 0)
        self._dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        self._cur_dir = 0
        self._dir_names = ("East", "North", "West", "South")

    def step(self, num: int) -> None:
        cur_dir = self._cur_dir
        cur_row, cur_col = self._pos
        while num > 0:
            delta_row, delta_col = self._dirs[cur_dir]
            new_row, new_col = cur_row + delta_row, cur_col + delta_col
            if not 0 <= new_row < self._height or not 0 <= new_col < self._width:
                cur_dir = cur_dir + 1 if cur_dir < 3 else 0
                continue
            cur_row, cur_col = new_row, new_col
            num -= 1

        self._cur_dir, self._pos = cur_dir, (cur_row, cur_col)

    def getPos(self) -> List[int]:
        return (self._pos[1], self._pos[0])

    def getDir(self) -> str:
        return self._dir_names[self._cur_dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
