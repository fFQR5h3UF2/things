# Submission title: Number of Even and Odd Bits
# Submission url  : https://leetcode.com/problems/number-of-even-and-odd-bits/description/"
# Submission url  : https://leetcode.com/submissions/detail/1054829486/"


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        return (n & 0x55555555).bit_count(), (n & 0xAAAAAAAA).bit_count()
