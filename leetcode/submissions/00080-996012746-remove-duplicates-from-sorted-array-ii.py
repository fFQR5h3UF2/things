# Submission title: Remove Duplicates from Sorted Array II
# Submission url  : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/"
# Submission url  : https://leetcode.com/submissions/detail/996012746/"


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)

        if length < 2:
            return length

        current_index = 2

        for number in nums[2:]:
            if number == nums[current_index - 2]:
                continue

            nums[current_index] = number
            current_index += 1

        return current_index
