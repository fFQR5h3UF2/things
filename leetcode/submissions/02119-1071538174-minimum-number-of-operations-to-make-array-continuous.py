# Submission title: Minimum Number of Operations to Make Array Continuous
# Submission url  : https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/"
# Submission url  : https://leetcode.com/submissions/detail/1071538174/"


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))

        for i in range(len(new_nums)):
            left = new_nums[i]
            right = left + n - 1
            j = bisect_right(new_nums, right)
            count = j - i
            ans = min(ans, n - count)

        return ans
