# Submission title: for Assign Cookies
# Submission url  : https://leetcode.com/submissions/detail/1133719850/
# Submission json : {"id": 1133719850, "status_display": "Accepted", "lang": "python3", "question_id": 455, "title_slug": "assign-cookies", "code": "class Solution:\n    def findContentChildren(self, g: List[int], s: List[int]) -> int:\n        g.sort()\n        s.sort()\n        content_children = 0\n        cookie_index = 0\n        while cookie_index < len(s) and content_children < len(g):\n            if s[cookie_index] >= g[content_children]:\n                content_children += 1\n            cookie_index += 1\n        return content_children", "title": "Assign Cookies", "url": "/submissions/detail/1133719850/", "lang_name": "Python3", "time": "1\u00a0month", "timestamp": 1704114642, "status": 10, "runtime": "137 ms", "is_pending": "Not Pending", "memory": "19.2 MB", "compare_result": "111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content_children = 0
        cookie_index = 0
        while cookie_index < len(s) and content_children < len(g):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        return content_children
