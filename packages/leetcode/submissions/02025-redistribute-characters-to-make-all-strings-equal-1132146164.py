# Submission title: for Redistribute Characters to Make All Strings Equal
# Submission url  : https://leetcode.com/submissions/detail/1132146164/
# Submission json : {"id": 1132146164, "status_display": "Accepted", "lang": "python3", "question_id": 2025, "title_slug": "redistribute-characters-to-make-all-strings-equal", "code": "class Solution:\n    def makeEqual(self, words: List[str]) -> bool:\n        counts = defaultdict(int)\n        for word in words:\n            for c in word:\n                counts[c] += 1\n        \n        n = len(words)\n        for val in counts.values():\n            if val % n != 0:\n                return False\n        \n        return True", "title": "Redistribute Characters to Make All Strings Equal", "url": "/submissions/detail/1132146164/", "lang_name": "Python3", "time": "1\u00a0month", "timestamp": 1703935357, "status": 10, "runtime": "57 ms", "is_pending": "Not Pending", "memory": "17.4 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = defaultdict(int)
        for word in words:
            for c in word:
                counts[c] += 1

        n = len(words)
        for val in counts.values():
            if val % n != 0:
                return False

        return True
