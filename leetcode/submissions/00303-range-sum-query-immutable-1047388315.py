# Submission title: Range Sum Query - Immutable
# Submission url  : https://leetcode.com/problems/range-sum-query-immutable/description/
# Submission url  : https://leetcode.com/submissions/detail/1047388315/
# Submission json : {"id":1047388315,"status_display":"Accepted","lang":"python3","question_id":303,"title_slug":"range-sum-query-immutable","code":"class NumArray:\n\n    def __init__(self, nums: List[int]):\n        self._nums = nums\n\n    @cache\n    def sumRange(self, left: int, right: int) -> int:\n        if right == left:\n            return self._nums[left]\n        if right - left == 1:\n            return self._nums[right] + self._nums[left]\n        mid = left + (right - left) // 2\n        return self.sumRange(left, mid) + self.sumRange(mid + 1, right)\n\n\n# Your NumArray object will be instantiated and called as such:\n# obj = NumArray(nums)\n# param_1 = obj.sumRange(left,right)","title":"Range Sum Query - Immutable","url":"/submissions/detail/1047388315/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694517173,"status":10,"runtime":"1321 ms","is_pending":"Not Pending","memory":"174.7 MB","compare_result":"111111111111111","has_notes":false,"flag_type":1}


class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums

    @cache
    def sumRange(self, left: int, right: int) -> int:
        if right == left:
            return self._nums[left]
        if right - left == 1:
            return self._nums[right] + self._nums[left]
        mid = left + (right - left) // 2
        return self.sumRange(left, mid) + self.sumRange(mid + 1, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
