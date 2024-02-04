# Submission for Minimum Speed to Arrive on Time
# Submission url: https://leetcode.com/submissions/detail/1004766449/


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        length = len(dist)
        if hour >= sum(dist):
            return 1

        if hour <= length - 1:
            return -1

        last_distance = length - 1
        distance, time_remaining = dist[-1], hour - length + 1
        max_speed = max(max(dist), distance // time_remaining + 1)
        min_speed = 1
        result = -1
        while min_speed <= max_speed:
            speed = min_speed + (max_speed - min_speed) // 2
            time = 0
            for i in range(0, length):
                distance = dist[i]
                if i == last_distance:
                    time += distance / speed
                else:
                    time += distance // speed + 1

                if time > hour:
                    break

            if time > hour:
                min_speed = speed + 1
            else:
                max_speed = speed - 1

        return max_speed
