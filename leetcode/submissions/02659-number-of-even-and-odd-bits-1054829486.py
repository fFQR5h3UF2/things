# Submission title: Number of Even and Odd Bits
# Submission url  : https://leetcode.com/problems/number-of-even-and-odd-bits/description/
# Submission url  : https://leetcode.com/submissions/detail/1054829486/
# Submission json : {"id":1054829486,"status_display":"Accepted","lang":"python3","question_id":2659,"title_slug":"number-of-even-and-odd-bits","code":"class Solution:\n    def evenOddBit(self, n: int) -> List[int]:\n        return (n & 0x55555555).bit_count(), (n & 0xaaaaaaaa).bit_count()","title":"Number of Even and Odd Bits","url":"/submissions/detail/1054829486/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695237768,"status":10,"runtime":"36 ms","is_pending":"Not Pending","memory":"16 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        return (n & 0x55555555).bit_count(), (n & 0xAAAAAAAA).bit_count()
