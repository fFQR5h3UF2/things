# Submission title: Number of Steps to Reduce a Number to Zero
# Submission url  : https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
# Submission url  : https://leetcode.com/submissions/detail/1000093970/
# Submission json : {"id":1000093970,"status_display":"Accepted","lang":"python3","question_id":1444,"title_slug":"number-of-steps-to-reduce-a-number-to-zero","code":"class Solution:\n    def numberOfSteps(self, num: int) -> int:\n        count = 0\n        while num:\n            count += 1\n            if num % 2 == 0:\n                num /= 2\n            else:\n                num -= 1\n        \n        return count\n            ","title":"Number of Steps to Reduce a Number to Zero","url":"/submissions/detail/1000093970/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689935685,"status":10,"runtime":"39 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            count += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1

        return count
