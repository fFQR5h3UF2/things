# Submission title: Divide Array Into Arrays With Max Difference
# Submission url  : https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/
# Submission url  : https://leetcode.com/submissions/detail/1164073020/
# Submission json : {"id":1164073020,"status_display":"Accepted","lang":"python3","question_id":3241,"title_slug":"divide-array-into-arrays-with-max-difference","code":"class Solution:\n    def divideArray(self, nums, k):\n        size = len(nums)\n        if size % 3 != 0:\n            return []\n\n        nums.sort()\n\n        result = []\n        group_index = 0\n        for i in range(0, size, 3):\n            if i + 2 < size and nums[i + 2] - nums[i] <= k:\n                result.append([nums[i], nums[i + 1], nums[i + 2]])\n                group_index += 1\n            else:\n                return []\n        return result\n\n\n","title":"Divide Array Into Arrays With Max Difference","url":"/submissions/detail/1164073020/","lang_name":"Python3","time":"1 day, 21 hours","timestamp":1706892730,"status":10,"runtime":"703 ms","is_pending":"Not Pending","memory":"30.8 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def divideArray(self, nums, k):
        size = len(nums)
        if size % 3 != 0:
            return []

        nums.sort()

        result = []
        group_index = 0
        for i in range(0, size, 3):
            if i + 2 < size and nums[i + 2] - nums[i] <= k:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
                group_index += 1
            else:
                return []
        return result
