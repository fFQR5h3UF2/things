# Submission for Max Consecutive Ones
# Submission url: https://leetcode.com/submissions/detail/1002802608/


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, count = 0, 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] == 1:
                count += 1
                continue

            if count == 1:
                count += 1

            if count > max_count:
                max_count = count

            count = 0

        return max(max_count, count)
