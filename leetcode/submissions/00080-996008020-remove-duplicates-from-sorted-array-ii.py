# Submission title: Remove Duplicates from Sorted Array II
# Submission url  : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/"
# Submission url  : https://leetcode.com/submissions/detail/996008020/"


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)

        if length < 2:
            return length

        current_number, unique, current_index = nums[0], True, 1
        for number in nums[1:]:
            if current_number != number:
                current_number = number
                unique = True
                nums[current_index] = number
                current_index += 1
                continue

            if unique:
                nums[current_index] = number
                current_index += 1
                unique = False

        return current_index
