# Submission title: Prime Number of Set Bits in Binary Representation
# Submission url  : https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/"
# Submission url  : https://leetcode.com/submissions/detail/1056027873/"


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_bits = (2, 3, 5, 7, 11, 13, 17, 19)
        answer = 0
        for num in range(left, right + 1):
            bit_count = num.bit_count()
            if bit_count in prime_bits:
                answer += 1

        return answer
