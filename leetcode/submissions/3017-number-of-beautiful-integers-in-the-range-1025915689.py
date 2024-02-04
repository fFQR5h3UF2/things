# Submission for Number of Beautiful Integers in the Range
# Submission url: https://leetcode.com/submissions/detail/1025915689/


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        count = 0
        for num in range(low, high + 1):
            if num % k != 0:
                continue

            even = 0
            while num:
                even += 1 if (num % 10) in (0, 2, 4, 6, 8) else -1
                num //= 10

            if even == 0:
                count += 1

        return count
