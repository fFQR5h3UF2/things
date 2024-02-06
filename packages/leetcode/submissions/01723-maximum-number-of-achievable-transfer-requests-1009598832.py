# Submission title: for Maximum Number of Achievable Transfer Requests
# Submission url  : https://leetcode.com/submissions/detail/1009598832/
# Submission json : {"id": 1009598832, "status_display": "Accepted", "lang": "python3", "question_id": 1723, "title_slug": "maximum-number-of-achievable-transfer-requests", "code": "class Solution:\n    def maximumRequests(self, n, requests):\n        current = [0] * n\n        length = len(requests)\n        \n        def backtrack(req_index: int, count: int) -> int:\n            if req_index == length:\n                return 0 if any(current) else count\n\n            req_from, req_to = requests[req_index]\n            \n            current[req_from] -= 1\n            current[req_to] += 1\n            take = backtrack(req_index + 1, count + 1)\n\n            current[req_from] += 1\n            current[req_to] -= 1\n            non_take = backtrack(req_index + 1, count)\n            \n            return max(take, non_take)\n        \n        return backtrack(0, 0)", "title": "Maximum Number of Achievable Transfer Requests", "url": "/submissions/detail/1009598832/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1690911488, "status": 10, "runtime": "759 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maximumRequests(self, n, requests):
        current = [0] * n
        length = len(requests)

        def backtrack(req_index: int, count: int) -> int:
            if req_index == length:
                return 0 if any(current) else count

            req_from, req_to = requests[req_index]

            current[req_from] -= 1
            current[req_to] += 1
            take = backtrack(req_index + 1, count + 1)

            current[req_from] += 1
            current[req_to] -= 1
            non_take = backtrack(req_index + 1, count)

            return max(take, non_take)

        return backtrack(0, 0)
