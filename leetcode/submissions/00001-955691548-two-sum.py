# Submission title: Two Sum
# Submission url  : https://leetcode.com/problems/two-sum/description/"
# Submission url  : https://leetcode.com/submissions/detail/955691548/"


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, number in enumerate(nums):
            for j, number_inner in enumerate(nums[i + 1 :]):
                if number + number_inner == target:
                    return [i, i + j + 1]
