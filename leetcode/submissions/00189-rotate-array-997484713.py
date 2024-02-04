# Submission for Rotate Array
# Submission url: https://leetcode.com/submissions/detail/997484713/


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        nums[length - k :] = nums[length - k :][::-1]
        nums[: length - k] = nums[: length - k][::-1]
        nums[:] = nums[::-1]
