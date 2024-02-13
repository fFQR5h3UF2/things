# Submission title: Partition Array for Maximum Sum
# Submission url  : https://leetcode.com/problems/partition-array-for-maximum-sum/description/
# Submission url  : https://leetcode.com/submissions/detail/1165825513/
# Submission json : {"id":1165825513,"status_display":"Accepted","lang":"python3","question_id":1121,"title_slug":"partition-array-for-maximum-sum","code":"class Solution:\n    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:\n        min_num = -1\n        length = len(arr)\n        last_idx = length - 1\n        cache = [-1] * length\n\n        def dp(start: int) -> int:\n            cached = cache[start]\n            if cached != -1:\n                return cached\n            max_num = min_num\n            max_sum = 0\n            for i in range(start, min(start + k, length)):\n                max_num = max(max_num, arr[i])\n                cur_sum = max_num * (i - start + 1)\n                if i != last_idx:\n                    cur_sum += dp(i + 1)\n                max_sum = max(max_sum, cur_sum)\n            cache[start] = max_sum\n            return max_sum\n        \n        return dp(0)\n            ","title":"Partition Array for Maximum Sum","url":"/submissions/detail/1165825513/","lang_name":"Python3","time":"2 hours, 3 minutes","timestamp":1707050286,"status":10,"runtime":"387 ms","is_pending":"Not Pending","memory":"17.6 MB","compare_result":"1111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        min_num = -1
        length = len(arr)
        last_idx = length - 1
        cache = [-1] * length

        def dp(start: int) -> int:
            cached = cache[start]
            if cached != -1:
                return cached
            max_num = min_num
            max_sum = 0
            for i in range(start, min(start + k, length)):
                max_num = max(max_num, arr[i])
                cur_sum = max_num * (i - start + 1)
                if i != last_idx:
                    cur_sum += dp(i + 1)
                max_sum = max(max_sum, cur_sum)
            cache[start] = max_sum
            return max_sum

        return dp(0)
