# Submission title: for Maximal Network Rank
# Submission url  : https://leetcode.com/submissions/detail/1024664738/
# Submission json : {"id": 1024664738, "status_display": "Accepted", "lang": "python3", "question_id": 1738, "title_slug": "maximal-network-rank", "code": "class Solution:\n    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:\n        city_roads = [set() for _ in range(n)]\n\n        for city_one, city_two in roads:\n            city_roads[city_one].add(city_two)\n            city_roads[city_two].add(city_one)\n        \n        max_rank = 0\n\n        for city_one in range(n):\n            for city_two in range(city_one + 1, n):\n                rank = len(city_roads[city_one]) + len(city_roads[city_two])\n                if city_one in city_roads[city_two]:\n                    rank -= 1\n                \n                if rank > max_rank:\n                    max_rank = rank\n        \n        return max_rank", "title": "Maximal Network Rank", "url": "/submissions/detail/1024664738/", "lang_name": "Python3", "time": "5\u00a0months, 2\u00a0weeks", "timestamp": 1692345152, "status": 10, "runtime": "292 ms", "is_pending": "Not Pending", "memory": "18.5 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        city_roads = [set() for _ in range(n)]

        for city_one, city_two in roads:
            city_roads[city_one].add(city_two)
            city_roads[city_two].add(city_one)

        max_rank = 0

        for city_one in range(n):
            for city_two in range(city_one + 1, n):
                rank = len(city_roads[city_one]) + len(city_roads[city_two])
                if city_one in city_roads[city_two]:
                    rank -= 1

                if rank > max_rank:
                    max_rank = rank

        return max_rank
