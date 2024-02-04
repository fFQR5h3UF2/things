# Submission title: for Longest Consecutive Sequence
# Submission url  : https://leetcode.com/submissions/detail/997534869/
# Submission json : {"id": 997534869, "status_display": "Accepted", "lang": "python3", "question_id": 128, "title_slug": "longest-consecutive-sequence", "code": "from sortedcontainers import SortedSet\n\nclass Solution:\n    def longestConsecutive(self, nums: List[int]) -> int:\n        nums = SortedSet(nums)\n        longest, current = 0, 0\n        for number in nums:\n            if number - 1 in nums:\n                current += 1\n                continue\n            if current > longest:\n                longest = current\n            current = 1\n        return max(current, longest)\n            ", "title": "Longest Consecutive Sequence", "url": "/submissions/detail/997534869/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689682124, "status": 10, "runtime": "415 ms", "is_pending": "Not Pending", "memory": "35.9 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


from sortedcontainers import SortedSet


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = SortedSet(nums)
        longest, current = 0, 0
        for number in nums:
            if number - 1 in nums:
                current += 1
                continue
            if current > longest:
                longest = current
            current = 1
        return max(current, longest)
