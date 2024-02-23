# Submission title: Counting Bits
# Submission url  : https://leetcode.com/problems/counting-bits/description/
# Submission url  : https://leetcode.com/submissions/detail/1037436534/"


class Solution:
    def countBits(self, n: int) -> List[int]:
        return tuple(bin(i).count("1") for i in range(n + 1))
