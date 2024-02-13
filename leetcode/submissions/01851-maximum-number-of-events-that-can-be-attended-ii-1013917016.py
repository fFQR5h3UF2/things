# Submission title: Maximum Number of Events That Can Be Attended II
# Submission url  : https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1013917016/
# Submission json : {"id":1013917016,"status_display":"Accepted","lang":"python3","question_id":1851,"title_slug":"maximum-number-of-events-that-can-be-attended-ii","code":"class Solution:\n    def maxValue(self, events: List[List[int]], k: int) -> int:        \n        events.sort()\n        n = len(events)\n        starts = [start for start, end, value in events]\n        dp = [[-1] * n for _ in range(k + 1)]\n        \n        def dfs(cur_index, count):\n            if count == 0 or cur_index == n:\n                return 0\n            if dp[count][cur_index] != -1:\n                return dp[count][cur_index]\n\n            # Find the nearest available event after attending event 0.\n\n            next_index = bisect_right(starts, events[cur_index][1])\n            dp[count][cur_index] = max(dfs(cur_index + 1, count), events[cur_index][2] + dfs(next_index, count - 1))\n            return dp[count][cur_index]\n        \n        return dfs(0, k)","title":"Maximum Number of Events That Can Be Attended II","url":"/submissions/detail/1013917016/","lang_name":"Python3","time":"6 months","timestamp":1691334011,"status":10,"runtime":"1228 ms","is_pending":"Not Pending","memory":"159.9 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        starts = [start for start, end, value in events]
        dp = [[-1] * n for _ in range(k + 1)]

        def dfs(cur_index, count):
            if count == 0 or cur_index == n:
                return 0
            if dp[count][cur_index] != -1:
                return dp[count][cur_index]

            # Find the nearest available event after attending event 0.

            next_index = bisect_right(starts, events[cur_index][1])
            dp[count][cur_index] = max(
                dfs(cur_index + 1, count),
                events[cur_index][2] + dfs(next_index, count - 1),
            )
            return dp[count][cur_index]

        return dfs(0, k)
