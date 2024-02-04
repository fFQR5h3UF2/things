# Submission for Minimum Speed to Arrive on Time
# Submission url: https://leetcode.com/submissions/detail/1004736125/


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        length = len(dist)
        if hour >= length:
            return 1

        if hour <= length - 1:
            return -1

        distance, time_remaining = dist[-1], hour - length + 1
        result = distance // time_remaining
        if not hour.is_integer():
            result += 1

        return int(result)
