# Submission title: for Max Points on a Line
# Submission url  : https://leetcode.com/submissions/detail/1057824838/
# Submission json : {"id": 1057824838, "status_display": "Accepted", "lang": "python3", "question_id": 149, "title_slug": "max-points-on-a-line", "code": "class Solution:\n    def maxPoints(self, points: List[List[int]]) -> int:\n        lines = defaultdict(set)\n        length = len(points)\n        if length < 3:\n            return length\n        for i in range(length):\n            x1, y1 = points[i]\n            for j in range(i + 1, length):\n                x2, y2 = points[j]\n                k1, k2 = None, None\n                if y1 == y2:\n                    k2 = y1\n                elif x1 == x2:\n                    k1 = x1\n                else: \n                    k1 = (y2 - y1) / (x2 - x1)\n                    k2 = y1 - k1 * x1\n                lines[(k1, k2)].update(((x1, y1), (x2, y2)))\n        return max((len(points) for points in lines.values()), default=0)\n", "title": "Max Points on a Line", "url": "/submissions/detail/1057824838/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695551188, "status": 10, "runtime": "103 ms", "is_pending": "Not Pending", "memory": "40.8 MB", "compare_result": "11111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = defaultdict(set)
        length = len(points)
        if length < 3:
            return length
        for i in range(length):
            x1, y1 = points[i]
            for j in range(i + 1, length):
                x2, y2 = points[j]
                k1, k2 = None, None
                if y1 == y2:
                    k2 = y1
                elif x1 == x2:
                    k1 = x1
                else:
                    k1 = (y2 - y1) / (x2 - x1)
                    k2 = y1 - k1 * x1
                lines[(k1, k2)].update(((x1, y1), (x2, y2)))
        return max((len(points) for points in lines.values()), default=0)
