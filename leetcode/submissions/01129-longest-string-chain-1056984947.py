# Submission title: Longest String Chain
# Submission url  : https://leetcode.com/problems/longest-string-chain/description/
# Submission url  : https://leetcode.com/submissions/detail/1056984947/
# Submission json : {"id":1056984947,"status_display":"Accepted","lang":"python3","question_id":1129,"title_slug":"longest-string-chain","code":"class Solution:\n    def longestStrChain(self, words: List[str]) -> int:\n        words.sort(key=len)\n        dp = {}\n        max_chain = 0\n        for word in words:\n            dp[word] = 1\n            for i in range(len(word)):\n                prev_word = word[:i] + word[i+1:]\n                if prev_word in dp:\n                    dp[word] = max(dp[word], dp[prev_word] + 1)\n            max_chain = max(max_chain, dp[word])\n        return max_chain","title":"Longest String Chain","url":"/submissions/detail/1056984947/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695464340,"status":10,"runtime":"119 ms","is_pending":"Not Pending","memory":"16.8 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        max_chain = 0
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i + 1 :]
                if prev_word in dp:
                    dp[word] = max(dp[word], dp[prev_word] + 1)
            max_chain = max(max_chain, dp[word])
        return max_chain
