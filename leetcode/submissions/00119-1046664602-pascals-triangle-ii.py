# Submission title: Pascal's Triangle II
# Submission url  : https://leetcode.com/problems/pascals-triangle-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1046664602/"


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = (1,)

        for i in range(1, rowIndex + 1):
            prev_row = (
                1,
                *(
                    prev_row[j] + prev_row[j + 1]
                    for j in range(len(prev_row) - 1)
                ),
                1,
            )

        return prev_row
