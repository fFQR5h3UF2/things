# Submission title: for Longest Nice Substring
# Submission url  : https://leetcode.com/submissions/detail/1056159909/
# Submission json : {"id": 1056159909, "status_display": "Accepted", "lang": "python3", "question_id": 1873, "title_slug": "longest-nice-substring", "code": "class Solution:\n    def longestNiceSubstring(self, s: str) -> str:\n        sSet = set(s)\n        for i in range(len(s)):\n            if s[i].lower() not in sSet or s[i].upper() not in sSet:\n                lns1 = self.longestNiceSubstring(s[:i])\n                lns2 = self.longestNiceSubstring(s[i+1:])\n\n                return max(lns1, lns2, key=len)\n\n        return s\n", "title": "Longest Nice Substring", "url": "/submissions/detail/1056159909/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1695374062, "status": 10, "runtime": "46 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        sSet = set(s)
        for i in range(len(s)):
            if s[i].lower() not in sSet or s[i].upper() not in sSet:
                lns1 = self.longestNiceSubstring(s[:i])
                lns2 = self.longestNiceSubstring(s[i + 1 :])

                return max(lns1, lns2, key=len)

        return s
