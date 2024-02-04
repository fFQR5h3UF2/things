# Submission for Online Election
# Submission url: https://leetcode.com/submissions/detail/1051859689/


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        times_people_last = defaultdict(lambda: defaultdict(int))
        times_people = defaultdict(lambda: defaultdict(int))
        for i in reversed(range(len(times))):
            person, time = persons[i], times[i]
            cur_votes = times_people[time][person]
            if cur_votes == 0:
                times_people_last[time][person] = i
            times_people[time][person] += 1

        self.results = {}
        for time in times_people:
            max_votes_person, max_votes_count = None, None
            for person, count in times_people[time].items():
                if max_votes_count and count < max_votes_count:
                    continue
                if max_votes_count is None or count > max_votes_count:
                    max_votes_person, max_votes_count = person, count
                    continue
                if (
                    times_people_last[time][max_votes_person]
                    > times_people_last[time][person]
                ):
                    max_votes_person, max_votes_count = person, count
            self.results[time] = max_votes_person

    def q(self, t: int) -> int:
        for i in reversed(range(t + 1)):
            if i in self.results:
                return self.results[i]

        return -1


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
