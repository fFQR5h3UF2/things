# Submission title: Construct the Rectangle
# Submission url  : https://leetcode.com/problems/construct-the-rectangle/description/
# Submission url  : https://leetcode.com/submissions/detail/1002826029/"


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        return next(
            [area // width, width]
            for width in range(int(area**0.5), 0, -1)
            if area % width == 0
        )
