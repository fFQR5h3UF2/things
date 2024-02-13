# Submission title: Product of Array Except Self
# Submission url  : https://leetcode.com/problems/product-of-array-except-self/description/
# Submission url  : https://leetcode.com/submissions/detail/1018287507/
# Submission json : {"id":1018287507,"status_display":"Accepted","lang":"python3","question_id":238,"title_slug":"product-of-array-except-self","code":"class Solution:\n    def productExceptSelf(self, nums: List[int]) -> List[int]:\n        nums_count = len(nums)\n        result = [1] * nums_count\n        prefix = 1\n        postfix = 1\n        for i in range(nums_count):\n            result[i] *= prefix\n            prefix *= nums[i]\n\n            from_end = -1 * (i + 1)\n            result[from_end] *= postfix\n            postfix *= nums[from_end]\n        \n        return result","title":"Product of Array Except Self","url":"/submissions/detail/1018287507/","lang_name":"Python3","time":"5 months, 3 weeks","timestamp":1691744733,"status":10,"runtime":"198 ms","is_pending":"Not Pending","memory":"24.1 MB","compare_result":"1111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_count = len(nums)
        result = [1] * nums_count
        prefix = 1
        postfix = 1
        for i in range(nums_count):
            result[i] *= prefix
            prefix *= nums[i]

            from_end = -1 * (i + 1)
            result[from_end] *= postfix
            postfix *= nums[from_end]

        return result
