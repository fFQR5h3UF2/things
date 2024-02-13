# Submission title: Maximum Running Time of N Computers
# Submission url  : https://leetcode.com/problems/maximum-running-time-of-n-computers/description/
# Submission url  : https://leetcode.com/submissions/detail/1005165062/
# Submission json : {"id":1005165062,"status_display":"Accepted","lang":"python3","question_id":2263,"title_slug":"maximum-running-time-of-n-computers","code":"class Solution:\n    # n = 2, batteries = [3,3,3], Output: 4\n    # n = 2, batteries = [1,1,1,1], Output: 2\n    def maxRunTime(self, n: int, batteries: List[int]) -> int:\n        length = len(batteries)\n\n        if length < n:\n            return 0\n        \n        if length == n:\n            return min(batteries)\n\n        batteries.sort()\n        extra = sum(batteries[:-n])\n        live = batteries[-n:]\n\n        \n        # We increase the total running time using 'extra' by increasing \n        # the running time of the computer with the smallest battery.\n        for i in range(n - 1):\n            # If the target running time is between live[i] and live[i + 1].\n            if extra // (i + 1) < live[i + 1] - live[i]:\n                return live[i] + extra // (i + 1)\n            \n            # Reduce 'extra' by the total power used.\n            extra -= (i + 1) * (live[i + 1] - live[i])\n        \n        # If there is power left, we can increase the running time \n        # of all computers.\n        return live[-1] + extra // n","title":"Maximum Running Time of N Computers","url":"/submissions/detail/1005165062/","lang_name":"Python3","time":"6 months, 1 week","timestamp":1690446512,"status":10,"runtime":"567 ms","is_pending":"Not Pending","memory":"30.8 MB","compare_result":"1111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    # n = 2, batteries = [3,3,3], Output: 4
    # n = 2, batteries = [1,1,1,1], Output: 2
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        length = len(batteries)

        if length < n:
            return 0

        if length == n:
            return min(batteries)

        batteries.sort()
        extra = sum(batteries[:-n])
        live = batteries[-n:]

        # We increase the total running time using 'extra' by increasing
        # the running time of the computer with the smallest battery.
        for i in range(n - 1):
            # If the target running time is between live[i] and live[i + 1].
            if extra // (i + 1) < live[i + 1] - live[i]:
                return live[i] + extra // (i + 1)

            # Reduce 'extra' by the total power used.
            extra -= (i + 1) * (live[i + 1] - live[i])

        # If there is power left, we can increase the running time
        # of all computers.
        return live[-1] + extra // n
