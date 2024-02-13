# Submission title: Container With Most Water
# Submission url  : https://leetcode.com/problems/container-with-most-water/description/
# Submission url  : https://leetcode.com/submissions/detail/1057826154/
# Submission json : {"id":1057826154,"status_display":"Accepted","lang":"python3","question_id":11,"title_slug":"container-with-most-water","code":"class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        left = 0\n        right = len(height) - 1\n        maxArea = 0\n\n        while left < right:\n            currentArea = min(height[left], height[right]) * (right - left)\n            if currentArea > maxArea:\n                maxArea = currentArea\n\n            if height[left] < height[right]:\n                left += 1\n            else:\n                right -= 1\n\n        return maxArea","title":"Container With Most Water","url":"/submissions/detail/1057826154/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695551335,"status":10,"runtime":"576 ms","is_pending":"Not Pending","memory":"29.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


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
