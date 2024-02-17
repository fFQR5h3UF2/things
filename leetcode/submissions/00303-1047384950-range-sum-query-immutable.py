# Submission title: Range Sum Query - Immutable
# Submission url  : https://leetcode.com/problems/range-sum-query-immutable/description/"
# Submission url  : https://leetcode.com/submissions/detail/1047384950/"


class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self._nums[left : right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
