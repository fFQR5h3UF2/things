# Submission title: 132 Pattern
# Submission url  : https://leetcode.com/problems/132-pattern/description/
# Submission url  : https://leetcode.com/submissions/detail/1062846682/
# Submission json : {"id":1062846682,"status_display":"Accepted","lang":"python3","question_id":456,"title_slug":"132-pattern","code":"class Solution:\n    def find132pattern(self, nums: List[int]) -> bool:\n        if len(nums) < 3:\n            return False\n        stack = []\n        min_array = [-1] * len(nums)\n        min_array[0] = nums[0]\n        for i in range(1, len(nums)):\n            min_array[i] = min(min_array[i - 1], nums[i])\n\n        for j in reversed(range(len(nums))):\n            if nums[j] <= min_array[j]:\n                continue\n            while stack and stack[-1] <= min_array[j]:\n                stack.pop()\n            if stack and stack[-1] < nums[j]:\n                return True\n            stack.append(nums[j])\n        return False","title":"132 Pattern","url":"/submissions/detail/1062846682/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1696057556,"status":10,"runtime":"428 ms","is_pending":"Not Pending","memory":"36.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])

        for j in reversed(range(len(nums))):
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False
