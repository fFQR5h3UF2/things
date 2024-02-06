# Submission title: for Daily Temperatures
# Submission url  : https://leetcode.com/submissions/detail/1161819645/
# Submission json : {"id": 1161819645, "status_display": "Accepted", "lang": "python3", "question_id": 739, "title_slug": "daily-temperatures", "code": "class Solution:\n    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:\n        temps_left = defaultdict(list)\n        to_pop = []\n        length = len(temperatures)\n        ans = [0] * length\n        for i in range(length):\n            temp = temperatures[i]\n            for temp_left, ids in temps_left.items():\n                if temp <= temp_left:\n                    continue\n                for id in ids:\n                    ans[id] = i - id\n                to_pop.append(temp_left)\n            temps_left[temp].append(i)\n            for temp in to_pop:\n                temps_left.pop(temp)\n            to_pop.clear()\n        \n        return ans", "title": "Daily Temperatures", "url": "/submissions/detail/1161819645/", "lang_name": "Python3", "time": "4\u00a0days, 6\u00a0hours", "timestamp": 1706688591, "status": 10, "runtime": "1098 ms", "is_pending": "Not Pending", "memory": "31.6 MB", "compare_result": "111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps_left = defaultdict(list)
        to_pop = []
        length = len(temperatures)
        ans = [0] * length
        for i in range(length):
            temp = temperatures[i]
            for temp_left, ids in temps_left.items():
                if temp <= temp_left:
                    continue
                for id in ids:
                    ans[id] = i - id
                to_pop.append(temp_left)
            temps_left[temp].append(i)
            for temp in to_pop:
                temps_left.pop(temp)
            to_pop.clear()

        return ans
