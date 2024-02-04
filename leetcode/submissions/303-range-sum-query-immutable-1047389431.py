# Submission for Range Sum Query - Immutable
# Submission url: https://leetcode.com/submissions/detail/1047389431/


class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums

    @cache
    def sumRange(self, left: int, right: int) -> int:
        if right == left:
            return self._nums[left]
        if right - left == 1:
            return self._nums[left] + self._nums[right]

        return self.sumRange(left, left + 1) + self.sumRange(left + 2, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
