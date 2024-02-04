# Submission for K-th Symbol in Grammar
# Submission url: https://leetcode.com/submissions/detail/1083659601/


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def get(row: int, column: int) -> int:
            if column == 0 or column == 1:
                return column

            half = 2 ** (row - 1)
            if column > half:
                return get(row - 1, column - half)
            return get(row - 1, column)

        return get(n - 1, k - 1)

        # 0
        # 0 1
        # 0 1 1 0
        # 0 1 1 0 1 0 0 1
        # 0 1 1 0 1 0 0 1
