# Submission title: Minimum Time to Make Rope Colorful
# Submission url  : https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
# Submission url  : https://leetcode.com/submissions/detail/1129545299/
# Submission json : {"id":1129545299,"status_display":"Accepted","lang":"python3","question_id":1700,"title_slug":"minimum-time-to-make-rope-colorful","code":"class Solution:\n    def minCost(self, colors: str, neededTime: List[int]) -> int:\n        totalTime = 0\n        i = 0\n        j = 0\n\n        while i < len(neededTime) and j < len(neededTime):\n            currTotal = 0\n            currMax = 0\n\n            while j < len(neededTime) and colors[i] == colors[j]:\n                currTotal += neededTime[j]\n                currMax = max(currMax, neededTime[j])\n                j += 1\n\n            totalTime += currTotal - currMax\n            i = j\n\n        return totalTime\n\n\n","title":"Minimum Time to Make Rope Colorful","url":"/submissions/detail/1129545299/","lang_name":"Python3","time":"1 month, 1 week","timestamp":1703667076,"status":10,"runtime":"869 ms","is_pending":"Not Pending","memory":"28.1 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


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
