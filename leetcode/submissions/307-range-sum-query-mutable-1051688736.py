# Submission for Range Sum Query - Mutable
# Submission url: https://leetcode.com/submissions/detail/1051688736/


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = list(accumulate(nums))
        self.nums = nums
        self.length = len(nums)

    def update(self, index: int, val: int) -> None:
        self.nums[index], diff = val, val - self.nums[index]
        for i in range(index, self.length):
            self.sums[i] += diff

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
