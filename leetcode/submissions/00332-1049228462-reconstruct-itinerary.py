# Submission title: Reconstruct Itinerary
# Submission url  : https://leetcode.com/problems/reconstruct-itinerary/description/"
# Submission url  : https://leetcode.com/submissions/detail/1049228462/"


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
