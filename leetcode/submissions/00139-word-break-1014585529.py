# Submission title: Word Break
# Submission url  : https://leetcode.com/problems/word-break/description/
# Submission url  : https://leetcode.com/submissions/detail/1014585529/
# Submission json : {"id":1014585529,"status_display":"Accepted","lang":"python3","question_id":139,"title_slug":"word-break","code":"class Solution:\n    def wordBreak(self, s: str, wordDict: List[str]) -> bool:\n        @cache\n        def dp(i):\n            if i < 0: \n                return True\n\n            for word in wordDict:\n                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):\n                    return True\n            \n            return False\n        \n        return dp(len(s) - 1)","title":"Word Break","url":"/submissions/detail/1014585529/","lang_name":"Python3","time":"6 months","timestamp":1691403903,"status":10,"runtime":"40 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"1111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i < 0:
                return True

            for word in wordDict:
                if s[i - len(word) + 1 : i + 1] == word and dp(i - len(word)):
                    return True

            return False

        return dp(len(s) - 1)
