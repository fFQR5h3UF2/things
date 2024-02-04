# Submission title: for Range Sum Query - Immutable
# Submission url  : https://leetcode.com/submissions/detail/1047394948/
# Submission json : {"id": 1047394948, "status_display": "Accepted", "lang": "python3", "question_id": 303, "title_slug": "range-sum-query-immutable", "code": "class NumArray:\n\n    def __init__(self, nums: List[int]):\n        self._sums = tuple(accumulate(nums))\n\n    def sumRange(self, left: int, right: int) -> int:\n        # [-2, 0, 3, -5, 2, -1], [-2, -2, 1, -4, -2, -3]\n        # [0, 2] -> 1\n        if left == 0:\n            return self._sums[right]\n\n        return self._sums[right] - self._sums[left-1]\n\n\n# Your NumArray object will be instantiated and called as such:\n# obj = NumArray(nums)\n# param_1 = obj.sumRange(left,right)", "title": "Range Sum Query - Immutable", "url": "/submissions/detail/1047394948/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694517838, "status": 10, "runtime": "77 ms", "is_pending": "Not Pending", "memory": "20.1 MB", "compare_result": "111111111111111", "has_notes": true, "flag_type": 1}


class NumArray:

    def __init__(self, nums: List[int]):
        self._sums = tuple(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        # [-2, 0, 3, -5, 2, -1], [-2, -2, 1, -4, -2, -3]
        # [0, 2] -> 1
        if left == 0:
            return self._sums[right]

        return self._sums[right] - self._sums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
