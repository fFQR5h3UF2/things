# Submission title: Longest Consecutive Sequence
# Submission url  : https://leetcode.com/problems/longest-consecutive-sequence/description/
# Submission url  : https://leetcode.com/submissions/detail/997539098/
# Submission json : {"id":997539098,"status_display":"Accepted","lang":"python3","question_id":128,"title_slug":"longest-consecutive-sequence","code":"class Solution:\n    def longestConsecutive(self, nums: List[int]) -> int:\n        length = len(nums)\n        if length < 2:\n            return length\n        \n        nums = set(nums)\n        longest = 1\n        for number in nums:\n            if number - 1 in nums:\n                continue\n            consequent = 1\n            while number + consequent in nums:\n                consequent += 1\n            longest = max(longest, consequent)\n        \n        return longest","title":"Longest Consecutive Sequence","url":"/submissions/detail/997539098/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689682534,"status":10,"runtime":"439 ms","is_pending":"Not Pending","memory":"31 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length

        nums = set(nums)
        longest = 1
        for number in nums:
            if number - 1 in nums:
                continue
            consequent = 1
            while number + consequent in nums:
                consequent += 1
            longest = max(longest, consequent)

        return longest
