# Submission title: String Compression II
# Submission url  : https://leetcode.com/problems/string-compression-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1130330804/
# Submission json : {"id":1130330804,"status_display":"Accepted","lang":"python3","question_id":1637,"title_slug":"string-compression-ii","code":"class Solution:\n    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:\n        n = len(s)\n        dp = [[9999] * 110 for _ in range(110)]\n        dp[0][0] = 0\n\n        for i in range(1, n + 1):\n            for j in range(0, k + 1):\n                cnt, del_ = 0, 0\n                for l in range(i, 0, -1):\n                    if s[l - 1] == s[i - 1]:\n                        cnt += 1\n                    else:\n                        del_ += 1\n\n                    if j - del_ >= 0:\n                        dp[i][j] = min(dp[i][j], dp[l - 1][j - del_] + 1 + (3 if cnt >= 100 else 2 if cnt >= 10 else 1 if cnt >= 2 else 0))\n\n                if j > 0:\n                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])\n\n        return dp[n][k]\n\n\n","title":"String Compression II","url":"/submissions/detail/1130330804/","lang_name":"Python3","time":"1 month, 1 week","timestamp":1703747555,"status":10,"runtime":"1916 ms","is_pending":"Not Pending","memory":"17.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[9999] * 110 for _ in range(110)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                cnt, del_ = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        del_ += 1

                    if j - del_ >= 0:
                        dp[i][j] = min(
                            dp[i][j],
                            dp[l - 1][j - del_]
                            + 1
                            + (
                                3
                                if cnt >= 100
                                else 2 if cnt >= 10 else 1 if cnt >= 2 else 0
                            ),
                        )

                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[n][k]
