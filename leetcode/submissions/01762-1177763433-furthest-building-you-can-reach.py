# Submission title: Furthest Building You Can Reach
# Submission url  : https://leetcode.com/problems/furthest-building-you-can-reach/description/"
# Submission url  : https://leetcode.com/submissions/detail/1177763433/"


class Solution:
    def furthestBuilding(
        self, heights: List[int], bricks: int, ladders: int
    ) -> int:
        heap = []
        i = 0
        length = len(heights)
        for i in range(length - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(heap, -diff)
            if bricks < 0:
                bricks += -heapq.heappop(heap)
                ladders -= 1
            if ladders < 0:
                return i
        return length - 1
