# Submission for Container With Most Water
# Submission url: https://leetcode.com/submissions/detail/1008597576/


class Solution:
    def maxArea(self, height: List[int]) -> int:

        length = len(height)
        max_area = 0

        for j in range(1, length):
            for i in range(0, j):
                area = min(height[i], height[j]) * (j - i)

                if area > max_area:
                    max_area = area

        return max_area
