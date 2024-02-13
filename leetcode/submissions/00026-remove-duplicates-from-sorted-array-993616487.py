# Submission title: Remove Duplicates from Sorted Array
# Submission url  : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Submission url  : https://leetcode.com/submissions/detail/993616487/
# Submission json : {"id":993616487,"status_display":"Accepted","lang":"python3","question_id":26,"title_slug":"remove-duplicates-from-sorted-array","code":"class Solution:\n    # non-decreasing order, so to remove the duplicates we just need to remove all \n    #    consequent duplicates\n    # create replace index, set it to 1 - the first element is always unique\n    # check if length is more than 1 to avoid out-of-bounds - \n    #   if the length is one, just return 1\n    # iterate over nums starting from the second element:\n    # - if the current number is not equal to the previous, \n    #   set nums[replace] to it, move the replace index\n    # - if the current number is equal to the previous one, continue \n    # return replace \n    def removeDuplicates(self, nums: List[int]) -> int:\n        replace = 1\n        for i, number in enumerate(nums[1:], 1): \n            if number == nums[i-1]:\n                continue\n            nums[replace] = number\n            replace += 1\n        \n        return replace","title":"Remove Duplicates from Sorted Array","url":"/submissions/detail/993616487/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689264811,"status":10,"runtime":"106 ms","is_pending":"Not Pending","memory":"17.9 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    # non-decreasing order, so to remove the duplicates we just need to remove all
    #    consequent duplicates
    # create replace index, set it to 1 - the first element is always unique
    # check if length is more than 1 to avoid out-of-bounds -
    #   if the length is one, just return 1
    # iterate over nums starting from the second element:
    # - if the current number is not equal to the previous,
    #   set nums[replace] to it, move the replace index
    # - if the current number is equal to the previous one, continue
    # return replace
    def removeDuplicates(self, nums: List[int]) -> int:
        replace = 1
        for i, number in enumerate(nums[1:], 1):
            if number == nums[i - 1]:
                continue
            nums[replace] = number
            replace += 1

        return replace
