# Submission for Number of Beautiful Integers in the Range
# Submission url: https://leetcode.com/submissions/detail/1025903227/


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        count = 0
        for num in range(low, high + 1):
            if num % k != 0:
                continue

            even = 0
            for digit in str(num):
                even += 1 if int(digit) % 2 == 0 else -1

            if even == 0:
                count += 1

        return count
