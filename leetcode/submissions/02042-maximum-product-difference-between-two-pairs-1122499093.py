# Submission title: Maximum Product Difference Between Two Pairs
# Submission url  : https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
# Submission url  : https://leetcode.com/submissions/detail/1122499093/
# Submission json : {"id":1122499093,"status_display":"Accepted","lang":"python3","question_id":2042,"title_slug":"maximum-product-difference-between-two-pairs","code":"class Solution:\r\n    def maxProductDifference(self, nums: List[int]) -> int:\r\n        nums.sort()\r\n        return nums[-1] * nums[-2] - nums[0] * nums[1]","title":"Maximum Product Difference Between Two Pairs","url":"/submissions/detail/1122499093/","lang_name":"Python3","time":"1 month, 2 weeks","timestamp":1702895229,"status":10,"runtime":"166 ms","is_pending":"Not Pending","memory":"17.7 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
