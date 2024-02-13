# Submission title: Pascal's Triangle II
# Submission url  : https://leetcode.com/problems/pascals-triangle-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1046664602/
# Submission json : {"id":1046664602,"status_display":"Accepted","lang":"python3","question_id":119,"title_slug":"pascals-triangle-ii","code":"class Solution:\n    def getRow(self, rowIndex: int) -> List[int]:\n        prev_row = (1,)\n        \n        for i in range(1, rowIndex + 1):\n            prev_row = (1, *(prev_row[j] + prev_row[j+1] for j in range(len(prev_row) - 1)), 1)\n        \n        return prev_row","title":"Pascal's Triangle II","url":"/submissions/detail/1046664602/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694448999,"status":10,"runtime":"33 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"1111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = (1,)

        for i in range(1, rowIndex + 1):
            prev_row = (
                1,
                *(prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)),
                1,
            )

        return prev_row
