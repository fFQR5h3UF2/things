# Submission title: for Arranging Coins
# Submission url  : https://leetcode.com/submissions/detail/1001982716/
# Submission json : {"id": 1001982716, "status_display": "Accepted", "lang": "python3", "question_id": 441, "title_slug": "arranging-coins", "code": "class Solution:\n    def arrangeCoins(self, n: int) -> int:\n        left, right = 0, n\n\n        while left <= right:\n            middle = left + (right - left) // 2\n            coins = middle * (middle + 1) // 2\n\n            if coins == n:\n                return middle\n            \n            if coins > n:\n                right = middle - 1\n            else:\n                left = middle + 1\n        \n        return right\n", "title": "Arranging Coins", "url": "/submissions/detail/1001982716/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690132680, "status": 10, "runtime": "50 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            middle = left + (right - left) // 2
            coins = middle * (middle + 1) // 2

            if coins == n:
                return middle

            if coins > n:
                right = middle - 1
            else:
                left = middle + 1

        return right
