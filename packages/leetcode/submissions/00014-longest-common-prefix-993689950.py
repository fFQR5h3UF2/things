# Submission title: for Longest Common Prefix
# Submission url  : https://leetcode.com/submissions/detail/993689950/
# Submission json : {"id": 993689950, "status_display": "Accepted", "lang": "python3", "question_id": 14, "title_slug": "longest-common-prefix", "code": "class Solution:\n    \n    def longestCommonPrefix(self, strs: List[str]) -> str:\n        if len(strs) == 1:\n            return strs[0]\n\n        min_length = min([len(string) for string in strs])\n        for i in range(min_length, -1, -1):\n            current = strs[0][0:i+1]\n            for string in strs[1:]:\n                if string[0:i+1] != current:\n                    break\n            else:\n                return current\n\n        return \"\"    ", "title": "Longest Common Prefix", "url": "/submissions/detail/993689950/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689270542, "status": 10, "runtime": "47 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        min_length = min([len(string) for string in strs])
        for i in range(min_length, -1, -1):
            current = strs[0][0 : i + 1]
            for string in strs[1:]:
                if string[0 : i + 1] != current:
                    break
            else:
                return current

        return ""
