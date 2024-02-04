# Submission title: for Longest Common Prefix
# Submission url  : https://leetcode.com/submissions/detail/993697050/
# Submission json : {"id": 993697050, "status_display": "Accepted", "lang": "python3", "question_id": 14, "title_slug": "longest-common-prefix", "code": "class Solution:\n    \n    def longestCommonPrefix(self, strs: List[str]) -> str:\n        if len(strs) == 1:\n            return strs[0]\n\n        min_length = min([len(string) for string in strs])\n        prefix = strs[0][0:min_length]\n        for string in strs:\n            if not prefix:\n                return \"\"\n            \n            while not string.startswith(prefix):\n                prefix = prefix[0:-1]\n            \n        return prefix", "title": "Longest Common Prefix", "url": "/submissions/detail/993697050/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689271071, "status": 10, "runtime": "48 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        min_length = min([len(string) for string in strs])
        prefix = strs[0][0:min_length]
        for string in strs:
            if not prefix:
                return ""

            while not string.startswith(prefix):
                prefix = prefix[0:-1]

        return prefix
