# Submission for Sort Integers by The Number of 1 Bits
# Submission url: https://leetcode.com/submissions/detail/1087389621/


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return tuple(num for num in sorted(arr, key=lambda num: (num.bit_count(), num)))
