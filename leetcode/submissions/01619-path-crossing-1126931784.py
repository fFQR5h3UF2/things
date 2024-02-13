# Submission title: Path Crossing
# Submission url  : https://leetcode.com/problems/path-crossing/description/
# Submission url  : https://leetcode.com/submissions/detail/1126931784/
# Submission json : {"id":1126931784,"status_display":"Accepted","lang":"python3","question_id":1619,"title_slug":"path-crossing","code":"class Solution:\n    def isPathCrossing(self, path: str) -> bool:\n        moves = {\n            \"N\": (0, 1),\n            \"S\": (0, -1),\n            \"W\": (-1, 0),\n            \"E\": (1, 0)\n        }\n        \n        visited = {(0, 0)}\n        x = 0\n        y = 0\n\n        for c in path:\n            dx, dy = moves[c]\n            x += dx\n            y += dy\n            \n            if (x, y) in visited:\n                return True\n\n            visited.add((x, y))\n        \n        return False","title":"Path Crossing","url":"/submissions/detail/1126931784/","lang_name":"Python3","time":"1 month, 1 week","timestamp":1703367696,"status":10,"runtime":"31 ms","is_pending":"Not Pending","memory":"17.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moves = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}

        visited = {(0, 0)}
        x = 0
        y = 0

        for c in path:
            dx, dy = moves[c]
            x += dx
            y += dy

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
