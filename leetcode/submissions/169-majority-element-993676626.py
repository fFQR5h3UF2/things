# Submission for 'Majority Element'
# Submission url: https://leetcode.com/submissions/detail/993676626/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
