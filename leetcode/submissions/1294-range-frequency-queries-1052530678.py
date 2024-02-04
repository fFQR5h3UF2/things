# Submission for Range Frequency Queries
# Submission url: https://leetcode.com/submissions/detail/1052530678/


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.nums = arr

    def query(self, left: int, right: int, value: int) -> int:
        count = 0
        for i in range(left, right + 1):
            if self.nums[i] == value:
                count += 1

        return count


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
