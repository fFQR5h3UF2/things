# Submission title: for Destination City
# Submission url  : https://leetcode.com/submissions/detail/1120177201/
# Submission json : {"id": 1120177201, "status_display": "Accepted", "lang": "python3", "question_id": 1547, "title_slug": "destination-city", "code": "class Solution:\n    def destCity(self, paths: List[List[str]]) -> str:\n        paths_from = set()\n        for path_from, path_to in paths:\n            paths_from.add(path_from)\n        \n        ans = \"\"\n        for _, path_to in paths:\n            if path_to not in paths_from:\n                ans = path_to\n                break\n        \n        return ans", "title": "Destination City", "url": "/submissions/detail/1120177201/", "lang_name": "Python3", "time": "1\u00a0month, 3\u00a0weeks", "timestamp": 1702626978, "status": 10, "runtime": "71 ms", "is_pending": "Not Pending", "memory": "16.5 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths_from = set()
        for path_from, path_to in paths:
            paths_from.add(path_from)

        ans = ""
        for _, path_to in paths:
            if path_to not in paths_from:
                ans = path_to
                break

        return ans
