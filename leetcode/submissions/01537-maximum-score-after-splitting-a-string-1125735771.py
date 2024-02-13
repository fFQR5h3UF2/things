# Submission title: Maximum Score After Splitting a String
# Submission url  : https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/
# Submission url  : https://leetcode.com/submissions/detail/1125735771/
# Submission json : {"id":1125735771,"status_display":"Accepted","lang":"python3","question_id":1537,"title_slug":"maximum-score-after-splitting-a-string","code":"class Solution:\n    def maxScore(self, s: str) -> int:\n        ones = s.count(\"1\")\n        zeros = 0\n        ans = 0 \n\n        for i in range(len(s) - 1):\n            if s[i] == \"1\":\n                ones -= 1\n            else:\n                zeros += 1\n        \n            ans = max(ans, zeros + ones)\n        \n        return ans","title":"Maximum Score After Splitting a String","url":"/submissions/detail/1125735771/","lang_name":"Python3","time":"1 month, 2 weeks","timestamp":1703235133,"status":10,"runtime":"37 ms","is_pending":"Not Pending","memory":"17.2 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        ans = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1

            ans = max(ans, zeros + ones)

        return ans
