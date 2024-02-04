# Submission for Detect Squares
# Submission url: https://leetcode.com/submissions/detail/1048516632/


class DetectSquares:

    def __init__(self):
        self._row_col = defaultdict(list)
        self._col_row = defaultdict(list)

    def add(self, point: List[int]) -> None:
        row, col = point
        self._row_col[row].append(col)
        self._col_row[col].append(row)

    def count(self, point: List[int]) -> int:
        ways_count = 0
        row1, col1 = point
        for col2 in self._row_col[row1]:
            if col2 == col1:
                continue

            for row2 in self._col_row[col1]:
                if row2 == row1:
                    continue

                col1_count, col2_count = 0, 0
                for col3 in self._row_col[row2]:
                    if col3 == col1:
                        col1_count += 1
                    elif col3 == col2:
                        col2_count += 1

                ways_count += min(col1_count, col2_count)

        return ways_count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
