# Submission for 'Find the Duplicate Number'
# Submission url: https://leetcode.com/submissions/detail/1053766402/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freqs = [0] * (10**5 + 1)
        for num in nums:
            freqs[num] += 1
            if freqs[num] > 1:
                return num

        raise Exception()
