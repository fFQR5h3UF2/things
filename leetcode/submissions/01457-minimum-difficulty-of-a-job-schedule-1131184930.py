# Submission title: Minimum Difficulty of a Job Schedule
# Submission url  : https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/
# Submission url  : https://leetcode.com/submissions/detail/1131184930/
# Submission json : {"id":1131184930,"status_display":"Accepted","lang":"python3","question_id":1457,"title_slug":"minimum-difficulty-of-a-job-schedule","code":"class Solution:\n    def minDifficulty(self, jobDifficulty, days):\n        length = len(jobDifficulty)\n        if days > length:\n            return -1\n\n        min_difficulties = [[float('inf')] * length for _ in range(days)]\n\n        max_diff = 0\n        i = 0\n        while i <= length - days:\n            max_diff = max(max_diff, jobDifficulty[i])\n            min_difficulties[0][i] = max_diff\n            i += 1\n\n        current_day = 1\n        while current_day < days:\n            to = current_day\n            while to <= length - days + current_day:\n                current_job_difficulty = jobDifficulty[to]\n                result = float('inf')\n                j = to - 1\n                while j >= current_day - 1:\n                    result = min(result, min_difficulties[current_day - 1][j] + current_job_difficulty)\n                    current_job_difficulty = max(current_job_difficulty, jobDifficulty[j])\n                    j -= 1\n                min_difficulties[current_day][to] = result\n                to += 1\n            current_day += 1\n\n        return min_difficulties[days - 1][length - 1]\n\n\n","title":"Minimum Difficulty of a Job Schedule","url":"/submissions/detail/1131184930/","lang_name":"Python3","time":"1 month, 1 week","timestamp":1703833766,"status":10,"runtime":"805 ms","is_pending":"Not Pending","memory":"17.5 MB","compare_result":"1111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minDifficulty(self, jobDifficulty, days):
        length = len(jobDifficulty)
        if days > length:
            return -1

        min_difficulties = [[float("inf")] * length for _ in range(days)]

        max_diff = 0
        i = 0
        while i <= length - days:
            max_diff = max(max_diff, jobDifficulty[i])
            min_difficulties[0][i] = max_diff
            i += 1

        current_day = 1
        while current_day < days:
            to = current_day
            while to <= length - days + current_day:
                current_job_difficulty = jobDifficulty[to]
                result = float("inf")
                j = to - 1
                while j >= current_day - 1:
                    result = min(
                        result,
                        min_difficulties[current_day - 1][j] + current_job_difficulty,
                    )
                    current_job_difficulty = max(
                        current_job_difficulty, jobDifficulty[j]
                    )
                    j -= 1
                min_difficulties[current_day][to] = result
                to += 1
            current_day += 1

        return min_difficulties[days - 1][length - 1]
