# Submission title: for Range Sum Query - Immutable
# Submission url  : https://leetcode.com/submissions/detail/1047384950/
# Submission json : {"id": 1047384950, "status_display": "Accepted", "lang": "python3", "question_id": 303, "title_slug": "range-sum-query-immutable", "code": "class NumArray:\n\n    def __init__(self, nums: List[int]):\n        self._nums = nums\n\n    def sumRange(self, left: int, right: int) -> int:\n        return sum(self._nums[left:right+1])\n\n\n# Your NumArray object will be instantiated and called as such:\n# obj = NumArray(nums)\n# param_1 = obj.sumRange(left,right)", "title": "Range Sum Query - Immutable", "url": "/submissions/detail/1047384950/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694516837, "status": 10, "runtime": "1025 ms", "is_pending": "Not Pending", "memory": "19.9 MB", "compare_result": "111111111111111", "has_notes": true, "flag_type": 1}


class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self._nums[left : right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
