# Submission title: Counting Bits
# Submission url  : https://leetcode.com/problems/counting-bits/description/
# Submission url  : https://leetcode.com/submissions/detail/1037436534/
# Submission json : {"id":1037436534,"status_display":"Accepted","lang":"python3","question_id":338,"title_slug":"counting-bits","code":"class Solution:\n    def countBits(self, n: int) -> List[int]:\n        return tuple(bin(i).count(\"1\") for i in range(n + 1))","title":"Counting Bits","url":"/submissions/detail/1037436534/","lang_name":"Python3","time":"5 months","timestamp":1693551312,"status":10,"runtime":"78 ms","is_pending":"Not Pending","memory":"23.1 MB","compare_result":"111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def countBits(self, n: int) -> List[int]:
        return tuple(bin(i).count("1") for i in range(n + 1))
