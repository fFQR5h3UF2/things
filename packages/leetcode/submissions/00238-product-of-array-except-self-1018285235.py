# Submission title: for Product of Array Except Self
# Submission url  : https://leetcode.com/submissions/detail/1018285235/
# Submission json : {"id": 1018285235, "status_display": "Accepted", "lang": "python3", "question_id": 238, "title_slug": "product-of-array-except-self", "code": "class Solution:\n    def productExceptSelf(self, nums: List[int]) -> List[int]:\n        nums_count = len(nums)\n        result = [1] * nums_count\n        prefix = 1\n        postfix = 1\n        for i in range(nums_count):\n            result[i] *= prefix\n            prefix *= nums[i]\n            result[nums_count-i-1] *= postfix\n            postfix *= nums[nums_count-i-1]\n        \n        return result", "title": "Product of Array Except Self", "url": "/submissions/detail/1018285235/", "lang_name": "Python3", "time": "5\u00a0months, 3\u00a0weeks", "timestamp": 1691744509, "status": 10, "runtime": "199 ms", "is_pending": "Not Pending", "memory": "24.2 MB", "compare_result": "1111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_count = len(nums)
        result = [1] * nums_count
        prefix = 1
        postfix = 1
        for i in range(nums_count):
            result[i] *= prefix
            prefix *= nums[i]
            result[nums_count - i - 1] *= postfix
            postfix *= nums[nums_count - i - 1]

        return result
