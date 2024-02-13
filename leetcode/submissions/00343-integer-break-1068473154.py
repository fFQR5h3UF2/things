# Submission title: Integer Break
# Submission url  : https://leetcode.com/problems/integer-break/description/
# Submission url  : https://leetcode.com/submissions/detail/1068473154/
# Submission json : {"id":1068473154,"status_display":"Accepted","lang":"python3","question_id":343,"title_slug":"integer-break","code":"class Solution:\n    def integerBreak(self, n: int) -> int:\n        if n < 4:\n            return n - 1\n        \n        @cache\n        def dp(num: int) -> int:\n            if num <= 3:\n                return num\n            ans = num\n            for i in range(2, num):\n                ans = max(ans, i * dp(num - i))\n            return ans\n\n        return dp(n)","title":"Integer Break","url":"/submissions/detail/1068473154/","lang_name":"Python3","time":"4 months","timestamp":1696584279,"status":10,"runtime":"42 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"11111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1

        @cache
        def dp(num: int) -> int:
            if num <= 3:
                return num
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp(num - i))
            return ans

        return dp(n)
