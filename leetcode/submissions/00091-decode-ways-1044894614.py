# Submission title: Decode Ways
# Submission url  : https://leetcode.com/problems/decode-ways/description/
# Submission url  : https://leetcode.com/submissions/detail/1044894614/
# Submission json : {"id":1044894614,"status_display":"Accepted","lang":"python3","question_id":91,"title_slug":"decode-ways","code":"class Solution:\n    def numDecodings(self, s: str) -> int:\n        char_count = len(s)\n\n        @cache\n        def dfs(i: int) -> int:\n            if i == char_count: \n                return 1\n            if s[i] == \"0\": \n                return 0\n            ways_count = dfs(i + 1)\n            if i + 1 < char_count and s[i:i+2] < \"27\":\n                ways_count += dfs(i + 2)\n            return ways_count\n\n        return dfs(0)","title":"Decode Ways","url":"/submissions/detail/1044894614/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694279418,"status":10,"runtime":"39 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def numDecodings(self, s: str) -> int:
        char_count = len(s)

        @cache
        def dfs(i: int) -> int:
            if i == char_count:
                return 1
            if s[i] == "0":
                return 0
            ways_count = dfs(i + 1)
            if i + 1 < char_count and s[i : i + 2] < "27":
                ways_count += dfs(i + 2)
            return ways_count

        return dfs(0)
