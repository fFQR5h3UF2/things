# Submission title: Sum of All Subset XOR Totals
# Submission url  : https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
# Submission url  : https://leetcode.com/submissions/detail/1056216664/
# Submission json : {"id":1056216664,"status_display":"Accepted","lang":"python3","question_id":1993,"title_slug":"sum-of-all-subset-xor-totals","code":"class Solution:\n    def subsetXORSum(self, nums: List[int]) -> int:\n        subsets_count = 2**(len(nums) - 1)\n        return reduce(operator.or_, nums) * subsets_count\n        ","title":"Sum of All Subset XOR Totals","url":"/submissions/detail/1056216664/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695379750,"status":10,"runtime":"33 ms","is_pending":"Not Pending","memory":"16.1 MB","compare_result":"111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets_count = 2 ** (len(nums) - 1)
        return reduce(operator.or_, nums) * subsets_count
