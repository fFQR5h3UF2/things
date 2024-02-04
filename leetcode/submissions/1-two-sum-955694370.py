# Submission for 'Two Sum'
# Submission url: https://leetcode.com/submissions/detail/955694370/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i, number in enumerate(nums):
            diff = target - number
            if diff in indexes:
                return [indexes[diff], i]
            indexes[number] = i
