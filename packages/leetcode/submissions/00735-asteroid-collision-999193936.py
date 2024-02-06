# Submission title: for Asteroid Collision
# Submission url  : https://leetcode.com/submissions/detail/999193936/
# Submission json : {"id": 999193936, "status_display": "Accepted", "lang": "python3", "question_id": 735, "title_slug": "asteroid-collision", "code": "class Solution:\n    def asteroidCollision(self, asteroids: List[int]) -> List[int]:\n        stack = []\n        for asteroid in asteroids:\n            if asteroid > 0:\n                stack.append(asteroid)\n                continue\n            \n            asteroid_abs = abs(asteroid)\n            while stack and stack[-1] > 0 and stack[-1] < asteroid_abs:\n                stack.pop()\n            \n            if stack and stack[-1] == asteroid_abs:\n                stack.pop()\n            elif not stack or stack[-1] < 0:\n                stack.append(asteroid)\n\n        return stack", "title": "Asteroid Collision", "url": "/submissions/detail/999193936/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689844341, "status": 10, "runtime": "118 ms", "is_pending": "Not Pending", "memory": "17.5 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue

            asteroid_abs = abs(asteroid)
            while stack and stack[-1] > 0 and stack[-1] < asteroid_abs:
                stack.pop()

            if stack and stack[-1] == asteroid_abs:
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(asteroid)

        return stack
