# Submission title: Two Sum
# Submission url  : https://leetcode.com/problems/two-sum/description/
# Submission url  : https://leetcode.com/submissions/detail/995274303/"


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i, number in enumerate(nums):
            diff = target - number
            if diff in indexes:
                return [indexes[diff], i]
            indexes[number] = i
