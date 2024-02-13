# Submission title: Number of Even and Odd Bits
# Submission url  : https://leetcode.com/problems/number-of-even-and-odd-bits/description/
# Submission url  : https://leetcode.com/submissions/detail/1054827616/
# Submission json : {"id":1054827616,"status_display":"Accepted","lang":"python3","question_id":2659,"title_slug":"number-of-even-and-odd-bits","code":"class Solution:\n    def evenOddBit(self, n: int) -> List[int]:\n        even, odd = n & 0x55555555, n & 0xaaaaaaaa\n        even_count, odd_count = 0, 0\n        while even:\n            if even & 1 == 1:\n                even_count += 1\n            even >>= 1\n            \n        while odd:\n            if odd & 1 == 1:\n                odd_count += 1\n            odd >>= 1\n        \n        return even_count, odd_count","title":"Number of Even and Odd Bits","url":"/submissions/detail/1054827616/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695237616,"status":10,"runtime":"40 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = n & 0x55555555, n & 0xAAAAAAAA
        even_count, odd_count = 0, 0
        while even:
            if even & 1 == 1:
                even_count += 1
            even >>= 1

        while odd:
            if odd & 1 == 1:
                odd_count += 1
            odd >>= 1

        return even_count, odd_count
