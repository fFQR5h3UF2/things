# Submission for Third Maximum Number
# Submission url: https://leetcode.com/submissions/detail/1002518030/


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        number_max = nums[0]
        count = 1
        for i in range(1, len(nums)):
            number = nums[i]
            if number == nums[i - 1]:
                continue

            count += 1

            if count == 3:
                return number

        return number_max
