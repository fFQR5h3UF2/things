# Submission title: Widest Vertical Area Between Two Points Containing No Points
# Submission url  : https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/
# Submission url  : https://leetcode.com/submissions/detail/1124812187/"


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        max_width = 0

        for i in range(1, len(points)):
            width = points[i][0] - points[i - 1][0]
            max_width = max(max_width, width)

        return max_width
