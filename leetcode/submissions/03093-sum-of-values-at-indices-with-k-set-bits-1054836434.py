# Submission title: Sum of Values at Indices With K Set Bits
# Submission url  : https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/
# Submission url  : https://leetcode.com/submissions/detail/1054836434/
# Submission json : {"id":1054836434,"status_display":"Accepted","lang":"python3","question_id":3093,"title_slug":"sum-of-values-at-indices-with-k-set-bits","code":"class Solution:\n    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:\n        return sum(num for i, num in enumerate(nums) if i.bit_count() == k)","title":"Sum of Values at Indices With K Set Bits","url":"/submissions/detail/1054836434/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695238346,"status":10,"runtime":"81 ms","is_pending":"Not Pending","memory":"16.1 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(num for i, num in enumerate(nums) if i.bit_count() == k)
