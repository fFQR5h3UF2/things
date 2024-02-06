# Submission title: for Maximum Length of a Concatenated String with Unique Characters
# Submission url  : https://leetcode.com/submissions/detail/1154381353/
# Submission json : {"id": 1154381353, "status_display": "Accepted", "lang": "python3", "question_id": 1360, "title_slug": "maximum-length-of-a-concatenated-string-with-unique-characters", "code": "class Solution:\n    def maxLength(self, arr: List[str]) -> int:\n        cur = set()\n        length = len(arr)\n        max_length = 0\n\n        def backtrack(start: int) -> None:\n            nonlocal max_length \n            \n            for i in range(start, length):\n                new_subs = arr[i]\n                new = set(new_subs)\n                if len(new_subs) != len(new) or len(cur.intersection(new)) != 0:\n                    continue\n                cur.update(new)\n                backtrack(i + 1)\n                cur.difference_update(new)\n\n            max_length = max(max_length, len(cur))\n\n        backtrack(0)\n\n        return max_length\n", "title": "Maximum Length of a Concatenated String with Unique Characters", "url": "/submissions/detail/1154381353/", "lang_name": "Python3", "time": "1\u00a0week, 5\u00a0days", "timestamp": 1705996478, "status": 10, "runtime": "60 ms", "is_pending": "Not Pending", "memory": "16.7 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        cur = set()
        length = len(arr)
        max_length = 0

        def backtrack(start: int) -> None:
            nonlocal max_length

            for i in range(start, length):
                new_subs = arr[i]
                new = set(new_subs)
                if len(new_subs) != len(new) or len(cur.intersection(new)) != 0:
                    continue
                cur.update(new)
                backtrack(i + 1)
                cur.difference_update(new)

            max_length = max(max_length, len(cur))

        backtrack(0)

        return max_length
