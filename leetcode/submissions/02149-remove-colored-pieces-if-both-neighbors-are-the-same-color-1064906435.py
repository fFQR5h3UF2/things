# Submission title: Remove Colored Pieces if Both Neighbors are the Same Color
# Submission url  : https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description/
# Submission url  : https://leetcode.com/submissions/detail/1064906435/
# Submission json : {"id":1064906435,"status_display":"Accepted","lang":"python3","question_id":2149,"title_slug":"remove-colored-pieces-if-both-neighbors-are-the-same-color","code":"class Solution:\n    def winnerOfGame(self, colors: str) -> bool:\n        cur_char, cur_conseq = colors[0], 1\n        moves = {\"A\": 0, \"B\": 0}\n        for char in colors[1:]:\n            if char == cur_char:\n                cur_conseq += 1\n            else:\n                moves[cur_char] += max(0, cur_conseq - 2)\n                cur_char, cur_conseq = char, 1\n        if cur_conseq > 2:\n            moves[cur_char] += cur_conseq - 2\n        return moves[\"A\"] > moves[\"B\"]","title":"Remove Colored Pieces if Both Neighbors are the Same Color","url":"/submissions/detail/1064906435/","lang_name":"Python3","time":"4 months","timestamp":1696249253,"status":10,"runtime":"158 ms","is_pending":"Not Pending","memory":"17.3 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


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
