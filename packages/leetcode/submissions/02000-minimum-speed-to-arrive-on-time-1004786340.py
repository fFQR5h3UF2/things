# Submission title: for Minimum Speed to Arrive on Time
# Submission url  : https://leetcode.com/submissions/detail/1004786340/
# Submission json : {"id": 1004786340, "status_display": "Accepted", "lang": "python3", "question_id": 2000, "title_slug": "minimum-speed-to-arrive-on-time", "code": "class Solution:\n    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:\n        length = len(dist)\n        if hour >= sum(dist):\n            return 1\n        \n        if hour <= length - 1:\n            return -1\n        \n        time_remaining = hour - length + 1\n        max_speed = int(max(\n            max(dist), dist[-1] // time_remaining + 1\n        ))\n        min_speed = 1\n        result = -1\n        while min_speed < max_speed:\n            speed = min_speed + (max_speed - min_speed) // 2\n            time = dist[-1] / speed + sum(\n                (distance + speed - 1) // speed \n                for distance in dist[:-1]\n            )\n            \n            if time > hour:\n                min_speed = speed + 1\n            else:\n                max_speed = speed\n        \n        return min_speed", "title": "Minimum Speed to Arrive on Time", "url": "/submissions/detail/1004786340/", "lang_name": "Python3", "time": "6\u00a0months, 1\u00a0week", "timestamp": 1690401415, "status": 10, "runtime": "2140 ms", "is_pending": "Not Pending", "memory": "30.3 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        length = len(dist)
        if hour >= sum(dist):
            return 1

        if hour <= length - 1:
            return -1

        time_remaining = hour - length + 1
        max_speed = int(max(max(dist), dist[-1] // time_remaining + 1))
        min_speed = 1
        result = -1
        while min_speed < max_speed:
            speed = min_speed + (max_speed - min_speed) // 2
            time = dist[-1] / speed + sum(
                (distance + speed - 1) // speed for distance in dist[:-1]
            )

            if time > hour:
                min_speed = speed + 1
            else:
                max_speed = speed

        return min_speed
