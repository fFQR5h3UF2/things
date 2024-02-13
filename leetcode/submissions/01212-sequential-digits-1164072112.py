# Submission title: Sequential Digits
# Submission url  : https://leetcode.com/problems/sequential-digits/description/
# Submission url  : https://leetcode.com/submissions/detail/1164072112/
# Submission json : {"id":1164072112,"status_display":"Accepted","lang":"python3","question_id":1212,"title_slug":"sequential-digits","code":"class Solution:\n    def sequentialDigits(self, low, high):\n        a = []\n\n        for i in range(1, 10):\n            num = i\n            next_digit = i + 1\n\n            while num <= high and next_digit <= 9:\n                num = num * 10 + next_digit\n                if low <= num <= high:\n                    a.append(num)\n                next_digit += 1\n\n        a.sort()\n        return a\n\n\n","title":"Sequential Digits","url":"/submissions/detail/1164072112/","lang_name":"Python3","time":"1 day, 21 hours","timestamp":1706892667,"status":10,"runtime":"40 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"11111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def sequentialDigits(self, low, high):
        a = []

        for i in range(1, 10):
            num = i
            next_digit = i + 1

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    a.append(num)
                next_digit += 1

        a.sort()
        return a
