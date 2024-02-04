# Submission for 'Number of Steps to Reduce a Number to Zero'
# Submission url: https://leetcode.com/submissions/detail/1000093970/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            count += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1

        return count
