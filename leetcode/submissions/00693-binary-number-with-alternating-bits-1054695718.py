# Submission title: Binary Number with Alternating Bits
# Submission url  : https://leetcode.com/problems/binary-number-with-alternating-bits/description/
# Submission url  : https://leetcode.com/submissions/detail/1054695718/
# Submission json : {"id":1054695718,"status_display":"Accepted","lang":"python3","question_id":693,"title_slug":"binary-number-with-alternating-bits","code":"class Solution:\n    def hasAlternatingBits(self, n: int) -> bool:\n        return n & (n >> 1) == 0 and n & (n >> 2) == n >> 2","title":"Binary Number with Alternating Bits","url":"/submissions/detail/1054695718/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695228656,"status":10,"runtime":"39 ms","is_pending":"Not Pending","memory":"16.1 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return n & (n >> 1) == 0 and n & (n >> 2) == n >> 2
