# Submission title: Minimum Number of Taps to Open to Water a Garden
# Submission url  : https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/
# Submission url  : https://leetcode.com/submissions/detail/1036785038/
# Submission json : {"id":1036785038,"status_display":"Accepted","lang":"python3","question_id":1451,"title_slug":"minimum-number-of-taps-to-open-to-water-a-garden","code":"class Solution:\n    def minTaps(self, n: int, ranges: List[int]) -> int:\n        inf = float(\"inf\")\n        dp = [inf] * (n + 1)\n        dp[0] = 0\n        \n        for i in range(n + 1):\n            cur_range = ranges[i]\n            tap_start, tap_end = max(0, i - cur_range), min(n, i + cur_range)\n            \n            for j in range(tap_start, tap_end + 1):\n                dp[tap_end] = min(dp[tap_end], dp[j] + 1)\n        \n        min_taps = dp[n]\n        return -1 if min_taps == inf else min_taps ","title":"Minimum Number of Taps to Open to Water a Garden","url":"/submissions/detail/1036785038/","lang_name":"Python3","time":"5 months, 1 week","timestamp":1693484983,"status":10,"runtime":"458 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"11111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        inf = float("inf")
        dp = [inf] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            cur_range = ranges[i]
            tap_start, tap_end = max(0, i - cur_range), min(n, i + cur_range)

            for j in range(tap_start, tap_end + 1):
                dp[tap_end] = min(dp[tap_end], dp[j] + 1)

        min_taps = dp[n]
        return -1 if min_taps == inf else min_taps
