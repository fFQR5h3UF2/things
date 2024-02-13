# Submission title: Remove Duplicates from Sorted Array
# Submission url  : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Submission url  : https://leetcode.com/submissions/detail/993608947/
# Submission json : {"id":993608947,"status_display":"Accepted","lang":"python3","question_id":26,"title_slug":"remove-duplicates-from-sorted-array","code":"class Solution:\n    # non-decreasing order, so to remove the duplicates we just need to remove all \n    #    consequent duplicates\n    # create replace index, set it to 0\n    # create a set of duplicates\n    # iterate over nums:\n    # - if the number is in the set, continue\n    # - if the number is not in the set, set nums[replace] to that number, add it to the set\n    # return replace\n    def removeDuplicates(self, nums: List[int]) -> int:\n        replace, duplicates = 0, set()\n        for i, number in enumerate(nums): \n            if number in duplicates:\n                continue\n            nums[replace] = number\n            replace += 1\n            duplicates.add(number)\n        \n        return replace","title":"Remove Duplicates from Sorted Array","url":"/submissions/detail/993608947/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689264194,"status":10,"runtime":"98 ms","is_pending":"Not Pending","memory":"18 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    # non-decreasing order, so to remove the duplicates we just need to remove all
    #    consequent duplicates
    # create replace index, set it to 0
    # create a set of duplicates
    # iterate over nums:
    # - if the number is in the set, continue
    # - if the number is not in the set, set nums[replace] to that number, add it to the set
    # return replace
    def removeDuplicates(self, nums: List[int]) -> int:
        replace, duplicates = 0, set()
        for i, number in enumerate(nums):
            if number in duplicates:
                continue
            nums[replace] = number
            replace += 1
            duplicates.add(number)

        return replace
