# Submission for Max Points on a Line
# Submission url: https://leetcode.com/submissions/detail/1057823686/


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = defaultdict(set)
        length = len(points)
        for i in range(length):
            x1, y1 = points[i]
            for j in range(i + 1, length):
                x2, y2 = points[j]
                a, b = None, None
                if y1 == y2:
                    b = y1
                elif x1 == x2:
                    a = x1
                else:
                    a = (y2 - y1) // (x2 - x1)
                    b = y1 - a * x1
                lines[(a, b)].update(((x1, y1), (x2, y2)))
        return max((len(points) for points in lines.values()), default=0)
