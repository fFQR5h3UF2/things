# Submission title: for Summary Ranges
# Submission url  : https://leetcode.com/submissions/detail/1029908803/
# Submission json : {"id": 1029908803, "status_display": "Accepted", "lang": "python3", "question_id": 228, "title_slug": "summary-ranges", "code": "class Solution:\n    def summaryRanges(self, nums: List[int]) -> List[str]:\n        nums_count = len(nums)\n        if nums_count == 0:\n            return []\n        if nums_count == 1:\n            return [str(nums[0])]\n\n        ranges = [[nums[0]] * 2]\n        for i, num in enumerate(nums[1:]):\n            if ranges[-1][1] == num - 1:\n                ranges[-1][1] = num\n            else:\n                ranges.append([num, num])\n\n        return [f\"{start}->{end}\" if start != end else str(start) for start, end in ranges]", "title": "Summary Ranges", "url": "/submissions/detail/1029908803/", "lang_name": "Python3", "time": "5\u00a0months, 2\u00a0weeks", "timestamp": 1692820596, "status": 10, "runtime": "36 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "1111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums_count = len(nums)
        if nums_count == 0:
            return []
        if nums_count == 1:
            return [str(nums[0])]

        ranges = [[nums[0]] * 2]
        for i, num in enumerate(nums[1:]):
            if ranges[-1][1] == num - 1:
                ranges[-1][1] = num
            else:
                ranges.append([num, num])

        return [
            f"{start}->{end}" if start != end else str(start) for start, end in ranges
        ]
