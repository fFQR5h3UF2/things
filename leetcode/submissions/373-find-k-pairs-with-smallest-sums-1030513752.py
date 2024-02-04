# Submission for Find K Pairs with Smallest Sums
# Submission url: https://leetcode.com/submissions/detail/1030513752/


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        heap = []
        heapify(heap)

        for first in nums1:
            for second in nums2:
                heappush(heap, (first + second, (first, second)))

        return tuple(pair for sum, pair in nsmallest(k, heap))
