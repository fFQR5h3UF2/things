# Submission title: Longest Consecutive Sequence
# Submission url  : https://leetcode.com/problems/longest-consecutive-sequence/description/
# Submission url  : https://leetcode.com/submissions/detail/997539098/"


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length

        nums = set(nums)
        longest = 1
        for number in nums:
            if number - 1 in nums:
                continue
            consequent = 1
            while number + consequent in nums:
                consequent += 1
            longest = max(longest, consequent)

        return longest
