# Submission title: Number of Laser Beams in a Bank
# Submission url  : https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
# Submission url  : https://leetcode.com/submissions/detail/1135579756/
# Submission json : {"id":1135579756,"status_display":"Accepted","lang":"python3","question_id":2244,"title_slug":"number-of-laser-beams-in-a-bank","code":"class Solution:\n    def numberOfBeams(self, bank):\n        ans, temp = 0, 0\n        for s in bank:\n            n = s.count('1')\n            if n == 0:\n                continue\n            ans += temp * n\n            temp = n\n        return ans\n\n\n","title":"Number of Laser Beams in a Bank","url":"/submissions/detail/1135579756/","lang_name":"Python3","time":"1 month","timestamp":1704282409,"status":10,"runtime":"91 ms","is_pending":"Not Pending","memory":"19.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def numberOfBeams(self, bank):
        ans, temp = 0, 0
        for s in bank:
            n = s.count("1")
            if n == 0:
                continue
            ans += temp * n
            temp = n
        return ans
