# Submission title: Minimum Time to Make Rope Colorful
# Submission url  : https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/"
# Submission url  : https://leetcode.com/submissions/detail/1129545299/"


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        i = 0
        j = 0

        while i < len(neededTime) and j < len(neededTime):
            currTotal = 0
            currMax = 0

            while j < len(neededTime) and colors[i] == colors[j]:
                currTotal += neededTime[j]
                currMax = max(currMax, neededTime[j])
                j += 1

            totalTime += currTotal - currMax
            i = j

        return totalTime
