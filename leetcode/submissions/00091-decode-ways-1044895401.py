# Submission title: Decode Ways
# Submission url  : https://leetcode.com/problems/decode-ways/description/
# Submission url  : https://leetcode.com/submissions/detail/1044895401/
# Submission json : {"id":1044895401,"status_display":"Accepted","lang":"python3","question_id":91,"title_slug":"decode-ways","code":"class Solution:\n    def numDecodings(self, s: str) -> int:\n        char_count = len(s)\n\n        @cache\n        def dfs(i: int) -> int:\n            if i == char_count: \n                return 1\n            if s[i] == \"0\": \n                return 0\n            return dfs(i + 1) + (dfs(i + 2) if i + 1 < char_count and s[i:i+2] < \"27\" else 0)\n\n        return dfs(0)","title":"Decode Ways","url":"/submissions/detail/1044895401/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694279483,"status":10,"runtime":"44 ms","is_pending":"Not Pending","memory":"16.7 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def numDecodings(self, s: str) -> int:
        char_count = len(s)

        @cache
        def dfs(i: int) -> int:
            if i == char_count:
                return 1
            if s[i] == "0":
                return 0
            return dfs(i + 1) + (
                dfs(i + 2) if i + 1 < char_count and s[i : i + 2] < "27" else 0
            )

        return dfs(0)
