# Submission title: Kth Largest Element in an Array
# Submission url  : https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1020914435/"


class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
