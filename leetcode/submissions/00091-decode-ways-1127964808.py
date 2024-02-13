# Submission title: Decode Ways
# Submission url  : https://leetcode.com/problems/decode-ways/description/
# Submission url  : https://leetcode.com/submissions/detail/1127964808/
# Submission json : {"id":1127964808,"status_display":"Accepted","lang":"python3","question_id":91,"title_slug":"decode-ways","code":"class Solution:\n    def numDecodings(self, s):\n        if s == \"0\":\n            return 0\n        \n        # dp_0 = dp[i]\n        # dp_1 = dp[i + 1]\n        # dp_2 = dp[i + 2]\n        dp_2 = 1\n        dp_1 = int(s[-1] != \"0\")\n\n        i = len(s) - 2\n        while i >= 0:\n            if s[i] == \"0\":\n                dp_0 = 0\n            else:\n                dp_0 = dp_1\n                if (s[i] == \"1\") or (s[i] == \"2\" and eval(s[i + 1]) < 7):\n                    dp_0 += dp_2\n            i -= 1\n            dp_0, dp_1, dp_2 = 0, dp_0, dp_1\n        \n        return dp_1","title":"Decode Ways","url":"/submissions/detail/1127964808/","lang_name":"Python3","time":"1 month, 1 week","timestamp":1703490835,"status":10,"runtime":"32 ms","is_pending":"Not Pending","memory":"17.3 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def numDecodings(self, s):
        if s == "0":
            return 0

        # dp_0 = dp[i]
        # dp_1 = dp[i + 1]
        # dp_2 = dp[i + 2]
        dp_2 = 1
        dp_1 = int(s[-1] != "0")

        i = len(s) - 2
        while i >= 0:
            if s[i] == "0":
                dp_0 = 0
            else:
                dp_0 = dp_1
                if (s[i] == "1") or (s[i] == "2" and eval(s[i + 1]) < 7):
                    dp_0 += dp_2
            i -= 1
            dp_0, dp_1, dp_2 = 0, dp_0, dp_1

        return dp_1
