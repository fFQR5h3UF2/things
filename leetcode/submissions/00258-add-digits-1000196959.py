# Submission title: Add Digits
# Submission url  : https://leetcode.com/problems/add-digits/description/
# Submission url  : https://leetcode.com/submissions/detail/1000196959/
# Submission json : {"id":1000196959,"status_display":"Accepted","lang":"python3","question_id":258,"title_slug":"add-digits","code":"class Solution:\n    def addDigits(self, num: int) -> int:\n        sum = num\n        while sum > 9:\n            current_number, current_sum = sum, 0\n            while current_number:\n                current_sum += current_number % 10\n                current_number //= 10\n            sum = current_sum\n        return sum","title":"Add Digits","url":"/submissions/detail/1000196959/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689946617,"status":10,"runtime":"36 ms","is_pending":"Not Pending","memory":"16.1 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def addDigits(self, num: int) -> int:
        sum = num
        while sum > 9:
            current_number, current_sum = sum, 0
            while current_number:
                current_sum += current_number % 10
                current_number //= 10
            sum = current_sum
        return sum
