# Submission for 'Number of Even and Odd Bits'
# Submission url: https://leetcode.com/submissions/detail/1054829486/

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        return (n & 0x55555555).bit_count(), (n & 0xaaaaaaaa).bit_count()
