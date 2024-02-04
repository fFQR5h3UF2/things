# Submission title: for Minimum Replacements to Sort the Array
# Submission url  : https://leetcode.com/submissions/detail/1036091559/
# Submission json : {"id": 1036091559, "status_display": "Accepted", "lang": "python3", "question_id": 2450, "title_slug": "minimum-replacements-to-sort-the-array", "code": "class Solution:\n    def minimumReplacement(self, nums: List[int]) -> int:\n        nums_count = len(nums)\n        operations_count = 0\n        for i in reversed(range(nums_count - 1)):\n            cur, prev = nums[i], nums[i+1]\n            if cur <= prev:\n                continue\n            \n            elements_count = (cur + prev - 1) // prev\n            operations_count += elements_count - 1\n            nums[i] //= elements_count\n\n        return operations_count", "title": "Minimum Replacements to Sort the Array", "url": "/submissions/detail/1036091559/", "lang_name": "Python3", "time": "5\u00a0months, 1\u00a0week", "timestamp": 1693411584, "status": 10, "runtime": "486 ms", "is_pending": "Not Pending", "memory": "28 MB", "compare_result": "11111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums_count = len(nums)
        operations_count = 0
        for i in reversed(range(nums_count - 1)):
            cur, prev = nums[i], nums[i + 1]
            if cur <= prev:
                continue

            elements_count = (cur + prev - 1) // prev
            operations_count += elements_count - 1
            nums[i] //= elements_count

        return operations_count
