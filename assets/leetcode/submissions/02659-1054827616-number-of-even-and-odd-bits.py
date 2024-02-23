# Submission title: Number of Even and Odd Bits
# Submission url  : https://leetcode.com/problems/number-of-even-and-odd-bits/description/
# Submission url  : https://leetcode.com/submissions/detail/1054827616/"


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = n & 0x55555555, n & 0xAAAAAAAA
        even_count, odd_count = 0, 0
        while even:
            if even & 1 == 1:
                even_count += 1
            even >>= 1

        while odd:
            if odd & 1 == 1:
                odd_count += 1
            odd >>= 1

        return even_count, odd_count
