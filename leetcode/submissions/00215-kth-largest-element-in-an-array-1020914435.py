# Submission title: Kth Largest Element in an Array
# Submission url  : https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1020914435/
# Submission json : {"id":1020914435,"status_display":"Accepted","lang":"python3","question_id":215,"title_slug":"kth-largest-element-in-an-array","code":"class Solution:\n    def findKthLargest(self, nums, k):\n        heap = []\n        for num in nums:\n            heapq.heappush(heap, num)\n            if len(heap) > k:\n                heapq.heappop(heap)\n        \n        return heap[0]","title":"Kth Largest Element in an Array","url":"/submissions/detail/1020914435/","lang_name":"Python3","time":"5 months, 3 weeks","timestamp":1692001059,"status":10,"runtime":"476 ms","is_pending":"Not Pending","memory":"29.4 MB","compare_result":"1111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
