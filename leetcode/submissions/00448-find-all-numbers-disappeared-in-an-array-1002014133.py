# Submission title: Find All Numbers Disappeared in an Array
# Submission url  : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1002014133/
# Submission json : {"id":1002014133,"status_display":"Accepted","lang":"python3","question_id":448,"title_slug":"find-all-numbers-disappeared-in-an-array","code":"class Solution:\n    # [1,1,3,4], [1,2,3,4] -> [2]\n    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:\n        result = {number: True for number in range(1, len(nums) + 1)}\n\n        for number in nums:\n            result[number] = False\n        \n        return [number for number, valid in result.items() if valid]\n","title":"Find All Numbers Disappeared in an Array","url":"/submissions/detail/1002014133/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690135265,"status":10,"runtime":"345 ms","is_pending":"Not Pending","memory":"29.5 MB","compare_result":"1111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    # [1,1,3,4], [1,2,3,4] -> [2]
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = {number: True for number in range(1, len(nums) + 1)}

        for number in nums:
            result[number] = False

        return [number for number, valid in result.items() if valid]
