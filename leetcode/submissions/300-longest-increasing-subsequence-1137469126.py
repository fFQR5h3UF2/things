# Submission for Longest Increasing Subsequence
# Submission url: https://leetcode.com/submissions/detail/1137469126/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)

        @cache
        def dp(start: int) -> int:
            num = nums[start]
            max_length = 1
            for i in range(start + 1, length):
                new_num, sub_length = nums[i], dp(i)
                if new_num > num:
                    sub_length += 1
                max_length = max(max_length, sub_length)
            return max_length

        return dp(0)
