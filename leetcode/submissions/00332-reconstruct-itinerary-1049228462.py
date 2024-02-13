# Submission title: Reconstruct Itinerary
# Submission url  : https://leetcode.com/problems/reconstruct-itinerary/description/
# Submission url  : https://leetcode.com/submissions/detail/1049228462/
# Submission json : {"id":1049228462,"status_display":"Accepted","lang":"python3","question_id":332,"title_slug":"reconstruct-itinerary","code":"class Solution:\n    def findItinerary(self, tickets: List[List[str]]) -> List[str]:\n        graph = defaultdict(list)\n        \n        for src, dst in sorted(tickets, reverse=True):\n            graph[src].append(dst)\n            \n        itinerary = []\n        def dfs(airport: str) -> None:\n            while graph[airport]:\n                dfs(graph[airport].pop())\n            \n            itinerary.append(airport)\n        \n        dfs(\"JFK\")\n        \n        return itinerary[::-1]","title":"Reconstruct Itinerary","url":"/submissions/detail/1049228462/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694691703,"status":10,"runtime":"84 ms","is_pending":"Not Pending","memory":"16.7 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []

        def dfs(airport: str) -> None:
            while graph[airport]:
                dfs(graph[airport].pop())

            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]
