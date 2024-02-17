# Submission title: Remove Duplicates from Sorted Array
# Submission url  : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/"
# Submission url  : https://leetcode.com/submissions/detail/956368066/"


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 1

        unique_count = 1
        last_unique_index = 0
        for i, number in enumerate(nums[1:], 1):
            last_unique = nums[last_unique_index]
            if number == last_unique:
                continue

            unique_count += 1
            last_unique_index += 1
            nums[last_unique_index] = number

        nums = nums[: last_unique_index + 1]

        return unique_count
