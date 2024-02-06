# Submission title: for Remove Duplicate Letters
# Submission url  : https://leetcode.com/submissions/detail/1059570814/
# Submission json : {"id": 1059570814, "status_display": "Accepted", "lang": "python3", "question_id": 316, "title_slug": "remove-duplicate-letters", "code": "class Solution:\n    def removeDuplicateLetters(self, s: str) -> str:\n        stack = []\n        seen = set() \n        last_occ = {char: i for i, char in enumerate(s)}\n        \n        for i, char in enumerate(s):\n            if char in seen:\n                continue\n                \n            while stack and char < stack[-1] and i < last_occ[stack[-1]]:\n                seen.discard(stack.pop())\n            seen.add(char)\n            stack.append(char)\n        \n        return ''.join(stack)", "title": "Remove Duplicate Letters", "url": "/submissions/detail/1059570814/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695724989, "status": 10, "runtime": "41 ms", "is_pending": "Not Pending", "memory": "16.2 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occ = {char: i for i, char in enumerate(s)}

        for i, char in enumerate(s):
            if char in seen:
                continue

            while stack and char < stack[-1] and i < last_occ[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(char)
            stack.append(char)

        return "".join(stack)
