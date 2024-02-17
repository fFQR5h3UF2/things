# Submission title: Maximum Subarray
# Submission url  : https://leetcode.com/problems/maximum-subarray/description/"
# Submission url  : https://leetcode.com/submissions/detail/1057808298/"


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        max_cur, max_overall = 0, float("-inf")
        for num in nums:
            max_cur += num
            if max_cur > max_overall:
                max_overall = max_cur
            if max_cur < 0:
                max_cur = 0
        return max_overall
