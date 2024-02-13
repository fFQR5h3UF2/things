# Submission title: Sort Integers by The Number of 1 Bits
# Submission url  : https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/
# Submission url  : https://leetcode.com/submissions/detail/1054833349/
# Submission json : {"id":1054833349,"status_display":"Accepted","lang":"python3","question_id":1458,"title_slug":"sort-integers-by-the-number-of-1-bits","code":"class Solution:\n    def sortByBits(self, arr: List[int]) -> List[int]:\n        return tuple(num for num in sorted(arr, key=lambda num: (num.bit_count(), num)))","title":"Sort Integers by The Number of 1 Bits","url":"/submissions/detail/1054833349/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695238096,"status":10,"runtime":"60 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return tuple(num for num in sorted(arr, key=lambda num: (num.bit_count(), num)))
