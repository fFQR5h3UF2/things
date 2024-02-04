# Submission for K-th Symbol in Grammar
# Submission url: https://leetcode.com/submissions/detail/1083641285/


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cur, nxt = [0], []
        cur_row = 1

        while cur_row <= n:
            for num in cur:
                if num == 0:
                    nxt.extend((0, 1))
                else:
                    nxt.extend((1, 0))
            cur.clear()
            cur_row += 1
            cur, nxt = nxt, cur

        return cur[k - 1]
