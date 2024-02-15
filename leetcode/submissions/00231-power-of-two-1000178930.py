# Submission title: Power of Two
# Submission url  : https://leetcode.com/problems/power-of-two/description/
# Submission url  : https://leetcode.com/submissions/detail/1000178930/
# Submission json : {"id":1000178930,"status_display":"Accepted","lang":"python3","question_id":231,"title_slug":"power-of-two","code":"class Solution:\n    def isPowerOfTwo(self, n: int) -> bool:\n        if n == 1:\n            return True\n\n        while n > 2 and not n % 2:\n            n //= 2\n        return n == 2","title":"Power of Two","url":"/submissions/detail/1000178930/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689944768,"status":10,"runtime":"41 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        while n > 2 and not n % 2:
            n //= 2
        return n == 2