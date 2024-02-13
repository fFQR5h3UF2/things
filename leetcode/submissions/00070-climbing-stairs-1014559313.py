# Submission title: Climbing Stairs
# Submission url  : https://leetcode.com/problems/climbing-stairs/description/
# Submission url  : https://leetcode.com/submissions/detail/1014559313/
# Submission json : {"id":1014559313,"status_display":"Accepted","lang":"python3","question_id":70,"title_slug":"climbing-stairs","code":"class Solution:\n    def climbStairs(self, n: int) -> int:\n\n        @cache\n        def dp(step: int) -> int:\n            if step <= 2:\n                return step\n            \n            return dp(step - 1) + dp(step - 2) \n \n        return dp(n)","title":"Climbing Stairs","url":"/submissions/detail/1014559313/","lang_name":"Python3","time":"6 months","timestamp":1691401554,"status":10,"runtime":"40 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def dp(step: int) -> int:
            if step <= 2:
                return step

            return dp(step - 1) + dp(step - 2)

        return dp(n)
