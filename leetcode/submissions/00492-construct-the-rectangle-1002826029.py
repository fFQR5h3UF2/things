# Submission title: for Construct the Rectangle
# Submission url  : https://leetcode.com/submissions/detail/1002826029/
# Submission json : {"id": 1002826029, "status_display": "Accepted", "lang": "python3", "question_id": 492, "title_slug": "construct-the-rectangle", "code": "class Solution:\n    def constructRectangle(self, area: int) -> List[int]:\n        return next([area//width, width] \n                    for width in range(int(area**0.5), 0, -1) \n                    if area % width == 0)", "title": "Construct the Rectangle", "url": "/submissions/detail/1002826029/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690218478, "status": 10, "runtime": "44 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        return next(
            [area // width, width]
            for width in range(int(area**0.5), 0, -1)
            if area % width == 0
        )
