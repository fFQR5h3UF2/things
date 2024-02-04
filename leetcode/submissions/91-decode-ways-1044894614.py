# Submission for 'Decode Ways'
# Submission url: https://leetcode.com/submissions/detail/1044894614/

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
            if i + 1 < char_count and s[i:i+2] < "27":
                ways_count += dfs(i + 2)
            return ways_count

        return dfs(0)
