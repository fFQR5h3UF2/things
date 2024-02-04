# Submission for Find the Duplicate Number
# Submission url: https://leetcode.com/submissions/detail/1053767971/


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freqs = [False] * (10**5 + 1)
        for num in nums:
            if freqs[num] == True:
                return num
            freqs[num] = True

        raise Exception()
