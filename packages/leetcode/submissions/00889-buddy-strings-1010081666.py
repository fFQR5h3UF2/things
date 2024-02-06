# Submission title: for Buddy Strings
# Submission url  : https://leetcode.com/submissions/detail/1010081666/
# Submission json : {"id": 1010081666, "status_display": "Accepted", "lang": "python3", "question_id": 889, "title_slug": "buddy-strings", "code": "class Solution:\n    def buddyStrings(self, s: str, goal: str) -> bool:\n        length_1, length_2 = len(s), len(goal)\n\n        if length_1 != length_2:\n            return False\n        \n        if s == goal:\n            freq = defaultdict(int)\n            for char in s:\n                freq[char] += 1\n                if freq[char] == 2:\n                    return True\n            return False\n        \n        swap_1, swap_2 = -1, -1\n        \n        for i in range(length_1):\n            char_1, char_2 = s[i], goal[i]\n            \n            if char_1 == char_2:\n                continue\n            \n            if swap_1 == -1:\n                swap_1 = i\n            elif swap_2 == -1:\n                swap_2 = i\n            else:\n                return False\n            \n\n        return swap_2 != -1 and s[swap_1] == goal[swap_2] and s[swap_2] == goal[swap_1]", "title": "Buddy Strings", "url": "/submissions/detail/1010081666/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1690963207, "status": 10, "runtime": "41 ms", "is_pending": "Not Pending", "memory": "16.5 MB", "compare_result": "111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        length_1, length_2 = len(s), len(goal)

        if length_1 != length_2:
            return False

        if s == goal:
            freq = defaultdict(int)
            for char in s:
                freq[char] += 1
                if freq[char] == 2:
                    return True
            return False

        swap_1, swap_2 = -1, -1

        for i in range(length_1):
            char_1, char_2 = s[i], goal[i]

            if char_1 == char_2:
                continue

            if swap_1 == -1:
                swap_1 = i
            elif swap_2 == -1:
                swap_2 = i
            else:
                return False

        return swap_2 != -1 and s[swap_1] == goal[swap_2] and s[swap_2] == goal[swap_1]
