# Submission title: Number of Longest Increasing Subsequence
# Submission url  : https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
# Submission url  : https://leetcode.com/submissions/detail/1000080729/
# Submission json : {"id":1000080729,"status_display":"Accepted","lang":"python3","question_id":673,"title_slug":"number-of-longest-increasing-subsequence","code":"class Solution:\n    def findNumberOfLIS(self, nums: List[int]) -> int:\n        n = len(nums)\n        if n <= 1:\n            return n\n\n        lengths = [1] * n\n        counts = [1] * n\n\n        for i in range(1, n):\n            for j in range(i):\n                if nums[i] > nums[j]:\n                    if lengths[j] + 1 > lengths[i]:\n                        lengths[i] = lengths[j] + 1\n                        counts[i] = counts[j]\n                    elif lengths[j] + 1 == lengths[i]:\n                        counts[i] += counts[j]\n\n        max_length = max(lengths)\n        return sum(count for length, count in zip(lengths, counts) if length == max_length)\n","title":"Number of Longest Increasing Subsequence","url":"/submissions/detail/1000080729/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689934296,"status":10,"runtime":"1126 ms","is_pending":"Not Pending","memory":"16.6 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        lengths = [1] * n
        counts = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_length = max(lengths)
        return sum(
            count for length, count in zip(lengths, counts) if length == max_length
        )
