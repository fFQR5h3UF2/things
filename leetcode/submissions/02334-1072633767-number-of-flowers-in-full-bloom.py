# Submission title: Number of Flowers in Full Bloom
# Submission url  : https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/"
# Submission url  : https://leetcode.com/submissions/detail/1072633767/"


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
