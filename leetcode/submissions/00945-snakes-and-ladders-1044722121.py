# Submission title: for Snakes and Ladders
# Submission url  : https://leetcode.com/submissions/detail/1044722121/
# Submission json : {"id": 1044722121, "status_display": "Accepted", "lang": "python3", "question_id": 945, "title_slug": "snakes-and-ladders", "code": "class Solution:\n    def snakesAndLadders(self, board: List[List[int]]) -> int:\n        n = len(board)\n        board.reverse()\n\n        def intToPos(square):\n            r = (square - 1) // n\n            c = (square - 1) % n\n            if r % 2:\n                c = n - 1 - c\n            return [r, c]\n\n        q = deque()\n        q.append([1, 0]) \n        visit = set()\n        while q:\n            square, moves = q.popleft()\n            for i in range(1, 7):\n                nextSquare = square + i\n                r, c = intToPos(nextSquare)\n                if board[r][c] != -1:\n                    nextSquare = board[r][c]\n                if nextSquare == n * n:\n                    return moves + 1\n                if nextSquare not in visit:\n                    visit.add(nextSquare)\n                    q.append([nextSquare, moves + 1])\n        return -1", "title": "Snakes and Ladders", "url": "/submissions/detail/1044722121/", "lang_name": "Python3", "time": "4\u00a0months, 4\u00a0weeks", "timestamp": 1694264815, "status": 10, "runtime": "92 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def intToPos(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2:
                c = n - 1 - c
            return [r, c]

        q = deque()
        q.append([1, 0])
        visit = set()
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == n * n:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1
