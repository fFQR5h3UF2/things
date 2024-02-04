# Submission for Longest Increasing Subsequence
# Submission url: https://leetcode.com/submissions/detail/1137464883/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)

        @cache
        def dp(start: int) -> tuple[int, int]:
            num = nums[start]
            max_length = 1
            for i in range(start + 1, length):
                new_num, sub_length = dp(i)
                if new_num > num:
                    max_length = max(max_length, sub_length + 1)
                else:
                    max_length = max(max_length, sub_length)
            return num, max_length

        return dp(0)[1]
