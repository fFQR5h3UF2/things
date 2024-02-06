# Submission title: for Frog Jump
# Submission url  : https://leetcode.com/submissions/detail/1033274823/
# Submission json : {"id": 1033274823, "status_display": "Accepted", "lang": "python3", "question_id": 403, "title_slug": "frog-jump", "code": "class Solution:\n    def canCross(self, stones: List[int]) -> bool:\n        m = set(stones)\n        @cache\n        def dfs(i, j):\n            if i == stones[-1]: return True\n            return any(x and x + i in m and dfs(x + i, x) for x in range(j - 1, j + 2))\n        return dfs(0, 0)", "title": "Frog Jump", "url": "/submissions/detail/1033274823/", "lang_name": "Python3", "time": "5\u00a0months, 1\u00a0week", "timestamp": 1693148108, "status": 10, "runtime": "160 ms", "is_pending": "Not Pending", "memory": "25.9 MB", "compare_result": "1111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        m = set(stones)

        @cache
        def dfs(i, j):
            if i == stones[-1]:
                return True
            return any(x and x + i in m and dfs(x + i, x) for x in range(j - 1, j + 2))

        return dfs(0, 0)
