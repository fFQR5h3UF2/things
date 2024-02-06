# Submission title: for Asteroid Collision
# Submission url  : https://leetcode.com/submissions/detail/999173927/
# Submission json : {"id": 999173927, "status_display": "Accepted", "lang": "python3", "question_id": 735, "title_slug": "asteroid-collision", "code": "class Solution:\n    def asteroidCollision(self, asteroids: List[int]) -> List[int]:\n        length = len(asteroids)\n\n        if length < 2:\n            return asteroids\n\n        stack = [asteroids[0]]\n        for i in range(1, length):\n            asteroid = asteroids[i]\n            asteroid_last = stack[-1] if stack else 0\n            stack.append(asteroid)\n\n            if asteroid > 0 or (\n                asteroid < 0 and asteroid_last < 0\n            ):\n                continue\n\n            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:\n                last, prev = abs(stack[-1]), abs(stack[-2])\n                if last == prev:\n                    stack.pop()\n                elif last > prev:\n                    stack[-1], stack[-2] = stack[-2], stack[-1]\n\n                stack.pop()\n\n        return stack", "title": "Asteroid Collision", "url": "/submissions/detail/999173927/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689842510, "status": 10, "runtime": "117 ms", "is_pending": "Not Pending", "memory": "17.6 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        length = len(asteroids)

        if length < 2:
            return asteroids

        stack = [asteroids[0]]
        for i in range(1, length):
            asteroid = asteroids[i]
            asteroid_last = stack[-1] if stack else 0
            stack.append(asteroid)

            if asteroid > 0 or (asteroid < 0 and asteroid_last < 0):
                continue

            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                last, prev = abs(stack[-1]), abs(stack[-2])
                if last == prev:
                    stack.pop()
                elif last > prev:
                    stack[-1], stack[-2] = stack[-2], stack[-1]

                stack.pop()

        return stack
