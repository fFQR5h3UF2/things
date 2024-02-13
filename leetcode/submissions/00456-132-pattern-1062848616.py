# Submission title: 132 Pattern
# Submission url  : https://leetcode.com/problems/132-pattern/description/
# Submission url  : https://leetcode.com/submissions/detail/1062848616/
# Submission json : {"id":1062848616,"status_display":"Accepted","lang":"python3","question_id":456,"title_slug":"132-pattern","code":"class Solution:\n    def find132pattern(self, nums: List[int]) -> bool:\n        if len(nums) < 3:\n            return False\n        min_array = [-1] * len(nums)\n        min_array[0] = nums[0]\n        for i in range(1, len(nums)):\n            min_array[i] = min(min_array[i - 1], nums[i])\n\n        k = len(nums)\n        for j in range(len(nums) - 1, -1, -1):\n            if nums[j] <= min_array[j]:\n                continue\n            while k < len(nums) and nums[k] <= min_array[j]:\n                k += 1\n            if k < len(nums) and nums[k] < nums[j]:\n                return True\n            k -= 1\n            nums[k] = nums[j]\n        return False","title":"132 Pattern","url":"/submissions/detail/1062848616/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1696057743,"status":10,"runtime":"423 ms","is_pending":"Not Pending","memory":"36.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])

        k = len(nums)
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while k < len(nums) and nums[k] <= min_array[j]:
                k += 1
            if k < len(nums) and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
        return False
