# Submission for Reconstruct Itinerary
# Submission url: https://leetcode.com/submissions/detail/1049213507/


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        t_from_to = defaultdict(list)
        for t_from, t_to in tickets:
            t_from_to[t_from].append(t_to)

        for t_from in t_from_to:
            t_from_to[t_from].sort(reverse=True)

        print(t_from_to)

        answer = ["JFK"]
        while t_from_to:
            t_from = answer[-1]
            t_to_avail = t_from_to[t_from]
            answer.append(t_to_avail.pop())
            if not t_to_avail:
                t_from_to.pop(t_from)

        return answer
