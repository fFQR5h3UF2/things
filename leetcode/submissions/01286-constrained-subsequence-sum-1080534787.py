# Submission title: Constrained Subsequence Sum
# Submission url  : https://leetcode.com/problems/constrained-subsequence-sum/description/
# Submission url  : https://leetcode.com/submissions/detail/1080534787/
# Submission json : {"id":1080534787,"status_display":"Accepted","lang":"python3","question_id":1286,"title_slug":"constrained-subsequence-sum","code":"import heapq\n\nclass Solution:\n    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:\n        heap = [(-nums[0], 0)]\n        ans = nums[0]\n        \n        for i in range(1, len(nums)):\n            while i - heap[0][1] > k:\n                heapq.heappop(heap)\n\n            curr = max(0, -heap[0][0]) + nums[i]\n            ans = max(ans, curr)\n            heapq.heappush(heap, (-curr, i))\n\n        return ans","title":"Constrained Subsequence Sum","url":"/submissions/detail/1080534787/","lang_name":"Python3","time":"3 months, 2 weeks","timestamp":1697887253,"status":10,"runtime":"1729 ms","is_pending":"Not Pending","memory":"36.4 MB","compare_result":"111111111111111111111111111111111111","has_notes":false,"flag_type":1}

import heapq


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]

        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heapq.heappop(heap)

            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heapq.heappush(heap, (-curr, i))

        return ans
