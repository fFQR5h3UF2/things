# Submission title: for Assign Cookies
# Submission url  : https://leetcode.com/submissions/detail/1002505295/
# Submission json : {"id": 1002505295, "status_display": "Accepted", "lang": "python3", "question_id": 455, "title_slug": "assign-cookies", "code": "class Solution:\n    def findContentChildren(self, g: List[int], s: List[int]) -> int:\n        g.sort(reverse=True)\n        s.sort(reverse=True)\n        count = 0\n        cookie_index = 0\n        cookie_count = len(s)\n        for greed in g:\n            if cookie_index >= cookie_count or greed > s[cookie_index]:\n                continue\n\n            count += 1\n            cookie_index += 1\n            \n        return count", "title": "Assign Cookies", "url": "/submissions/detail/1002505295/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690191882, "status": 10, "runtime": "175 ms", "is_pending": "Not Pending", "memory": "18.3 MB", "compare_result": "111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        count = 0
        cookie_index = 0
        cookie_count = len(s)
        for greed in g:
            if cookie_index >= cookie_count or greed > s[cookie_index]:
                continue

            count += 1
            cookie_index += 1

        return count
