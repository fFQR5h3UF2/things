# Submission for Minimum Speed to Arrive on Time
# Submission url: https://leetcode.com/submissions/detail/1004740176/


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        length = len(dist)
        if hour >= length:
            return 1

        if hour <= length - 1:
            return -1

        min_speed = max(dist)
        distance, time_remaining = dist[-1], hour - length + 1
        speed = distance // time_remaining
        if speed <= min_speed:
            return min_speed

        return int(speed)
