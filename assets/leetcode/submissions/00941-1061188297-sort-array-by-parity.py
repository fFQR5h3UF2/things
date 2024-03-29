# Submission title: Sort Array By Parity
# Submission url  : https://leetcode.com/problems/sort-array-by-parity/description/
# Submission url  : https://leetcode.com/submissions/detail/1061188297/"


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 == 1:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums
