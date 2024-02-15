# Submission title: Pow(x, n)
# Submission url  : https://leetcode.com/problems/powx-n/description/
# Submission url  : https://leetcode.com/submissions/detail/1057801419/
# Submission json : {"id":1057801419,"status_display":"Accepted","lang":"python3","question_id":50,"title_slug":"powx-n","code":"class Solution:\n    def myPow(self, x: float, n: int) -> float:\n        if n == 0:\n            return 1\n\n        if n < 0:\n            n *= -1\n            x = 1 / x\n\n        result = 1\n        while n:\n            if n % 2:\n                result *= x\n                n -= 1\n            x *= x\n            n //= 2\n        \n        return result","title":"Pow(x, n)","url":"/submissions/detail/1057801419/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695548515,"status":10,"runtime":"40 ms","is_pending":"Not Pending","memory":"16.2 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            n *= -1
            x = 1 / x

        result = 1
        while n:
            if n % 2:
                result *= x
                n -= 1
            x *= x
            n //= 2

        return result