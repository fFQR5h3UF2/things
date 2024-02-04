# Submission for Range Sum Query - Immutable
# Submission url: https://leetcode.com/submissions/detail/1047387801/


class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums

    @cache
    def sumRange(self, left: int, right: int) -> int:
        if right == left:
            return nums[left]
        if right - left == 1:
            return nums[right] - nums[left]
        mid = left + (right - left) // 2
        return self.sumRange(left, mid) + self.sumRange(mid + 1, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
