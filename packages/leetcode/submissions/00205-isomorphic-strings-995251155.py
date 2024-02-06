# Submission title: for Isomorphic Strings
# Submission url  : https://leetcode.com/submissions/detail/995251155/
# Submission json : {"id": 995251155, "status_display": "Accepted", "lang": "python3", "question_id": 205, "title_slug": "isomorphic-strings", "code": "class Solution:\n    def isIsomorphic(self, s: str, t: str) -> bool:\n        s_length, t_length = len(s), len(t)\n        if s_length != t_length:\n            return False\n        \n        s_to_t = {}\n        t_to_s = {}\n        for i, s_symbol in enumerate(s):\n            t_symbol = t[i]\n\n            if s_symbol not in s_to_t and t_symbol not in t_to_s:\n                s_to_t[s_symbol] = t_symbol\n                t_to_s[t_symbol] = s_symbol\n            elif s_symbol in s_to_t and s_to_t[s_symbol] == t_symbol:\n                continue\n            else:\n                return False\n                \n        return True", "title": "Isomorphic Strings", "url": "/submissions/detail/995251155/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689443610, "status": 10, "runtime": "59 ms", "is_pending": "Not Pending", "memory": "16.6 MB", "compare_result": "11111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_length, t_length = len(s), len(t)
        if s_length != t_length:
            return False

        s_to_t = {}
        t_to_s = {}
        for i, s_symbol in enumerate(s):
            t_symbol = t[i]

            if s_symbol not in s_to_t and t_symbol not in t_to_s:
                s_to_t[s_symbol] = t_symbol
                t_to_s[t_symbol] = s_symbol
            elif s_symbol in s_to_t and s_to_t[s_symbol] == t_symbol:
                continue
            else:
                return False

        return True
