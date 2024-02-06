# Submission title: for Number of Flowers in Full Bloom
# Submission url  : https://leetcode.com/submissions/detail/1072633767/
# Submission json : {"id": 1072633767, "status_display": "Accepted", "lang": "python3", "question_id": 2334, "title_slug": "number-of-flowers-in-full-bloom", "code": "class Solution:\n    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:\n        flowers.sort()\n        sorted_people = sorted(people)\n        dic = {}\n        heap = []\n        \n        i = 0\n        for person in sorted_people:\n            while i < len(flowers) and flowers[i][0] <= person:\n                heapq.heappush(heap, flowers[i][1])\n                i += 1\n            \n            while heap and heap[0] < person:\n                heapq.heappop(heap)\n            \n            dic[person] = len(heap)\n\n        return [dic[x] for x in people]", "title": "Number of Flowers in Full Bloom", "url": "/submissions/detail/1072633767/", "lang_name": "Python3", "time": "3\u00a0months, 3\u00a0weeks", "timestamp": 1697029595, "status": 10, "runtime": "918 ms", "is_pending": "Not Pending", "memory": "44.6 MB", "compare_result": "1111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        flowers.sort()
        sorted_people = sorted(people)
        dic = {}
        heap = []

        i = 0
        for person in sorted_people:
            while i < len(flowers) and flowers[i][0] <= person:
                heapq.heappush(heap, flowers[i][1])
                i += 1

            while heap and heap[0] < person:
                heapq.heappop(heap)

            dic[person] = len(heap)

        return [dic[x] for x in people]
