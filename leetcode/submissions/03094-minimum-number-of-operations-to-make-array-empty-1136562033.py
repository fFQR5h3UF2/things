# Submission title: Minimum Number of Operations to Make Array Empty
# Submission url  : https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/
# Submission url  : https://leetcode.com/submissions/detail/1136562033/
# Submission json : {"id":1136562033,"status_display":"Accepted","lang":"python3","question_id":3094,"title_slug":"minimum-number-of-operations-to-make-array-empty","code":"class Solution:\n    def minOperations(self, nums: List[int]) -> int:\n        counter = Counter(nums)\n        ans = 0\n        for c in counter.values():\n            if c == 1: \n                return -1\n            ans += ceil(c / 3)\n        return ans","title":"Minimum Number of Operations to Make Array Empty","url":"/submissions/detail/1136562033/","lang_name":"Python3","time":"1 month","timestamp":1704366709,"status":10,"runtime":"516 ms","is_pending":"Not Pending","memory":"32.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1:
                return -1
            ans += ceil(c / 3)
        return ans
