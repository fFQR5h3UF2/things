# Submission title: for Seat Reservation Manager
# Submission url  : https://leetcode.com/submissions/detail/1050843823/
# Submission json : {"id": 1050843823, "status_display": "Accepted", "lang": "python3", "question_id": 1955, "title_slug": "seat-reservation-manager", "code": "class SeatManager:\n\n    def __init__(self, n: int):\n        self.heap = list(range(1, n + 1))  \n\n    def reserve(self) -> int:\n        return heappop(self.heap)\n\n    def unreserve(self, seatNumber: int) -> None:\n        heappush(self.heap, seatNumber)\n\n\n# Your SeatManager object will be instantiated and called as such:\n# obj = SeatManager(n)\n# param_1 = obj.reserve()\n# obj.unreserve(seatNumber)", "title": "Seat Reservation Manager", "url": "/submissions/detail/1050843823/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694867737, "status": 10, "runtime": "420 ms", "is_pending": "Not Pending", "memory": "44.1 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1, n + 1))

    def reserve(self) -> int:
        return heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)