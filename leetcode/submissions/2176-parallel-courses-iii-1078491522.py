# Submission for Parallel Courses III
# Submission url: https://leetcode.com/submissions/detail/1078491522/


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        required = {i: [0, set()] for i in range(n)}

        for prev, nxt in relations:
            required[nxt - 1][1].add(prev - 1)

        max_time = 0

        while required:
            taken = set()
            for course, (time_count, reqs) in required.items():
                if len(reqs) == 0:
                    taken.add(course)
                    max_time = max(max_time, time_count + time[course])

            for course in taken:
                required.pop(course)

            for course, (_, reqs) in required.items():
                union = reqs & taken
                if union:
                    required[course][0] += max(time[item] for item in union)
                    reqs.difference_update(taken)

        return max_time
