# Submission title: Poor Pigs
# Submission url  : https://leetcode.com/problems/poor-pigs/description/
# Submission url  : https://leetcode.com/submissions/detail/1086938416/"


class Solution:
    def poorPigs(self, buckets: int, a: int, b: int) -> int:
        pigs = 0
        while (b / a + 1) ** pigs < buckets:
            pigs += 1

        return pigs
