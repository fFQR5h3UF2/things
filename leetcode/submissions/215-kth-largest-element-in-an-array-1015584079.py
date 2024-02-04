# Submission for 'Kth Largest Element in an Array'
# Submission url: https://leetcode.com/submissions/detail/1015584079/

class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
