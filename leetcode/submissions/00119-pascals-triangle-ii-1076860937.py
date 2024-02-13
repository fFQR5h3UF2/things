# Submission title: Pascal's Triangle II
# Submission url  : https://leetcode.com/problems/pascals-triangle-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1076860937/
# Submission json : {"id":1076860937,"status_display":"Accepted","lang":"python3","question_id":119,"title_slug":"pascals-triangle-ii","code":"class Solution:\n    def getRow(self, rowIndex: int) -> List[int]:\n        cur, prev = [], [1]\n        row = 0\n\n        while row < rowIndex:\n            cur.append(1)\n            for i in range(1, len(prev)):\n                cur.append(prev[i] + prev[i-1])\n            cur.append(1)\n            prev.clear()\n            cur, prev = prev, cur\n            row += 1\n        \n        return prev ","title":"Pascal's Triangle II","url":"/submissions/detail/1076860937/","lang_name":"Python3","time":"3 months, 2 weeks","timestamp":1697477527,"status":10,"runtime":"46 ms","is_pending":"Not Pending","memory":"16.2 MB","compare_result":"1111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur, prev = [], [1]
        row = 0

        while row < rowIndex:
            cur.append(1)
            for i in range(1, len(prev)):
                cur.append(prev[i] + prev[i - 1])
            cur.append(1)
            prev.clear()
            cur, prev = prev, cur
            row += 1

        return prev
