# Submission title: for Design a Number Container System
# Submission url  : https://leetcode.com/submissions/detail/1050267339/
# Submission json : {"id": 1050267339, "status_display": "Accepted", "lang": "python3", "question_id": 2434, "title_slug": "design-a-number-container-system", "code": "class NumberContainers:\n\n    def __init__(self):\n        self.num_indices = defaultdict(list)\n        self.num_at_index = {}\n        \n\n    def change(self, index: int, number: int) -> None:\n        self.num_at_index[index] = number\n        heapq.heappush(self.num_indices[number], index)\n        \n\n    def find(self, number: int) -> int:\n        while self.num_indices[number] and self.num_at_index[self.num_indices[number][0]] != number:\n            heapq.heappop(self.num_indices[number])\n        \n        return self.num_indices[number][0] if len(self.num_indices[number]) > 0 else -1\n        \n\n\n# Your NumberContainers object will be instantiated and called as such:\n# obj = NumberContainers()\n# obj.change(index,number)\n# param_2 = obj.find(number)", "title": "Design a Number Container System", "url": "/submissions/detail/1050267339/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694797196, "status": 10, "runtime": "584 ms", "is_pending": "Not Pending", "memory": "72.6 MB", "compare_result": "111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class NumberContainers:

    def __init__(self):
        self.num_indices = defaultdict(list)
        self.num_at_index = {}

    def change(self, index: int, number: int) -> None:
        self.num_at_index[index] = number
        heapq.heappush(self.num_indices[number], index)

    def find(self, number: int) -> int:
        while (
            self.num_indices[number]
            and self.num_at_index[self.num_indices[number][0]] != number
        ):
            heapq.heappop(self.num_indices[number])

        return self.num_indices[number][0] if len(self.num_indices[number]) > 0 else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
