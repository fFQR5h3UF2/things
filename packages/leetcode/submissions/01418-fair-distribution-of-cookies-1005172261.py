# Submission title: for Fair Distribution of Cookies
# Submission url  : https://leetcode.com/submissions/detail/1005172261/
# Submission json : {"id": 1005172261, "status_display": "Accepted", "lang": "python3", "question_id": 1418, "title_slug": "fair-distribution-of-cookies", "code": "class Solution:\n    def distributeCookies(self, cookies: List[int], k: int) -> int:\n        cur = [0] * k\n        n = len(cookies)\n\n        def dfs(i, zero_count):\n            # If there are not enough cookies remaining, return `float('inf')` \n            # as it leads to an invalid distribution.\n            if n - i < zero_count:\n                return float('inf')\n            \n            # After distributing all cookies, return the unfairness of this\n            # distribution.\n            if i == n:\n                return max(cur)\n            \n            # Try to distribute the i-th cookie to each child, and update answer\n            # as the minimum unfairness in these distributions.\n            answer = float('inf')\n            for j in range(k):\n                zero_count -= int(cur[j] == 0)\n                cur[j] += cookies[i]\n                \n                # Recursively distribute the next cookie.\n                answer = min(answer, dfs(i + 1, zero_count))\n                \n                cur[j] -= cookies[i]\n                zero_count += int(cur[j] == 0)\n            \n            return answer\n        \n        return dfs(0, k)", "title": "Fair Distribution of Cookies", "url": "/submissions/detail/1005172261/", "lang_name": "Python3", "time": "6\u00a0months, 1\u00a0week", "timestamp": 1690447271, "status": 10, "runtime": "1604 ms", "is_pending": "Not Pending", "memory": "16.2 MB", "compare_result": "11111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cur = [0] * k
        n = len(cookies)

        def dfs(i, zero_count):
            # If there are not enough cookies remaining, return `float('inf')`
            # as it leads to an invalid distribution.
            if n - i < zero_count:
                return float("inf")

            # After distributing all cookies, return the unfairness of this
            # distribution.
            if i == n:
                return max(cur)

            # Try to distribute the i-th cookie to each child, and update answer
            # as the minimum unfairness in these distributions.
            answer = float("inf")
            for j in range(k):
                zero_count -= int(cur[j] == 0)
                cur[j] += cookies[i]

                # Recursively distribute the next cookie.
                answer = min(answer, dfs(i + 1, zero_count))

                cur[j] -= cookies[i]
                zero_count += int(cur[j] == 0)

            return answer

        return dfs(0, k)
