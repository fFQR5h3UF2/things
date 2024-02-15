# Submission title: Add Digits
# Submission url  : https://leetcode.com/problems/add-digits/description/
# Submission url  : https://leetcode.com/submissions/detail/1000199091/
# Submission json : {"id":1000199091,"status_display":"Accepted","lang":"python3","question_id":258,"title_slug":"add-digits","code":"class Solution:\n    def addDigits(self, num: int) -> int:\n        sum = 0\n        while num > 0:\n            sum += num % 10\n            num //= 10\n        \n            if num == 0 and sum > 9:\n                num, sum = sum, 0\n                \n        return sum","title":"Add Digits","url":"/submissions/detail/1000199091/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689946832,"status":10,"runtime":"51 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10

            if num == 0 and sum > 9:
                num, sum = sum, 0

        return sum