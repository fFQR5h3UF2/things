# Submission title: Word Break
# Submission url  : https://leetcode.com/problems/word-break/description/
# Submission url  : https://leetcode.com/submissions/detail/1014586880/
# Submission json : {"id":1014586880,"status_display":"Accepted","lang":"python3","question_id":139,"title_slug":"word-break","code":"class Solution:\n    def wordBreak(self, s: str, wordDict: List[str]) -> bool:\n        n = len(s)\n        words = set(wordDict)\n        dp = [False] * (n + 1)\n        dp[0] = True\n        \n        for i in range(1, n + 1):\n            for j in range(i):\n                if dp[j] and s[j:i] in words:\n                    dp[i] = True\n                    break\n        \n        return dp[-1]","title":"Word Break","url":"/submissions/detail/1014586880/","lang_name":"Python3","time":"6 months","timestamp":1691404030,"status":10,"runtime":"41 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"1111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]
