# Submission title: Majority Element
# Submission url  : https://leetcode.com/problems/majority-element/description/"
# Submission url  : https://leetcode.com/submissions/detail/993634402/"


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
