# Submission title: Sqrt(x)
# Submission url  : https://leetcode.com/problems/sqrtx/description/
# Submission url  : https://leetcode.com/submissions/detail/997665272/
# Submission json : {"id":997665272,"status_display":"Accepted","lang":"python3","question_id":69,"title_slug":"sqrtx","code":"class Solution:\n    def mySqrt(self, x: int) -> int:\n        if x == 0 or x == 1:\n            return x\n\n        left, right = 1, x\n\n        while left <= right:\n            mid = left + (right - left) // 2\n            square = mid * mid\n\n            if square == x:\n                return mid\n            \n            if square > x:\n                right = mid - 1 \n            else:\n                left = mid + 1\n            \n        return right","title":"Sqrt(x)","url":"/submissions/detail/997665272/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689693019,"status":10,"runtime":"63 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 1, x

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid

            if square > x:
                right = mid - 1
            else:
                left = mid + 1

        return right
