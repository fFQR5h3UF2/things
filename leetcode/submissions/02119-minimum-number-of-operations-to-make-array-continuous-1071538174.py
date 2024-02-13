# Submission title: Minimum Number of Operations to Make Array Continuous
# Submission url  : https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/
# Submission url  : https://leetcode.com/submissions/detail/1071538174/
# Submission json : {"id":1071538174,"status_display":"Accepted","lang":"python3","question_id":2119,"title_slug":"minimum-number-of-operations-to-make-array-continuous","code":"class Solution:\n    def minOperations(self, nums: List[int]) -> int:\n        n = len(nums)\n        ans = n\n        new_nums = sorted(set(nums))\n        \n        for i in range(len(new_nums)):\n            left = new_nums[i]\n            right = left + n - 1\n            j = bisect_right(new_nums, right)\n            count = j - i\n            ans = min(ans, n - count)\n\n        return ans","title":"Minimum Number of Operations to Make Array Continuous","url":"/submissions/detail/1071538174/","lang_name":"Python3","time":"3 months, 3 weeks","timestamp":1696915408,"status":10,"runtime":"687 ms","is_pending":"Not Pending","memory":"35.3 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))

        for i in range(len(new_nums)):
            left = new_nums[i]
            right = left + n - 1
            j = bisect_right(new_nums, right)
            count = j - i
            ans = min(ans, n - count)

        return ans
