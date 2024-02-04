# Submission for Longest Increasing Subsequence
# Submission url: https://leetcode.com/submissions/detail/1014742480/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums_count = len(nums)

        @cache
        def dp(idx: int) -> int:
            start = nums[idx]
            max_length = 0
            for i in range(idx + 1, nums_count):
                length = dp(i)
                if nums[i] > start:
                    length += 1

                if length > max_length:
                    max_length = length

            return max_length if max_length else 1

        return dp(0)
