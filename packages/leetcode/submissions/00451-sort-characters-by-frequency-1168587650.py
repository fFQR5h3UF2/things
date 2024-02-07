# Submission title: for Sort Characters By Frequency
# Submission url  : https://leetcode.com/submissions/detail/1168587650/
# Submission json : {"id": 1168587650, "status_display": "Accepted", "lang": "python3", "question_id": 451, "title_slug": "sort-characters-by-frequency", "code": "class Solution:\n    def frequencySort(self, s: str) -> str:\n        counter = defaultdict(int)\n        for char in s:\n            counter[char] += 1\n        pq = [(-freq, char) for char, freq in counter.items()]\n        heapq.heapify(pq)\n        result = []\n        while pq:\n            freq, char = heapq.heappop(pq)\n            result.append(char * -freq)\n        return \"\".join(result)", "title": "Sort Characters By Frequency", "url": "/submissions/detail/1168587650/", "lang_name": "Python3", "time": "26\u00a0minutes", "timestamp": 1707292784, "status": 10, "runtime": "49 ms", "is_pending": "Not Pending", "memory": "17.9 MB", "compare_result": "111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1
        pq = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(pq)
        result = []
        while pq:
            freq, char = heapq.heappop(pq)
            result.append(char * -freq)
        return "".join(result)
