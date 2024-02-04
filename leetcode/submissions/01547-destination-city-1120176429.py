# Submission title: for Destination City
# Submission url  : https://leetcode.com/submissions/detail/1120176429/
# Submission json : {"id": 1120176429, "status_display": "Accepted", "lang": "python3", "question_id": 1547, "title_slug": "destination-city", "code": "class Solution:\n    def destCity(self, paths: List[List[str]]) -> str:\n        paths_from, paths_to = set(), set()\n        for path_from, path_to in paths:\n            paths_from.add(path_from)\n            paths_to.add(path_to)\n        \n        return (paths_to - paths_from).pop()", "title": "Destination City", "url": "/submissions/detail/1120176429/", "lang_name": "Python3", "time": "1\u00a0month, 3\u00a0weeks", "timestamp": 1702626891, "status": 10, "runtime": "67 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths_from, paths_to = set(), set()
        for path_from, path_to in paths:
            paths_from.add(path_from)
            paths_to.add(path_to)

        return (paths_to - paths_from).pop()
