# Submission title: for Widest Vertical Area Between Two Points Containing No Points
# Submission url  : https://leetcode.com/submissions/detail/1124812187/
# Submission json : {"id": 1124812187, "status_display": "Accepted", "lang": "python3", "question_id": 1742, "title_slug": "widest-vertical-area-between-two-points-containing-no-points", "code": "class Solution:\n    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:\n        points.sort(key=lambda x: x[0])\n\n        max_width = 0\n\n        for i in range(1, len(points)):\n            width = points[i][0] - points[i-1][0]\n            max_width = max(max_width, width)\n\n        return max_width", "title": "Widest Vertical Area Between Two Points Containing No Points", "url": "/submissions/detail/1124812187/", "lang_name": "Python3", "time": "1\u00a0month, 2\u00a0weeks", "timestamp": 1703137353, "status": 10, "runtime": "741 ms", "is_pending": "Not Pending", "memory": "60.1 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        max_width = 0

        for i in range(1, len(points)):
            width = points[i][0] - points[i - 1][0]
            max_width = max(max_width, width)

        return max_width
