# Submission title: Remove Duplicates from Sorted Array II
# Submission url  : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/996008020/
# Submission json : {"id":996008020,"status_display":"Accepted","lang":"python3","question_id":80,"title_slug":"remove-duplicates-from-sorted-array-ii","code":"class Solution:\n    def removeDuplicates(self, nums: List[int]) -> int:\n        length = len(nums)\n\n        if length < 2:\n            return length\n        \n        current_number, unique, current_index = nums[0], True, 1\n        for number in nums[1:]:\n            if current_number != number:\n                current_number = number\n                unique = True\n                nums[current_index] = number\n                current_index += 1\n                continue\n\n            if unique:\n                nums[current_index] = number\n                current_index += 1\n                unique = False\n\n        return current_index","title":"Remove Duplicates from Sorted Array II","url":"/submissions/detail/996008020/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689524373,"status":10,"runtime":"66 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


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
