# Submission title: for Maximum Profit in Job Scheduling
# Submission url  : https://leetcode.com/submissions/detail/1139390559/
# Submission json : {"id": 1139390559, "status_display": "Accepted", "lang": "python3", "question_id": 1352, "title_slug": "maximum-profit-in-job-scheduling", "code": "class Solution:\n    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:\n        jobs = sorted(zip(endTime, startTime, profit))\n      \n        number_of_jobs = len(profit)\n      \n        dp = [0] * (number_of_jobs + 1)\n      \n        for i, (current_end_time, current_start_time, current_profit) in enumerate(jobs):\n            index = bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])\n            dp[i + 1] = max(dp[i], dp[index] + current_profit)\n      \n        return dp[number_of_jobs]", "title": "Maximum Profit in Job Scheduling", "url": "/submissions/detail/1139390559/", "lang_name": "Python3", "time": "4\u00a0weeks", "timestamp": 1704619569, "status": 10, "runtime": "603 ms", "is_pending": "Not Pending", "memory": "29.3 MB", "compare_result": "1111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(endTime, startTime, profit))

        number_of_jobs = len(profit)

        dp = [0] * (number_of_jobs + 1)

        for i, (current_end_time, current_start_time, current_profit) in enumerate(
            jobs
        ):
            index = bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[index] + current_profit)

        return dp[number_of_jobs]
