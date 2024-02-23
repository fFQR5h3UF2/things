# Submission title: Remove Colored Pieces if Both Neighbors are the Same Color
# Submission url  : https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description/
# Submission url  : https://leetcode.com/submissions/detail/1064906435/"


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cur_char, cur_conseq = colors[0], 1
        moves = {"A": 0, "B": 0}
        for char in colors[1:]:
            if char == cur_char:
                cur_conseq += 1
            else:
                moves[cur_char] += max(0, cur_conseq - 2)
                cur_char, cur_conseq = char, 1
        if cur_conseq > 2:
            moves[cur_char] += cur_conseq - 2
        return moves["A"] > moves["B"]
