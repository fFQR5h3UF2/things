# Submission title: Container With Most Water
# Submission url  : https://leetcode.com/problems/container-with-most-water/description/
# Submission url  : https://leetcode.com/submissions/detail/1008647326/"


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            if currentArea > maxArea:
                maxArea = currentArea

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
