# Submission title: Happy Number
# Submission url  : https://leetcode.com/problems/happy-number/description/
# Submission url  : https://leetcode.com/submissions/detail/995701431/
# Submission json : {"id":995701431,"status_display":"Accepted","lang":"python3","question_id":202,"title_slug":"happy-number","code":"class Solution:\n    def isHappy(self, n: int) -> bool:\n        sums = set()\n        while n != 1:\n            if n in sums:\n                return False\n            sums.add(n)\n            \n            sum = 0\n            while n > 0:\n                sum += (n % 10 )**2\n                n = n // 10\n            n = sum\n\n        return True","title":"Happy Number","url":"/submissions/detail/995701431/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689493640,"status":10,"runtime":"48 ms","is_pending":"Not Pending","memory":"16.1 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()
        while n != 1:
            if n in sums:
                return False
            sums.add(n)

            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n = n // 10
            n = sum

        return True
