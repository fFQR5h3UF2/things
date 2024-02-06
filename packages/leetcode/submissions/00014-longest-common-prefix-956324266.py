# Submission title: for Longest Common Prefix
# Submission url  : https://leetcode.com/submissions/detail/956324266/
# Submission json : {"id": 956324266, "status_display": "Accepted", "lang": "python3", "question_id": 14, "title_slug": "longest-common-prefix", "code": "class Solution:\n    def longestCommonPrefix(self, strs: List[str]) -> str:\n        answer = []\n        strings = sorted(strs)\n        first = strings[0]\n        last = strings[-1]\n        min_length = min(len(first), len(last))\n        for i in range(min_length):\n            first_symbol = first[i]\n            last_symbol = last[i]\n            if first_symbol == last_symbol:\n                answer.append(first_symbol)\n                continue\n            \n            return \"\".join(answer)\n\n        return \"\".join(answer)\n\n\n        ", "title": "Longest Common Prefix", "url": "/submissions/detail/956324266/", "lang_name": "Python3", "time": "8\u00a0months, 2\u00a0weeks", "timestamp": 1684917421, "status": 10, "runtime": "54 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = []
        strings = sorted(strs)
        first = strings[0]
        last = strings[-1]
        min_length = min(len(first), len(last))
        for i in range(min_length):
            first_symbol = first[i]
            last_symbol = last[i]
            if first_symbol == last_symbol:
                answer.append(first_symbol)
                continue

            return "".join(answer)

        return "".join(answer)
