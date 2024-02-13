# Submission title: Sort Array By Parity
# Submission url  : https://leetcode.com/problems/sort-array-by-parity/description/
# Submission url  : https://leetcode.com/submissions/detail/1061188297/
# Submission json : {"id":1061188297,"status_display":"Accepted","lang":"python3","question_id":941,"title_slug":"sort-array-by-parity","code":"class Solution:\n    def sortArrayByParity(self, nums: List[int]) -> List[int]:\n        left, right = 0, len(nums) - 1\n        while left < right:\n            while left < right and nums[left] % 2 == 0:\n                left += 1\n            while left < right and nums[right] % 2 == 1:\n                right -= 1\n            nums[left], nums[right] = nums[right], nums[left]\n        return nums","title":"Sort Array By Parity","url":"/submissions/detail/1061188297/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695885453,"status":10,"runtime":"79 ms","is_pending":"Not Pending","memory":"17 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 == 1:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums
