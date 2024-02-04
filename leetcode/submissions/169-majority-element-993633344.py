# Submission for Majority Element
# Submission url: https://leetcode.com/submissions/detail/993633344/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, 0
        for number in nums:
            if count == 0:
                candidate = number

            if number == candidate:
                count += 0
            else:
                count -= 1

        return candidate
