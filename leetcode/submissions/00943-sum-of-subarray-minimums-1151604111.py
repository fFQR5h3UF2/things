# Submission title: Sum of Subarray Minimums
# Submission url  : https://leetcode.com/problems/sum-of-subarray-minimums/description/
# Submission url  : https://leetcode.com/submissions/detail/1151604111/
# Submission json : {"id":1151604111,"status_display":"Accepted","lang":"python3","question_id":943,"title_slug":"sum-of-subarray-minimums","code":"class Solution:\n    def sumSubarrayMins(self, arr: List[int]) -> int:\n        n = len(arr)\n        left = [-1] * n \n        right = [n] * n\n        stack = []\n\n        for i, value in enumerate(arr):\n            while stack and arr[stack[-1]] >= value:  \n                stack.pop()  \n            if stack:\n                left[i] = stack[-1]  \n            stack.append(i) \n\n        stack = [] \n\n        \n        for i in range(n - 1, -1, -1):  \n            while stack and arr[stack[-1]] > arr[i]: \n                stack.pop()  \n            if stack:\n                right[i] = stack[-1]  \n            stack.append(i) \n\n        mod = 10**9 + 7 \n\n        result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod\n      \n        return result ","title":"Sum of Subarray Minimums","url":"/submissions/detail/1151604111/","lang_name":"Python3","time":"2 weeks, 1 day","timestamp":1705760503,"status":10,"runtime":"368 ms","is_pending":"Not Pending","memory":"21.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        mod = 10**9 + 7

        result = (
            sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr))
            % mod
        )

        return result
