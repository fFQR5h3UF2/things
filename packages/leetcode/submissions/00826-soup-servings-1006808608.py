# Submission title: for Soup Servings
# Submission url  : https://leetcode.com/submissions/detail/1006808608/
# Submission json : {"id": 1006808608, "status_display": "Accepted", "lang": "python3", "question_id": 826, "title_slug": "soup-servings", "code": "class Solution:\n    def soupServings(self, n: int) -> float:\n        servings = ceil(n / 25)\n\n        states = defaultdict(dict)\n        moves = [[-4, 0], [-3, -1], [-2, -2], [-1, -3]]\n    \n        @cache\n        def calculate(soup_a: int, soup_b: int) -> float:\n            if soup_a <= 0 and soup_b <= 0:\n                return 0.5\n            if soup_a <= 0:\n                return 1.0\n            if soup_b <= 0:\n                return 0.0\n            if soup_a in states and soup_b in states[soup_a]:\n                return states[soup_a][soup_b]\n            \n            state = sum(calculate(soup_a + move[0], soup_b + move[1]) for move in moves) / 4.0\n            states[soup_a][soup_b] = state\n\n            return state\n\n        max_probability = 1 - 1e-5\n\n        for serving in range(1, servings + 1):\n            state = calculate(serving, serving)\n            if state > max_probability:\n                return 1.0\n        \n        return calculate(servings, servings)\n       \n\n", "title": "Soup Servings", "url": "/submissions/detail/1006808608/", "lang_name": "Python3", "time": "6\u00a0months, 1\u00a0week", "timestamp": 1690626272, "status": 10, "runtime": "346 ms", "is_pending": "Not Pending", "memory": "40 MB", "compare_result": "11111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def soupServings(self, n: int) -> float:
        servings = ceil(n / 25)

        states = defaultdict(dict)
        moves = [[-4, 0], [-3, -1], [-2, -2], [-1, -3]]

        @cache
        def calculate(soup_a: int, soup_b: int) -> float:
            if soup_a <= 0 and soup_b <= 0:
                return 0.5
            if soup_a <= 0:
                return 1.0
            if soup_b <= 0:
                return 0.0
            if soup_a in states and soup_b in states[soup_a]:
                return states[soup_a][soup_b]

            state = (
                sum(calculate(soup_a + move[0], soup_b + move[1]) for move in moves)
                / 4.0
            )
            states[soup_a][soup_b] = state

            return state

        max_probability = 1 - 1e-5

        for serving in range(1, servings + 1):
            state = calculate(serving, serving)
            if state > max_probability:
                return 1.0

        return calculate(servings, servings)
