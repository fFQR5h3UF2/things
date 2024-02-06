# Submission title: for Sum of All Subset XOR Totals
# Submission url  : https://leetcode.com/submissions/detail/1056218717/
# Submission json : {"id": 1056218717, "status_display": "Accepted", "lang": "python3", "question_id": 1993, "title_slug": "sum-of-all-subset-xor-totals", "code": "class Solution:\n    def subsetXORSum(self, nums: List[int]) -> int:\n        return reduce(operator.or_, nums) * 1 << (len(nums) - 1)\n        ", "title": "Sum of All Subset XOR Totals", "url": "/submissions/detail/1056218717/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1695379909, "status": 10, "runtime": "45 ms", "is_pending": "Not Pending", "memory": "16 MB", "compare_result": "111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(operator.or_, nums) * 1 << (len(nums) - 1)
