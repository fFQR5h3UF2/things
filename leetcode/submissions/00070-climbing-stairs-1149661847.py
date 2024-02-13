# Submission title: Climbing Stairs
# Submission url  : https://leetcode.com/problems/climbing-stairs/description/
# Submission url  : https://leetcode.com/submissions/detail/1149661847/
# Submission json : {"id":1149661847,"status_display":"Accepted","lang":"python3","question_id":70,"title_slug":"climbing-stairs","code":"class Solution:\n    def climbStairs(self, n: int) -> int:\n        prev, cur = 1, 2\n        if n == prev:\n            return prev\n        if n == cur:\n            return cur\n        for i in range(2, n):\n            new = prev + cur\n            cur, prev = new, cur\n        return cur","title":"Climbing Stairs","url":"/submissions/detail/1149661847/","lang_name":"Python3","time":"2 weeks, 3 days","timestamp":1705573630,"status":10,"runtime":"29 ms","is_pending":"Not Pending","memory":"17.4 MB","compare_result":"111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 1, 2
        if n == prev:
            return prev
        if n == cur:
            return cur
        for i in range(2, n):
            new = prev + cur
            cur, prev = new, cur
        return cur
