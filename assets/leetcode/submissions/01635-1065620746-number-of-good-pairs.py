# Submission title: Number of Good Pairs
# Submission url  : https://leetcode.com/problems/number-of-good-pairs/description/
# Submission url  : https://leetcode.com/submissions/detail/1065620746/"


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(
            (count**2 - count) // 2
            for count in Counter(nums).values()
            if count > 1
        )
