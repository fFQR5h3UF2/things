# Submission title: Special Positions in a Binary Matrix
# Submission url  : https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/"
# Submission url  : https://leetcode.com/submissions/detail/1118673519/"


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def get_column_sum(col_idx):
            return sum(row[col_idx] for row in mat)

        special = 0
        for row in mat:
            if sum(row) == 1:
                col_idx = row.index(1)
                special += get_column_sum(col_idx) == 1

        return special
