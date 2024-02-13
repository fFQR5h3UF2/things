# Submission title: Maximum Number of Achievable Transfer Requests
# Submission url  : https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/
# Submission url  : https://leetcode.com/submissions/detail/1009581498/
# Submission json : {"id":1009581498,"status_display":"Accepted","lang":"python3","question_id":1723,"title_slug":"maximum-number-of-achievable-transfer-requests","code":"class Solution:\n    def __init__(self):\n        self.ans = 0\n\n    def helper(self, start, requests, indegree, n, count):\n        if start == len(requests):\n            for i in range(n):\n                if indegree[i] != 0:\n                    return\n            self.ans = max(self.ans, count)\n            return\n\n        # Take \n        indegree[requests[start][0]] -= 1\n        indegree[requests[start][1]] += 1\n        self.helper(start + 1, requests, indegree, n, count + 1)\n\n        # Not-take\n        indegree[requests[start][0]] += 1\n        indegree[requests[start][1]] -= 1\n        self.helper(start + 1, requests, indegree, n, count)\n\n    def maximumRequests(self, n, requests):\n        indegree = [0] * n\n        self.helper(0, requests, indegree, n, 0)\n        return self.ans","title":"Maximum Number of Achievable Transfer Requests","url":"/submissions/detail/1009581498/","lang_name":"Python3","time":"6 months","timestamp":1690910365,"status":10,"runtime":"1037 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def __init__(self):
        self.ans = 0

    def helper(self, start, requests, indegree, n, count):
        if start == len(requests):
            for i in range(n):
                if indegree[i] != 0:
                    return
            self.ans = max(self.ans, count)
            return

        # Take
        indegree[requests[start][0]] -= 1
        indegree[requests[start][1]] += 1
        self.helper(start + 1, requests, indegree, n, count + 1)

        # Not-take
        indegree[requests[start][0]] += 1
        indegree[requests[start][1]] -= 1
        self.helper(start + 1, requests, indegree, n, count)

    def maximumRequests(self, n, requests):
        indegree = [0] * n
        self.helper(0, requests, indegree, n, 0)
        return self.ans
