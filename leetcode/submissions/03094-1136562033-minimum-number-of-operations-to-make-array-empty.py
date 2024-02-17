# Submission title: Minimum Number of Operations to Make Array Empty
# Submission url  : https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/"
# Submission url  : https://leetcode.com/submissions/detail/1136562033/"


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1:
                return -1
            ans += ceil(c / 3)
        return ans
