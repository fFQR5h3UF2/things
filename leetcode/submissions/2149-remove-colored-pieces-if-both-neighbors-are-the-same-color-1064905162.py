# Submission for Remove Colored Pieces if Both Neighbors are the Same Color
# Submission url: https://leetcode.com/submissions/detail/1064905162/


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cur_char, cur_conseq = colors[0], 1
        moves = {"A": 0, "B": 0}
        for char in colors:
            if char == cur_char:
                cur_conseq += 1
            else:
                moves[cur_char] += max(0, cur_conseq - 2)
                cur_char, cur_conseq = char, 1
        return moves["A"] > moves["B"]
