# Submission title: Find All Numbers Disappeared in an Array
# Submission url  : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1002023003/
# Submission json : {"id":1002023003,"status_display":"Accepted","lang":"python3","question_id":448,"title_slug":"find-all-numbers-disappeared-in-an-array","code":"class Solution:\n    # [1,1,3,4], [1,2,3,4] -> [2]\n    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:\n        for number in nums:\n            index = abs(number) - 1\n            nums[index] = -1 * abs(nums[index])\n        \n        return [number\n                for number in range(1, len(nums) + 1) \n                if nums[number-1] > 0]\n        \n","title":"Find All Numbers Disappeared in an Array","url":"/submissions/detail/1002023003/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690135971,"status":10,"runtime":"372 ms","is_pending":"Not Pending","memory":"25.2 MB","compare_result":"1111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    # [1,1,3,4], [1,2,3,4] -> [2]
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for number in nums:
            index = abs(number) - 1
            nums[index] = -1 * abs(nums[index])

        return [number for number in range(1, len(nums) + 1) if nums[number - 1] > 0]
